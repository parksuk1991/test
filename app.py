import streamlit as st

# 앱 제목
st.title("📱 간단 계산기")

# 사용자 입력 안내
st.write("두 숫자를 입력하고 원하는 연산을 선택하세요.")

# 숫자 입력
num1 = st.number_input("첫 번째 숫자", value=0.0, format="%.2f")
num2 = st.number_input("두 번째 숫자", value=0.0, format="%.2f")

# 연산 선택
operation = st.selectbox(
    "연산 선택",
    ["더하기 (+)", "빼기 (-)", "곱하기 (×)", "나누기 (÷)"]
)

# 계산 수행
result = None
if st.button("계산하기"):
    if operation == "더하기 (+)":
        result = num1 + num2
    elif operation == "빼기 (-)":
        result = num1 - num2
    elif operation == "곱하기 (×)":
        result = num1 * num2
    elif operation == "나누기 (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("0으로는 나눌 수 없습니다!")

    if result is not None:
        st.success(f"결과: {result}")
