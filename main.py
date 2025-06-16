import streamlit as st

# 미리 정의된 혈액형 데이터 (실제 서비스라면 데이터베이스를 사용할 수 있음)
blood_data = {
    "김민수": "A형",
    "이서준": "B형",
    "박지민": "O형",
    "최예린": "AB형",
    "정하늘": "A형",
}

st.title("응급 혈액형 조회 시스템 🩸")
st.write("이름을 입력하면 등록된 혈액형 정보를 확인할 수 있습니다.")

# 사용자 입력 받기
name = st.text_input("이름을 입력하세요")

# 조회 버튼
if st.button("혈액형 조회"):
    if name in blood_data:
        st.success(f"{name}님의 혈액형은 **{blood_data[name]}** 입니다.")
    else:
        st.error("해당 이름의 혈액형 정보가 등록되어 있지 않습니다.")

st.markdown("---")
st.caption("⚠️ 이 정보는 응급 상황에서 참고용으로 사용되며, 정확한 혈액형 확인은 병원 기록을 기준으로 해야 합니다.")
