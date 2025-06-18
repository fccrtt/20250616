import streamlit as st
import pandas as pd

# 전국 병원 예시 데이터
hospital_data = [
    {"name": "서울아산병원", "address": "서울특별시 송파구", "wait_time": 25, "congestion": "중간"},
    {"name": "세브란스병원", "address": "서울특별시 서대문구", "wait_time": 40, "congestion": "높음"},
    {"name": "삼성서울병원", "address": "서울특별시 강남구", "wait_time": 15, "congestion": "낮음"},
    {"name": "부산대병원", "address": "부산광역시 서구", "wait_time": 35, "congestion": "높음"},
    {"name": "전남대병원", "address": "광주광역시 동구", "wait_time": 20, "congestion": "낮음"},
    {"name": "충북대병원", "address": "충청북도 청주시", "wait_time": 28, "congestion": "중간"},
    {"name": "제주대병원", "address": "제주특별자치도 제주시", "wait_time": 40, "congestion": "높음"},
]

df = pd.DataFrame(hospital_data)

# 주소 분리 (시/도, 시/군/구)
df[['sido', 'sigungu']] = df['address'].str.split(" ", expand=True)

st.title("전국 응급실 대기 정보 조회 🏥")

# 1단계: 시/도 선택
sido_list = df['sido'].unique()
selected_sido = st.selectbox("📍 시/도를 선택하세요", options=sido_list)

# 2단계: 해당 시/도의 시/군/구 선택
sigungu_list = df[df['sido'] == selected_sido]['sigungu'].unique()
selected_sigungu = st.selectbox("🏙️ 시/군/구를 선택하세요", options=sigungu_list)

# 선택 지역 병원 필터링
filtered_df = df[(df['sido'] == selected_sido) & (df['sigungu'] == selected_sigungu)]

st.subheader(f"{selected_sido} {selected_sigungu} 지역 병원 목록")

if filtered_df.empty:
    st.warning("선택한 지역에 등록된 병원이 없습니다.")
else:
    hospital_names = filtered_df['name'].tolist()
    selected_hospital = st.selectbox("🏥 병원을 선택하세요", options=hospital_names)

    if st.button("🔍 조회하기"):
        hospital_info = filtered_df[filtered_df['name'] == selected_hospital].iloc[0]
        st.markdown(f"### {hospital_info['name']} 정보")
        st.write(f"- 주소: {hospital_info['address']}")
        st.write(f"- 예상 응급실 대기 시간: **{hospital_info['wait_time']}분**")
        st.write(f"- 현재 혼잡도: **{hospital_info['congestion']}**")

        # 혼잡도에 따라 메시지 출력
        if hospital_info['congestion'] == "높음":
            st.warning("현재 병원이 매우 혼잡하니 가능한 다른 병원을 이용하세요.")
        elif hospital_info['congestion'] == "중간":
            st.info("병원이 다소 혼잡합니다. 참고해주세요.")
        else:
            st.success("병원 혼잡도가 낮아 비교적 빠른 진료가 가능합니다.")
