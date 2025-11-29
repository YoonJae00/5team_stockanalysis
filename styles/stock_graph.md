# 기능

## 1. 웹페이지의 메인 스크립트에서 실시간으로 표시할 주식 이름을 입력받습니다.
## 2. `styles/graph/main.py` 에서 주식 이름을 입력해서 주식 그래프 이미지을 확보합니다.
## 3. 확보한 주식 그래프 이미지를 웹페이지에 표시하는 블럭입니다.

# 사용법

## 이 블럭을 웹페이지에 포함시키고, `stock_name` 매개변수에 표시할 주식 이름을 전달합니다.

```python
from styles.graph.main import plot_stock_data

def display_stock_graph(stock_name: str):
    """
    주식 이름을 받아 해당 주식의 그래프 이미지를 웹페이지에 표시합니다.
    
    :param stock_name: 표시할 주식의 이름 (예: 'AAPL', 'GOOGL')
    """
    # 1. 주식 그래프 이미지 가져오기
    graph_image = plot_stock_data(stock_name)
    
    # 2. 웹페이지에 이미지 표시 (가상의 함수, 실제 구현은 웹 프레임워크에 따라 다름)
    render_image_on_webpage(graph_image)
```