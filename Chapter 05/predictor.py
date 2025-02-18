# 라이브러리 임포트
import numpy as np

# 전환률과 샘플 수 설정
conversionRates = [0.15, 0.04, 0.13, 0.11, 0.05]    # 각 슬롯 머신의 승률
N = 10000   # 샘플 수 -> 이길지 또는 언제 게임할 지 알려줄 사전 정의된 데이터셋 필요
d = len(conversionRates)    # 전환율 리스트의 길이 -> 슬롯 머신의 개수

# 데이터셋 생성 -> 특정 시간 단계 i에 대해 특정 슬롯머신에서 플레이했을 때 이길지를 알려주는 집합
X = np.zeros(shape=(N, d))  # N * d 크기의 0으로 채워진 2차원 배열
for i in range(N):
    for j in range(d):
        # 임의의 (0, 1) 범위 내의 부동소수점 값이 해당 슬롯 머신의 전환율보다 작은지 확인
        if np.random.rand() < conversionRates[j]:   
            X[i][j] = 1 