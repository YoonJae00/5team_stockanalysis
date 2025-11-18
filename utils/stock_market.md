## 📌 기능 요약
한국투자증권 API의 APP KEY와 SECRET을 사용하여 접근 토큰을 발급받고, WebSocket을 연결하여 지정된 종목의 실시간 체결 데이터를 구독 및 수신합니다.

## ⚙️ 주요 클래스: KiRealtimeStreamer

### 1. __init__(settings, tr_id, stock_code)
* **기능**: 클래스 초기화. APP KEY, SECRET, URL 등의 설정 정보와 구독할 종목 코드, TR ID를 저장합니다.

### 2. get_access_token()
* **기능**: REST API를 호출하여 **접근 토큰**을 발급받고 `self.access_token`에 저장합니다.
* **로직**: `client_credentials` 방식으로 HTTP POST 요청을 통해 토큰을 요청합니다.

### 3. on_open(ws)
* **기능**: WebSocket 연결 성공 시 호출되는 콜백 함수.
* **로직**: 발급받은 `access_token`을 포함하여 **실시간 시세 구독(tr_type: "1") 요청 메시지**를 WebSocket 서버에 전송합니다.

### 4. on_message(ws, message)
* **기능**: 실시간 데이터 수신 시 호출되는 콜백 함수.
* **로직**: 수신된 메시지를 파싱하기 위해 `_process_realtime_data` 메서드를 호출합니다.

### 5. _process_realtime_data(message: 문자열)
* **기능**: 수신된 실시간 데이터 문자열을 파싱하고, 필요한 정보를 추출합니다.
* **로직**:
    1.  메시지를 구분자(`|`, `^`)로 분리하여 TR ID를 확인합니다.
    2.  TR ID가 **"H0STCNT0" (실시간 체결)**일 경우, 데이터에서 현재가, 시간, 종목 등을 추출하여 출력합니다.
    3.  **TODO**: 여기서 추출된 데이터를 외부 큐나 DB에 저장하는 로직이 추가될 수 있습니다.

### 6. on_error(ws, error) / on_close(ws, status_code, msg)
* **기능**: 에러 및 연결 종료 시 호출되는 콜백 함수. 상태 정보를 출력합니다.

### 7. run_streamer()
* **기능**: 스트리머 실행을 위한 메인 메서드.
* **로직**:
    1.  `get_access_token()`을 호출합니다.
    2.  `websocket.WebSocketApp` 객체를 생성하고, 위에서 정의한 콜백 함수들을 연결합니다.
    3.  `run_forever()`를 호출하여 WebSocket 연결을 유지하고 실시간 데이터를 수신하는 이벤트 루프를 시작합니다.

## 🤝 관계
* `user_loader.py`를 **활용**하여 API 접속에 필요한 키와 시크릿 등의 설정 정보를 로드합니다 (주석 처리된 가정 로직).
* (가정) 이 클래스가 수집한 실시간 데이터를 `stock_graph.py`가 **불러와서** 시각화합니다.