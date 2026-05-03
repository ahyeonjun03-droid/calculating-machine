import ipywidgets as widgets
from IPython.display import display, Math, HTML

# 결과 출력을 위한 전용 영역 생성
out = widgets.Output()

def show_solution(b):
    with out:
        out.clear_output()
        
        # 1. 입력값 가져오기
        m = float(m_in.value)
        v0 = float(v0_in.value)
        v = float(v_in.value)
        h = float(h_in.value)
        g = 9.8  # 중력가속도
        
        print(f"📝 선택한 분야: {mode.value}")
        print("-" * 40)

        if mode.value == '충격량 구하기':
            # 계산: I = mv - mv0
            impulse = m * v - m * v0
            
            display(Math(r'\mathbf{[단계 1: 공식 설정]}'))
            display(Math(r'I = \Delta p = m \cdot v - m \cdot v_0'))
            
            display(Math(r'\mathbf{[단계 2: 수치 대입]}'))
            display(Math(rf'I = ({m} \times {v}) - ({m} \times {v0})'))
            
            display(Math(rf'\mathbf{{[단계 3: 최종 결과]}} \quad I = {impulse:.2f} \, \text{{N}}\cdot\text{{s}}'))

        elif mode.value == '역학적 에너지 구하기':
            # 계산
            ep = m * g * h
            ek = 0.5 * m * (v**2)
            etot = ep + ek
            
            display(Math(r'\mathbf{[단계 1: 각 에너지 공식]}'))
            display(Math(r'E_p = mgh, \quad E_k = \frac{1}{2}mv^2'))
            
            display(Math(r'\mathbf{[단계 2: 계산 과정]}'))
            display(Math(rf'E_p = {m} \times 9.8 \times {h} = {ep:.2f} \, \text{{J}}'))
            display(Math(rf'E_k = \frac{{1}}{{2}} \times {m} \times {v}^2 = {ek:.2f} \, \text{{J}}'))
            
            display(Math(r'\mathbf{[단계 3: 역학적 에너지 합계]}'))
            display(Math(rf'E_{{total}} = {ep:.2f} + {ek:.2f} = {etot:.2f} \, \text{{J}}'))

# --- UI 구성 ---
mode = widgets.Dropdown(options=['충격량 구하기', '역학적 에너지 구하기'], description='모드:')
m_in = widgets.FloatText(value=2.0, description='질량(kg):')
v0_in = widgets.FloatText(value=0.0, description='초기속력(v0):')
v_in = widgets.FloatText(value=10.0, description='나중속력(v):')
h_in = widgets.FloatText(value=5.0, description='높이(h):')
calc_btn = widgets.Button(description="풀이 과정 보기", button_style='info')

calc_btn.on_click(show_solution)

# 화면 표시
display(widgets.VBox([mode, m_in, v0_in, v_in, h_in, calc_btn]), out)
display(widgets.VBox([mode, m_w, v0_w, v_w, h_w, btn]), output)
