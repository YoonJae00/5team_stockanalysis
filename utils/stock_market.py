import stock_market # 주식 실시간 정보를 받아오기 위한 외부 라이브러리

def get_stock_price(name: str ) -> float:
    """
    주식 이름을 입력받아 현재 주가를 반환하는 함수.
    
    Args:
        name (str): 주식 이름.
        
    Returns:
        float: 현재 주가.
    """
    price = stock_market.get_current_price(name)
    return price

def get_stock_history(name: str, days: int) -> list:
    """
    주식 이름과 일수를 입력받아 해당 기간 동안의 주가 변동을 반환하는 함수.
    
    Args:
        name (str): 주식 이름.
        days (int): 조회할 일수.
        
    Returns:
        list: 해당 기간 동안의 주가 변동 리스트.
    """
    history = stock_market.get_price_history(name, days)
    return history