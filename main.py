import streamlit as st
import pandas as pd
import os

# CSV 파일 경로
DATA_FILE = "blood_data.csv"

# CSV 파일이 없으면 생성
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["name", "blood_type"])
    df.to_csv(DATA_FILE, index=False)

# CSV에서 데이터 로드
def load_data():
    return pd.read_csv(DATA_FILE)

# CSV에 데이터 저장
def save_data(name, blood_type):
    df = load_data()
    new_entry = pd.DataFrame([[name, blood_type]], columns=["name", "blood_type"])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

# 앱 제목
st.title("응급 혈액형 조회 및 등록 시스템 🩸")

# 메뉴 선택
menu = st.sidebar.selectbox("메뉴 선택", ["혈액형 조회", "혈액형 등록"])

if menu == "혈액형 조회":
    st.header("🔍 혈액형 조회")
    name = st.text_input("이름을 입력하세요")
    if st.button("조회"):
        df = load_data()
        person = df[df["name"] == name]
        if not person.empty:
            blood = person.iloc[0]["blood_type"]
            st.success(f"{name}님의 혈액형은 **{blood}형**입니다.")
        else:
            st.error("해당 이름의 혈액형 정보가 없습니다.")

elif menu == "혈액형 등록":
    st.header("✍️ 혈액형 등록")
    name = st.text_input("이름")
    blood_type = st.selectbox("혈액형", ["A", "B", "O", "AB"])
    if st.button("등록"):
        if name.strip() == "":
            st.warning("이름을 입력해주세요.")
        else:
            save_data(name.strip(), blood_type)
            st.success(f"{name}님의 혈액형이 {blood_type}형으로 등록되었습니다.")
