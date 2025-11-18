# user_loader.py
import os
import json
from typing import List, Dict, Any

# 모듈이 사용할 기본 디렉토리 경로 (상수 정의)
DEFAULT_USERDATA_DIR = './userdata/'


def _load_single_json_file(filepath: str) -> Dict[str, Any] | None:
    """
    (내부 함수) 지정된 단일 JSON 파일에서 사용자 데이터를 로드합니다.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            user_data = json.load(f)
            return user_data
    except FileNotFoundError:
        print(f"⚠️ 오류: 파일을 찾을 수 없습니다 - {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"⚠️ 오류: JSON 디코딩 실패. 파일 형식을 확인하세요 - {filepath}")
        return None
    except Exception as e:
        print(f"⚠️ 알 수 없는 오류 발생: {e} - {filepath}")
        return None


def load_user_profiles(directory_path: str = DEFAULT_USERDATA_DIR,
                       extension: str = '.json') -> List[Dict[str, Any]]:
    """
    지정된 디렉토리에서 특정 확장자를 가진 모든 파일을 찾아 사용자 프로필 데이터를 로드하는 
    주요 공개 함수입니다.

    :param directory_path: 유저 데이터가 저장된 디렉토리 경로. (기본값: './userdata/')
    :param extension: 로드할 파일의 확장자. (기본값: '.json')
    :return: 로드된 모든 사용자 데이터를 담고 있는 딕셔너리 리스트.
    """
    all_user_data: List[Dict[str, Any]] = []
    
    # 1. 디렉토리 존재 여부 확인
    if not os.path.isdir(directory_path):
        print(f"⛔️ 경고: 디렉토리가 존재하지 않습니다: {directory_path}")
        return all_user_data
    
    # 2. 디렉토리 내용 탐색
    for filename in os.listdir(directory_path):
        if filename.endswith(extension):
            filepath = os.path.join(directory_path, filename)
            
            data = _load_single_json_file(filepath)
            
            if data is not None:
                all_user_data.append(data)
    
    return all_user_data