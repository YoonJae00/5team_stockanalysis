import stock_market as mt # Realtime으로 Stock Data를 제공하는 추상 API입니다


def get_stock_data(stock_name: str):
    """
    주어진 종목 이름에 대한 실시간 주가 데이터를 불러옵니다.

    Args:
        stock_name (str): 주가 데이터를 불러올 종목 이름.

    Returns:
        list: 주가 데이터 리스트. 각 항목은 딕셔너리 형태로 시간, 가격, 종목 코드를 포함합니다.
    """
    if not stock_name in mt.get_available_stocks():
        raise ValueError(f"'{stock_name}'은(는) 사용 가능한 주식 종목이 아닙니다.")
    
    # Realtime Stock Data Streamer 인스턴스 생성
    streamer = mt.KiRealtimeStreamer(stock_name)

    # 실시간 데이터 수신 (예시로 10건의 데이터 수신)
    stock_data = []
    for _ in range(10):
        data_point = streamer.get_realtime_data()
        stock_data.append(data_point)

    return stock_data

def get_stock_list():
    """
    사용 가능한 주식 종목 리스트를 반환합니다.

    Returns:
        list: 주식 종목 이름 리스트.
    """
    return mt.get_available_stocks()