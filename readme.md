# OrthoQA-300

**OrthoQA-300** is a synthetic question-answering dataset focused on orthopedic surgical procedures. Each entry simulates a natural patient-provider interaction, with the question posed from a patient's perspective and the answer generated in a clinician-style tone using LLMs. The dataset is structured by both procedure and thematic category (e.g., “What is it?”, “Recovery”, “Risks”), allowing for organized downstream evaluation and experimentation.

This dataset was developed by **Stratum Research**, a lab focused on applied LLM systems for clinical reasoning.

---

## Overview

| Field       | Description                                               |
|-------------|-----------------------------------------------------------|
| `question`  | Patient-style question related to an orthopedic procedure |
| `answer`    | Synthetic answer generated to simulate clinical language  |
| `procedure` | Name of the orthopedic procedure (e.g. ACL Reconstruction)|
| `theme`     | Thematic label (e.g. "Recovery", "What is it?", etc.)     |

The data was generated using prompt engineering and open LLMs (via OpenRouter), without human supervision or manual revision. No PHI or real patient data was used.

---

## Example Entry

```json
{
  "question": "Can you explain what ACL reconstruction surgery actually involves?",
  "answer": "ACL reconstruction is a procedure where the torn ligament is replaced with a graft...",
  "procedure": "ACL Reconstruction",
  "theme": "What is it?"
}




## Setup

1. Install dependencies:
```bash
pip install openai python-dotenv
```

2. Set up your OpenRouter API key:
```bash
export OPENROUTER_API_KEY="your_key_here"
```

3. Configure the pipeline in `config.py` to adjust:
   - Model selection
   - Procedures and themes
   - Output paths
   - Prompt templates

## Usage

Run the complete pipeline:

```bash
python src/pipeline.py
```

This will:
- Generate prompts for all procedure/theme combinations
- Create questions using GPT-3.5-turbo
- Generate answers using GPT-3.5-turbo  
- Evaluate answer quality using GPT-4

## Output

All outputs are saved as JSON files in the `outputs/` directory:
- `prompts.json`: Generated prompts
- `questions.json`: Generated questions
- `answers.json`: Generated answers
- `judgments.json`: Quality evaluations

## Configuration

Edit `config.py` to customize:
- Models used for each stage
- List of orthopedic procedures
- Thematic categories
- Evaluation criteria
- File paths

## Models

- **Question/Answer Generation**: OpenAI GPT-3.5-turbo via OpenRouter
- **Quality Evaluation**: OpenAI GPT-4 via OpenRouter

The system uses OpenRouter to access OpenAI models with competitive pricing and reliability.