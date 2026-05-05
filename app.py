import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="고2 물리 해결사", layout="centered")

st.title("🏹 고2 물리학1 풀이 생성기")
st.write("값을 입력하면 정석적인 풀이 과정을 생성합니다.")

# 2. 메뉴 선택
menu = st.selectbox("단원 선택", ["충격량과 운동량", "역학적 에너지 보존"])

st.divider()

# 3. 입력창 구성
if menu == "충격량과 운동량":
    m = st.number_input("질량 (m, kg)", value=2.0)
    v0 = st.number_input("처음 속력 (v0, m/s)", value=0.0)
    v1 = st.number_input("나중 속력 (v, m/s)", value=10.0)
    
    if st.button("풀이 생성"):
        result = m * v1 - m * v0
        st.subheader("📝 풀이 과정")
        # 수식과 변수를 안전하게 분리
        st.latex(r"I = \Delta p = m \cdot v - m \cdot v_0")
        st.latex(f"I = ({m} \\times {v1}) - ({m} \\times {v0})")
        st.success(f"최종 충격량: {result:.2f} N·s")

else: # 역학적 에너지 보존
    m = st.number_input("질량 (m, kg)", value=2.0)
    h = st.number_input("높이 (h, m)", value=5.0)
    v = st.number_input("현재 속력 (v, m/s)", value=0.0)
    g = 9.8
    
    if st.button("풀이 생성"):
        ep = m * g * h
        ek = 0.5 * m * (v**2)
        etot = ep + ek
        
        st.subheader("📝 풀이 과정")
        st.latex(r"E_{total} = mgh + \frac{1}{2}mv^2")
        st.write(f"1. 위치 에너지: ${m} \\times 9.8 \\times {h} = {ep:.2f} J$")
        st.write(f"2. 운동 에너지: $0.5 \\times {m} \\times {v}^2 = {ek:.2f} J$")
        st.latex(f"E_{{total}} = {ep:.2f} + {ek:.2f} = {etot:.2f} J")
        st.info(f"최종 역학적 에너지: {etot:.2f} J")tput)
