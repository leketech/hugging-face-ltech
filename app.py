from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbook = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
    gr.interface(fn=predict, inputs=textbox, outputs="text")

demo. launch()
