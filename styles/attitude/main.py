# 선호 성향 선택
 def show_menu():
+     """
+     투자 성향 선택 메뉴를 콘솔에 출력합니다.
+
+     기능:
+         - 3가지 투자 스타일을 화면에 표시
+         - 사용자 입력을 받을 준비만 하는 구조
+         - 실제 로직은 select_invest_type 함수가 처리
+
+     Returns:
+         None
+     """

    print("\n====================================")
    print("초보자도 쉽게 배우는 주식 프로그램")
    print("====================================")
    print("원하시는 투자 스타일을 선택하세요.\n")
    print("1) 배당 안정형")
    print("2) 성장 기술형")
    print("3) 생활 소비형")
    print("0) 종료\n")

# 선택된 성향에 따라 데이터 불러오기
+ def get_recommended_stocks(style_choice: str) -> dict:
+     """
+     사용자가 선택한 투자 성향(style_choice)에 맞는
+     추천 종목 데이터를 반환합니다.
+
+     Args:
+         style_choice (str): "1" ~ "3" 중 선택된 번호 문자열.
+
+     Returns:
+         dict: 선택한 성향에 해당하는 추천 데이터.
+               유효하지 않은 입력일 경우 None 반환.
+     """
    if style_choice == "1":
        return dataSet.get("배당 안정형")
    elif style_choice == "2":
        return dataSet.get("성장 기술형")
    elif style_choice == "3":
        return dataSet.get("생활 소비형")
    else:
        return None

# 추천 결과 출력값
+ def print_recommendation(data: dict):
+     """
+     투자 성향별 추천 데이터를 보기 좋게 출력합니다.
+
+     Args:
+         data (dict): dataSet에서 가져온 추천 데이터.
+
+     Returns:
+         None
+     """
+ def main():
+     """
+     프로그램 전체 실행 흐름을 제어합니다.
+
+     주요 단계:
+         1) 메뉴 출력
+         2) 사용자 입력 수집
+         3) 추천 데이터 조회
+         4) 추천 결과 출력
+
+     Returns:
+         None
+     """
