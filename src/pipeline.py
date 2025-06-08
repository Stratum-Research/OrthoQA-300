import os
import re
import json
from openai import OpenAI
from dotenv import load_dotenv
import config
import utils

load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY")
)


def generate_prompts():
    prompts = []
    for proc in config.PROCEDURES:
        for theme in config.THEMES:
            prompts.append(
                {
                    "procedure": proc,
                    "theme": theme,
                    "prompt": f"You are a patient speaking with an orthopedic surgeon about '{proc}'. Generate {config.NUM_QUESTIONS} questions related to: '{theme}'. Return as a JSON list of strings: [\"question1\", \"question2\", ...]",
                }
            )

    utils.save_json(prompts, config.PATHS["prompts"])
    return prompts


def generate_questions(prompts):
    print(f"\nGenerating QUESTIONS from {len(prompts)} prompts")
    questions = []
    for prompt_data in prompts:
        print(prompt_data["prompt"])
        response = client.chat.completions.create(
            model=config.QUESTION_MODEL,
            messages=[{"role": "user", "content": prompt_data["prompt"]}],
            temperature=0.7,
        )

        api_response = response.choices[0].message.content.strip()
        print(f"API Response: {api_response}")

        try:
            question_list = json.loads(api_response)
            print(f"Parsed JSON: {question_list}")
            for q in question_list:
                print(q)
                questions.append(
                    {
                        "question": q,
                        "procedure": prompt_data["procedure"],
                        "theme": prompt_data["theme"],
                    }
                )
        except json.JSONDecodeError as e:
            print(f"JSON parsing failed: {e}")
            print(f"Raw response was: {repr(api_response)}")
            pass

    utils.save_json(questions, config.PATHS["questions"])
    return questions


def generate_answers(questions):
    print(f"\nGenerating ANSWERS from {len(questions)} questions")
    answers = []
    for q in questions:
        response = client.chat.completions.create(
            model=config.ANSWER_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": f"You are an experienced orthopedic surgeon. A patient is asking about '{q['procedure']}': {q['question']} Answer professionally in 2-3 sentences.",
                }
            ],
            temperature=0.3,
        )
        answer = response.choices[0].message.content.strip()
        print({**q, "answer": answer})
        answers.append({**q, "answer": answer})

    utils.save_json(answers, config.PATHS["answers"])
    return answers


def judge_answers(answers):
    print(f"\nJudging {len(answers)} answers")
    results = []
    for qa in answers:
        scoring = {}
        for dim in ["accuracy", "completeness", "hallucination"]:
            response = client.chat.completions.create(
                model=config.JUDGE_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": config.JUDGE_PROMPT_TEMPLATES[dim].format(
                            question=qa["question"], answer=qa["answer"]
                        ),
                    }
                ],
                temperature=0.1,
            )
            text = response.choices[0].message.content.strip()
            score_match = re.search(r"SCORE:\s*(\d+)", text)
            score = int(score_match.group(1)) if score_match else 3
            scoring[dim] = {"score": max(1, min(5, score)), "reasoning": text}
        print({**qa, "scoring": scoring})
        results.append({**qa, "scoring": scoring})

    utils.save_json(results, config.PATHS["judgments"])
    return results


def run_pipeline():
    print("Running pipeline...")
    prompts = generate_prompts()
    print(f"Generated {len(prompts)} prompts")

    questions = generate_questions(prompts)
    print(f"Generated {len(questions)} questions")

    answers = generate_answers(questions)
    print(f"Generated {len(answers)} answers")

    results = judge_answers(answers)
    print(f"Judged {len(results)} Q&A pairs")
    print("Pipeline complete!")
    print("\nAll outputs saved as JSON to outputs/ directory")


if __name__ == "__main__":
    run_pipeline()
