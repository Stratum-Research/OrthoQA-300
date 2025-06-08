![banner for project](assets/github%20banner.png)
# OrthoQA-300

**OrthoQA-300** is a structured, synthetic dataset of 300 patient-provider style question-and-answer (QA) pairs focused on orthopedic surgery. Each entry simulates a realistic clinical interaction, with patient-style questions and LLM-generated provider-style answers.
Questions are grouped by procedure (e.g., ACL Reconstruction, Total Hip Replacement) and theme (e.g., "What is it?", "Recovery", "Risks"). This structured format supports use in language model evaluation, prompt engineering, and clinical NLP prototyping.

**Table of Contents**
1. Dataset Overview
2. Intended Use
3. Example
4. Limitations
5. Contact
6. Citations


## Dataset Overview

| Field       | Description                                               |
|-------------|-----------------------------------------------------------|
| `question`  | A patient-style question about a surgical procedure       |
| `answer`    | LLM-generated answer in a provider-style tone             |
| `procedure` | Surgical procedure (e.g., "ACL Reconstruction")           |
| `theme`     | Thematic label (e.g., "Recovery", "What is it?")          |

No PHI or real patient data was used. All content is synthetic and generated using OpenRouter access to LLMs.



## Intended Use

OrthoQA-300 is designed as a sandbox dataset for early-stage clinical LLM research. It can be used to:

- Compare different LLMs (e.g., GPT-4o, Claude, Mistral) on structured medical questions
- Test judgment prompts and hallucination detection pipelines
- Prototype question-answering systems in clinical or surgical contexts
- Develop and test scoring systems prior to applying on real clinical data

While not suitable for training clinical models intended for **production deployment**, OrthoQA-300 supports reproducible research in LLM system design and evaluation.


## Example

```json
{
  "question": "Can you explain what ACL reconstruction surgery actually involves?",
  "answer": "ACL reconstruction is a procedure where the torn ligament is replaced with a graft...",
  "procedure": "ACL Reconstruction",
  "theme": "What is it?"
}
```

## Limitations
1. All answers are LLM-generated and not validated by medical professionals
2. This dataset is not intended for patient-facing tools or clinical decision support
3. Performance on this dataset does not imply safety or readiness for real-world deployment

## Contact
Abdullah Ridwan

Email: abdullahridwan [at] gmail [dot] com

## Citation
```yaml
@dataset{ridwan2024orthoqa,
  author  = {Abdullah Ridwan},
  title   = {OrthoQA-300: A Structured Synthetic Dataset for Orthopedic Surgery Q&A},
  year    = {2024},
  url     = {https://huggingface.co/datasets/stratum-research/orthoqa-300},
  doi     = {10.57967/hf/0000000},
  note    = {Version 1.0, Stratum Research}
}
```
