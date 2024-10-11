import gradio as gr
import groq_gradio

gr.load(
    name='llama-3.1-70b-versatile',
    src=groq_gradio.registry,
    title='Groq-Gradio Integration',
    description="Chat with llama-3.1-70b-versatile model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()
