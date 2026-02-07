def getPrompt(region: str, n: int = 8, days: int = 30):
    prompt = f"""
    당신은 '지역 땅값 점수'를 매기는 심사위원이다.
    지역: {region}

    최근 30일 뉴스 중 부동산/토지/주택가격 관련 뉴스를 참고하여
    현재 땅값에 적용할 변동폭(delta_pp, %p)을 판단하라.

    규칙:
    - delta_pp는 숫자만 출력 (-3.0 ~ +3.0 범위)
    - 근거로 사용한 뉴스 제목을 news_titles 배열에 포함
    - 출력은 JSON만
    """
    return prompt