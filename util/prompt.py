def getPrompt(region: str, n: int = 8, days: int = 30):
    prompt = f"""
    당신은 '지역 땅값 점수'를 매기는 심사위원이다.
    지역: {region}

    최근 30일 뉴스 중 부동산/토지/주택가격 관련 뉴스를 참고하여
    현재 땅값에 적용할 변동폭(delta_pp, %p)을 판단하라.

    규칙:
    - delta_pp는 숫자만 출력 (최소 ±3.0)
    - 다른 출력 없이 무조건 delta_pp만 출력
    - float 자료형으로 바로 변환하기 편하게 숫자만 출력

    결과, 근거 다 필요없고 무조건 delta_pp만 출력해
    """
    return prompt