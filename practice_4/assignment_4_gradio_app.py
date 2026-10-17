import os 

import gradio as gr
import requests

URL = "https://knowledge-retriever-mvp.vercel.app/api/ans_fact"

def answer_fact(question):
    response = requests.post(
        URL,
        json={"text": question},
    )
    response.raise_for_status()
    return response.json()["answer"]

gr.Interface(
    answer_fact,
    gr.Textbox(lines=8, label="Question"),
    gr.Textbox(label="Answer")).launch()