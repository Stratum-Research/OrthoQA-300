# Ortho-Synthetic Dataset Generator

A modular pipeline for generating high-quality orthopedic surgery Q&A datasets using LLMs.

## Overview

This pipeline generates synthetic orthopedic surgery questions and answers, then evaluates their quality using an LLM-as-a-Judge approach. The system is designed to create training data for medical AI applications.

## Architecture

The pipeline consists of four main stages:

1. **Prompt Generation**: Creates structured prompts for different procedures and themes
2. **Question Generation**: Uses LLMs to generate relevant questions
3. **Answer Generation**: Generates comprehensive answers to the questions
4. **Quality Evaluation**: Uses LLM-as-a-Judge to score answers on accuracy, completeness, and hallucination detection

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