import streamlit as st

# 페이지 제목 설정
st.set_page_config(page_title="물리 계산기", page_icon="🚀")

st.title("🚀 물리 문제 풀이 도우미")
st.markdown("질량, 속도, 높이를 입력하면 **충격량**과 **역학적 에너지**를 자동으로 계산해줍니다.")

# 사이드바에서 모드 선택
mode = st.sidebar.selectbox('계산 모드 선택', ['충격량 구하기', '역학적 에너지 구하기'])

# 입력값 설정 (메인 화면)
st.subheader("1. 데이터 입력")
col1, col2 = st.columns(2)

with col1:
    m = st.number_input('질량 (kg)', value=2.0, step=0.1)
    v0 = st.number_input('초기 속력 (v0, m/s)', value=0.0, step=0.1)

with col2:
    v = st.number_input('나중 속력 (v, m/s)', value=10.0, step=0.1)
    h = st.number_input('높이 (h, m)', value=5.0, step=0.1)

g = 9.8  # 중력가속도

# 계산 및 출력 버튼
if st.button('풀이 과정 보기'):
    st.divider()
    st.subheader(f"📝 결과: {mode}")

    if mode == '충격량 구하기':
        # 계산: I = mv - mv0
        impulse = m * v - m * v0
        
        st.markdown("#### [단계 1: 공식 설정]")
        st.latex(r'I = \Delta p = m \cdot v - m \cdot v_0')
        
        st.markdown("#### [단계 2: 수치 대입]")
        st.latex(rf'I = ({m} \times {v}) - ({m} \times {v0})')
        
        st.success(f"**[단계 3: 최종 결과]** :  $I = {impulse:.2f} \, \\text{{N}}\cdot\\text{{s}}$")

    elif mode == '역학적 에너지 구하기':
        # 계산
        ep = m * g * h
        ek = 0.5 * m * (v**2)
        etot = ep + ek
        
        st.markdown("#### [단계 1: 각 에너지 공식]")
        st.latex(r'E_p = mgh, \quad E_k = \frac{1}{2}mv^2')
        
        st.markdown("#### [단계 2: 계산 과정]")
        st.latex(rf'E_p = {m} \times 9.8 \times {h} = {ep:.2f} \, \text{{J}}')
        st.latex(rf'E_k = \frac{{1}}{{2}} \times {m} \times {v}^2 = {ek:.2f} \, \text{{J}}')
        
        st.markdown("#### [단계 3: 역학적 에너지 합계]")
        st.info(f"**역학적 에너지 합** : $E_{{total}} = {ep:.2f} + {ek:.2f} = {etot:.2f} \, \\text{{J}}$")
display(widgets.VBox([mode, m_in, v0_in, v_in, h_in, calc_btn]), out)
