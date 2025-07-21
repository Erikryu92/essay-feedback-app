import os
from pdb import run
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
# .env 파일 로드
load_dotenv()

# 환경변수에서 API 키 불러오기
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
style = st.selectbox("Choose feedback style", ["Academic", "Friendly", "Professional"])
style_prompts = {
    "Academic": "You are an experienced academic writing coach who gives precise grammar and structure corrections.",
    "Friendly": "You are a friendly writing tutor who provides supportive and easy-to-understand suggestions.",
    "Professional": "You are a professional editor specializing in business English. Correct tone and clarity."
}
system_prompt = style_prompts[style]
user_input = st.text_area("Write your sentence")
if user_input:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    st.write(response.choices[0].message.content)