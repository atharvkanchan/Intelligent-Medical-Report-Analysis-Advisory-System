from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
qa_pipeline = pipeline("question-answering")

def summarize_text(text):
    if len(text) > 1000:
        text = text[:1000]
    result = summarizer(text, max_length=120, min_length=40)
    return result[0]['summary_text']

def answer_question(question, context):
    return qa_pipeline(question=question, context=context)
