# main.py
import argparse
from utils import load_document, call_gpt, extract_keywords, generate_questions
from prompts import SUMMARY_PROMPT_TEMPLATE, KEYWORD_PROMPT, QUESTION_PROMPT

# Main function that orchestrates the document processing workflow
def main(file_path, summary_type):
    # Load and extract raw text from the provided input document
    text = load_document(file_path)

    # ======== Summarization ========
    # Format the prompt for summarization by injecting the summary type and document text
    summary_prompt = SUMMARY_PROMPT_TEMPLATE.replace("<TYPE>", summary_type).replace("<TEXT>", text)
    # Call GPT to generate a bullet-point summary
    summary = call_gpt(summary_prompt)
    # Save the summary output
    with open("outputs/summary.txt", "w") as f:
        f.write(summary.strip())

    # ======== Keyword Extraction ========
    # Format the prompt to extract important keywords from the document
    keyword_prompt = KEYWORD_PROMPT.replace("<TEXT>", text)
    keywords = extract_keywords(keyword_prompt)
    # Save extracted keywords
    with open("outputs/keywords.txt", "w") as f:
        f.write("\n".join(keywords))

    # ======== Question Generation ========
    # Format the prompt to generate comprehension-based questions
    question_prompt = QUESTION_PROMPT.replace("<TEXT>", text)
    questions = generate_questions(question_prompt)
    # Save the questions
    with open("outputs/questions.txt", "w") as f:
        f.write("\n".join(questions))

    # Log message to notify that the process is completed
    print("\n--- Output Generated ---")
    print("Summary, keywords, and questions saved in outputs folder.")

# Command-line interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="sample_input.txt", help="Path to PDF or TXT file (default: sample_input.txt)")  # Input file path
    parser.add_argument("--summary_type", choices=["brief", "detailed", "executive"], default="brief")  # Summary type
    args = parser.parse_args()

    main(args.file, args.summary_type)

