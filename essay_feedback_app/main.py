import os
<<<<<<< HEAD
from pdb import run
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
=======
from openai import OpenAI
from dotenv import load_dotenv

>>>>>>> e841cc3ba3d18b7bb60ced9c9d6c14d2a92ef71f
# .env 파일 로드
load_dotenv()

# 환경변수에서 API 키 불러오기
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
<<<<<<< HEAD
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
=======

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "너는 한국에서 20년 경력의 작가로 첨삭을 전문적으로 해."},
        {"role": "user", "content": "안녕하세요 저는 글쓰기 연습을 하고 있습니다."}
    ]
)

print(response.choices[0].message.content)
>>>>>>> e841cc3ba3d18b7bb60ced9c9d6c14d2a92ef71f
