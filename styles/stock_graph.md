## 📌 기능 요약
실시간 주가 데이터를 시뮬레이션하거나(테스트 시) 실제로 불러와(실제 사용 시),
데이터를 처리한 후, **주가 추이 그래프**와 **최근 체결 정보 표**를 이미지(Base64 인코딩) 형태로 생성하여 반환합니다.

## ⚙️ 주요 함수

### 1. simulate_data_acquisition()
* **기능**: 테스트 및 시뮬레이션을 위해 더미 주가 데이터(시간, 가격, 종목 코드) 10건을 생성합니다.
* **로직**: 현재 시간부터 10초 간격으로 과거로 거슬러 올라가며 가상의 가격을 설정합니다.

### 2. execute_stock_visualization_pipeline(stock_name: 문자열)
* **기능**: 시각화 파이프라인의 메인 진입점. 데이터 수집부터 이미지 생성까지 전 과정을 실행합니다.
* **로직**:
    1.  **데이터 수집**: `simulate_data_acquisition()` (또는 실제 `KiRealtimeStreamer` 모듈)을 사용해 원본 주가 데이터를 불러옵니다.
    2.  **서버 시간 확인**: `utils.get_server_current_time()`을 호출하여 현재 서버 시간을 기록합니다.
    3.  **데이터 처리**: `utils.process_stock_data()`를 호출하여 원본 데이터를 DataFrame으로 변환합니다.
    4.  **그래프 생성**: `utils.generate_stock_chart_image()`를 호출하여 주가 추이 그래프를 PNG 바이트로 생성하고, 이를 **Base64 문자열로 인코딩**합니다.
    5.  **표 생성**: 처리된 DataFrame에서 최근 데이터를 추출하여 `utils.generate_table_image()`를 호출, 체결 정보를 표 이미지로 생성하고 **Base64 문자열로 인코딩**합니다.
    6.  **결과 반환**: 상태, 서버 시간, 표 이미지 Base64, 그래프 이미지 Base64가 포함된 딕셔너리를 반환합니다.

## 🤝 관계
* `stock_utils.py`의 함수들을 **호출**하여 데이터 처리(`process_stock_data`) 및 이미지 생성(`generate_stock_chart_image`, `generate_table_image`)을 수행합니다.
* (가정) `stock_market.py` (`KiRealtimeStreamer`) 모듈로부터 데이터를 **수신**합니다.