import gradio as gr
import groq_gradio

gr.load(
    name='llama-3.1-8b-instant',
    src=groq_gradio.registry,
).launch()