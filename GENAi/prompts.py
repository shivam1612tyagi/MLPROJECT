# Template for generating a summary based on type and content
SUMMARY_PROMPT_TEMPLATE = """
You are a helpful AI assistant.
Generate a <TYPE> bullet-point summary of the following document:

<TEXT>


Summary:
- 
"""

# Template for extracting keywords
KEYWORD_PROMPT = """
Extract the 5 most important keywords from the following text:


<TEXT>


Keywords:
1. 
"""

# Template for generating comprehension questions
QUESTION_PROMPT = """
Generate 3 questions that test comprehension of the following text:


<TEXT>


Questions:
1.
"""
