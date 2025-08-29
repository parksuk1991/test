import streamlit as st

# 앱 제목
st.title("🧮 BMI 계산기 (Streamlit)")

# 사용자 입력: 키(cm)와 몸무게(kg)
height_cm = st.number_input("키를 입력하세요 (cm):", min_value=0.0, format="%.1f")
weight_kg = st.number_input("몸무게를 입력하세요 (kg):", min_value=0.0, format="%.1f")

# BMI 계산 버튼
if st.button("BMI 계산하기"):
    if height_cm > 0:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        bmi_rounded = round(bmi, 2)

        # BMI 분류 기준
        if bmi < 18.5:
            category = "저 체 중"
        elif 18.5 <= bmi <= 22.9:
            category = "정 상"
        elif 23 <= bmi <= 24.9:
            category = "비만전단계"
        elif 25 <= bmi <= 29.9:
            category = "1단계 비만"
        elif 30 <= bmi <= 34.9:
            category = "2단계 비만"
        else:
            category = "3단계 비만"

        st.success(f"당신의 BMI는 {bmi_rounded}입니다. ({category})")
    else:
        st.error("키를 올바르게 입력해주세요.")
