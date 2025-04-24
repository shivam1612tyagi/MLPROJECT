import os
import openai
import pdfplumber

# Load and extract text from PDF or TXT file
def load_document(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join([page.extract_text() or "" for page in pdf.pages])
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        raise ValueError("Unsupported file format. Use PDF or TXT.")
    return text[:6000]  # Truncate to fit OpenAI model token limits

# Send prompt to OpenAI and return the model's response
def call_gpt(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Load API key from environment variable
    client = openai.OpenAI()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# Parse the result and extract cleaned keywords
def extract_keywords(prompt):
    result = call_gpt(prompt)
    return [line.strip("- 1234567890. ") for line in result.splitlines() if line.strip()]

# Parse the result and extract cleaned comprehension questions
def generate_questions(prompt):
    result = call_gpt(prompt)
    return [line.strip("- 1234567890. ") for line in result.splitlines() if line.strip()]