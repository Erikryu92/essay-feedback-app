import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

# 1. .env 파일 로드 (환경변수 설정)
load_dotenv()

# 2. API 키 불러오기 및 클라이언트 설정
api_key = os.getenv("OPENAI_API_KEY")

# API 키가 없는 경우 에러 처리
if not api_key:
    st.error("OPENAI_API_KEY가 설정되지 않았습니다. .env 파일을 확인해주세요.")
    st.stop()

client = OpenAI(api_key=api_key)

# 3. Streamlit UI 구성
st.title("✍️ AI Writing Assistant")

# 스타일 선택 박스
style = st.selectbox("Choose feedback style", ["Academic", "Friendly", "Professional"])

# 스타일에 따른 프롬프트 정의
style_prompts = {
    "Academic": "You are an experienced academic writing coach who gives precise grammar and structure corrections.",
    "Friendly": "You are a friendly writing tutor who provides supportive and easy-to-understand suggestions.",
    "Professional": "You are a professional editor specializing in business English. Correct tone and clarity."
}

system_prompt = style_prompts[style]

# 사용자 입력 받기
user_input = st.text_area("Write your sentence", height=150)

# 4. 버튼 클릭 시 AI 호출
if st.button("Get Feedback"):
    if user_input:
        with st.spinner("Analyzing..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_input}
                    ]
                )
                st.success("Analysis Complete!")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a sentence first.")