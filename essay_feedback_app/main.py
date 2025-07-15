import os
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경변수에서 API 키 불러오기
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "너는 한국에서 20년 경력의 작가로 첨삭을 전문적으로 해."},
        {"role": "user", "content": "안녕하세요 저는 글쓰기 연습을 하고 있습니다."}
    ]
)

print(response.choices[0].message.content)