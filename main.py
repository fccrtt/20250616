import streamlit as st
import pandas as pd

# 모의 데이터 (병원명, 주소, 응급실 대기 시간(분), 혼잡도)
hospital_data = [
    {"name": "서울아산병원", "address": "서울 송파구", "wait_time": 25, "congestion": "중간"},
    {"name": "세브란스병원", "address": "서울 서대문구", "wait_time": 40, "congestion": "높음"},
    {"name": "삼성서울병원", "address": "서울 강남구", "wait_time": 15, "congestion": "낮음"},
    {"name": "서울대병원", "address": "서울 종로구", "wait_time": 30, "congestion": "중간"},
    {"name": "강남성심병원", "address": "서울 강남구", "wait_time": 50, "congestion": "높음"},
]

df = pd.DataFrame(hospital_data)

st.title("응급실 대기 시간 및 병원 혼잡도 조회 🏥")

# 사용자 위치 선택 (서울시 구 이름)
gu_list = df['address'].unique()
selected_gu = st.selectbox("지역을 선택하세요", options=gu_list)

# 선택한 지역 병원 리스트 필터링
filtered_df = df[df['address'] == selected_gu]

st.subheader(f"{selected_gu} 지역 병원 리스트")

# 병원명 선택
hospital_names = filtered_df['name'].tolist()
selected_hospital = st.selectbox("병원을 선택하세요", options=hospital_names)

if s
