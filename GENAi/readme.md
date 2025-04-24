# GenAI — Prompt Engineering & Summarization

## 📌 Overview
This project uses Generative AI (via OpenAI API) to:
- Summarize long documents in bullet points
- Extract top 5 keywords
- Generate 3 comprehension-based questions
- Support multiple summary types: brief, detailed, executive

## 🚀 How to Run

### 1. Install Dependencies
```bash
1. conda create -p venv python==3.10 -y
2. conda activate venv/
3. pip install -r requirements.txt
4. python main.py --file sample_input.pdf --summary_type detailed



## 📁 Output
- `outputs/summary.txt`
- `outputs/keywords.txt`
- `outputs/questions.txt`

## 🧠 Prompt Templates
All prompts are stored in `prompts.py` and dynamically updated using placeholders `<TEXT>` and `<TYPE>`.

## 🗂 Folder Structure
```
genai_summary/
├── main.py
├── utils.py
├── prompts.py
├── outputs/
│   ├── summary.txt
│   ├── keywords.txt
│   └── questions.txt
├── sample_input.txt
├── requirements.txt
├── setup.py
└── README.md
```