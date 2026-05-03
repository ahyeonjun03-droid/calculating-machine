import ipywidgets as widgets
from IPython.display import display, HTML, Math

# 수식을 깔끔하게 출력하기 위한 함수
def print_math(latex_str):
    display(Math(latex_str))

print("🎓 물리학1 풀이 과정 생성기 (수정판)")
print("-" * 50)

# 선택 메뉴
mode = widgets.Dropdown(
    options=['충격량-운동량', '역학적 에너지'], 
    value='충격량-운동량',
    description='분야 선택:'
)

# 입력 위젯들
m_w = widgets.FloatText(value=2.0, description='질량 (m, kg):')
v0_w = widgets.FloatText(value=0, description='초기속력 (v0, m/s):')
v_w = widgets.FloatText(value=10.0, description='나중속력 (v, m/s):')
h_w = widgets.FloatText(value=5.0, description='높이 (h, m):')

btn = widgets.Button(description="풀이 생성하기", button_style='success')
output = widgets.Output()

def generate_solution(b):
    with output:
        output.clear_output()
        g = 9.8 # 중력가속도 상수
        
        if mode.value == '충격량-운동량':
            impulse = m_w.value * v_w.value - m_w.value * v0_w.value
            print_math(r'\text{1. 사용 공식: } I = \Delta p = m v - m v_0')
            print_math(rf'\text{{2. 수치 대입: }} I = ({m_w.value} \times {v_w.value}) - ({m_w.value} \times {v0_w.value})')
            print_math(rf'\text{{3. 결과: }} I = {impulse:.2f} \, \text{{N}}\cdot\text{{s}}')
            
        elif mode.value == '역학적 에너지':
            ep = m_w.value * g * h_w.value
            ek = 0.5 * m_w.value * (v_w.value ** 2)
            etot = ep + ek
            print_math(r'\text{1. 사용 공식: } E_{total} = mgh + \frac{1}{2}mv^2')
            print_math(rf'\text{{2. 위치 에너지(E_p): }} {m_w.value} \times 9.8 \times {h_w.value} = {ep:.2f} \, \text{{J}}')
            print_math(rf'\text{{3. 운동 에너지(E_k): }} \frac{{1}}{{2}} \times {m_w.value} \times {v_w.value}^2 = {ek:.2f} \, \text{{J}}')
            print_math(rf'\text{{4. 역학적 에너지 합계: }} {etot:.2f} \, \text{{J}}')

btn.on_click(generate_solution)
display(widgets.VBox([mode, m_w, v0_w, v_w, h_w, btn]), output)
