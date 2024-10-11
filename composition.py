import gradio as gr
import groq_gradio

with gr.Blocks() as demo:
    with gr.Tab("llama-3.1-70b-versatile"):
        gr.load('llama-3.1-70b-versatile', src=groq_gradio.registry)
    with gr.Tab("llama-3.1-8b-instant"):
        gr.load('llama-3.1-8b-instant', src=groq_gradio.registry)

demo.launch()
