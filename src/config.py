QUESTION_MODEL = "deepseek/deepseek-r1-0528:free"
ANSWER_MODEL = "deepseek/deepseek-r1-0528:free"
JUDGE_MODEL = "deepseek/deepseek-r1-0528:free"

NUM_QUESTIONS = 1

PATHS = {
    "prompts": "generated_prompts.jsonl",
    "questions": "generated_questions.json",
    "answers": "generated_answers.json",
    "judgments": "judged_results.json",
}

PROCEDURES = [
    "ACL Reconstruction",
    "Total Hip Replacement",
    "Total Knee Replacement",
    "Rotator Cuff Repair",
    "Meniscus Surgery",
    "Labral Tear",
    "Shoulder Dislocation",
    "Arthritis Management",
    "Carpal Tunnel Release",
    "Spinal Fusion",
]

THEMES = [
    "What is it?",
    "What are the risks/complications?",
    "What is the recovery like?",
    "When can I return to activities?",
    "What are the alternatives?",
    "Do I need surgery or a second opinion?",
]

JUDGE_PROMPT_TEMPLATES = {
    "accuracy": """You are an expert orthopedic surgeon evaluating the following answer for factual accuracy.

Question: {question}
Answer: {answer}

Evaluate the answer and score it from 1 to 5:
- 5 = completely accurate
- 3 = minor factual issues
- 1 = major errors or incorrect medical info

Explain your reasoning. Return both the score and your explanation.
Format your response as:
SCORE: [number]
Reasoning: [your explanation]""",
    "completeness": """You are an expert orthopedic surgeon evaluating the following answer for completeness.

Question: {question}
Answer: {answer}

Evaluate how comprehensive the answer is and score it from 1 to 5:
- 5 = completely comprehensive, covers all important aspects
- 3 = covers main points but missing some details
- 1 = incomplete, missing critical information

Explain your reasoning. Return both the score and your explanation.
Format your response as:
SCORE: [number]
Reasoning: [your explanation]""",
    "hallucination": """You are an expert orthopedic surgeon evaluating the following answer for hallucination (fabricated information).

Question: {question}
Answer: {answer}

Evaluate if the answer contains any fabricated or invented information and score it from 1 to 5:
- 1 = no hallucinated content detected
- 3 = minor speculation presented as fact
- 5 = significant fabricated medical information

Explain your reasoning. Return both the score and your explanation.
Format your response as:
SCORE: [number]
Reasoning: [your explanation]""",
}
