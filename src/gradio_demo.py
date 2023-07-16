import gradio as gr
from retrieval import retrieve

demo = gr.Interface(fn=retrieve, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch(share=True)