import utils.stock_load
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64


def plot_stock_data(stock_name: str):
    """
    주어진 종목 이름에 대한 주가 데이터를 그래프로 시각화하고,
    그래프 이미지를 Base64 인코딩된 문자열로 반환합니다.

    Args:
        stock_name (str): 주가 데이터를 불러올 종목 이름.

    Returns:
        str: Base64 인코딩된 그래프 이미지 문자열.
    """
    # 주가 데이터 불러오기
    stock_data = utils.stock_load.get_stock_data(stock_name)
    
    # 데이터 파싱
    times = [data_point['time'] for data_point in stock_data]
    prices = [data_point['price'] for data_point in stock_data]

    # 그래프 생성
    plt.figure(figsize=(10, 5))
    plt.plot(times, prices, marker='o', linestyle='-', color='b')
    plt.title(f"{stock_name} 주가 추이")
    plt.xlabel("시간")
    plt.ylabel("가격 (원)")
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()

    # 그래프를 이미지로 저장
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    
    # Base64 인코딩
    img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')
    
    # 리소스 해제
    plt.close()

    return img_base64