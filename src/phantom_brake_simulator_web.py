import plotly.graph_objects as go
import numpy as np
from tracker_web import log_app_usage

def simulate_sensor_fusion_dilemma(output_filename="phantom_braking_chart.html"):
    # 1. 시뮬레이션 시간축 설정 (0~10초, 데이터 포인트를 200개로 늘려 정밀도 향상)
    time_steps = np.linspace(0, 10, 200)
    
    # 2. 기본 센서 신뢰도 데이터 생성 (평상시 90점 이상)
    camera_confidence = np.full_like(time_steps, 95.0)
    radar_confidence = np.full_like(time_steps, 92.0)
    
    # 3. 데이터 및 로그 생성
    brake_trigger_active = []
    
    print("="*60)
    print("자율주행 시스템 상태 모니터링 시작 (Real-time Sensor Fusion)...")
    print("="*60)

    for index, current_time in enumerate(time_steps):
        # 4.5초에서 5.5초 사이에 레이더 난반사(Multipath Effect) 강제 발생
        if 4.5 <= current_time <= 5.5:
            # 레이더 신뢰도가 40 미만으로 툭 떨어짐 (노이즈 추가)
            radar_confidence[index] = 25.0 + np.random.normal(0, 3)
            camera_confidence[index] = 95.0 + np.random.normal(0, 1)
        else:
            # 평상시 노이즈
            radar_confidence[index] += np.random.normal(0, 1)
            camera_confidence[index] += np.random.normal(0, 1)

        # 4. 제동 판단 로직 (Fail-Safe)
        # 레이더나 카메라 중 하나라도 40점 미만이면 즉시 제동
        is_braking = radar_confidence[index] < 40 or camera_confidence[index] < 40
        brake_trigger_active.append(100 if is_braking else 0)

        # 5. 특정 구간 로그 출력
        if 4.3 <= current_time <= 5.7:
            if is_braking:
                msg = f"[{current_time:.2f}s] !! PHANTOM BRAKE (FAIL-SAFE) !! | R:{radar_confidence[index]:.1f}, C:{camera_confidence[index]:.1f}"
                print(msg)
            else:
                print(f"[{current_time:.2f}s] NORMAL | 주행 유지 (R:{radar_confidence[index]:.1f}, C:{camera_confidence[index]:.1f})")

    # 6. Plotly 시각화 (그래프가 직선이 아닌 실제 데이터처럼 흔들리게 표현)
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=time_steps, y=camera_confidence, mode='lines', name='카메라 신뢰도', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=time_steps, y=radar_confidence, mode='lines', name='레이더 신뢰도', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=time_steps, y=brake_trigger_active, mode='none', fill='tozeroy', name='제동 발동', fillcolor='rgba(255, 0, 0, 0.3)'))

    fig.update_layout(
        title="자율주행 센서 데이터 충돌 시뮬레이션",
        xaxis_title="시간(s)", yaxis_title="신뢰도 점수",
        template="plotly_white", yaxis=dict(range=[0, 110])
    )

    fig.write_html(output_filename)
    print("="*60)
    print(f"시뮬레이션 완료. 결과 파일: {output_filename}")

if __name__ == "__main__":
    log_app_usage("phantom_brake_simulator", "simulator_started")
    simulate_sensor_fusion_dilemma()