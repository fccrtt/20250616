import streamlit as st
import pandas as pd

# 병원별 모의 데이터
hospital_data = [
    {"name": "서울아산병원", "address": "서울 송파구", "wait_time": 25, "congestion": "중간"},
    {"name": "세브란스병원", "address": "서울 서대문구", "wait_time": 40, "congestion": "높음"},
    {"name": "삼성서울병원", "address": "서울 강남구", "wait_time": 15, "congestion": "낮음"},
    {"name": "서울대병원", "address": "서울 종로구", "wait_time": 30, "congestion": "중간"},
    {"name": "강남성심병원", "address": "서울 강남구", "wait_time": 50, "congestion": "높음"},
]

df = pd.DataFrame(hospital_data)

st.title("응급실 대기 시간 및 병원 혼잡도 조회 🏥")

# 지역 선택
gu_list = df['address'].unique()
selected_gu = st.selectbox("지역을 선택하세요", options=gu_list)

# 선택 지역 병원 필터링
filtered_df = df[df['address'] == selected_gu]

st.subheader(f"{selected_gu} 지역 병원 리스트")

hospital_names = filtered_df['name'].tolist()
selected_hospital = st.selectbox("병원을 선택하세요", options=hospital_names)

if st.button("조회하기"):
    hospital_info = filtered_df[filtered_df['name'] == selected_hospital].iloc[0]
    st.markdown(f"### {hospital_info['name']} 정보")
    st.write(f"- 주소: {hospital_info['address']}")
    st.write(f"- 예상 응급실 대기 시간: **{hospital_info['wait_time']}분**")
    st.write(f"- 현재 혼잡도: **{hospital_info['congestion']}**")

    if hospital_info['congestion'] == "높음":
        st.warning("현재 병원이 매우 혼잡하니 가능한 다른 병원을 이용하세요.")
    elif hospital_info['congestion'] == "중간":
        st.info("병원이 다소 혼잡합니다. 참고해주세요.")
    else:
        st.success("병원 혼잡도가 낮아 비교적 빠른 진료가 가능합니다.")
