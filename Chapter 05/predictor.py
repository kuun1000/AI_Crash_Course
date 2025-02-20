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

# 각 슬롯머신별 승패 수를 저장할 배열 생성
nPosReward = np.zeros(d)
nNegReward = np.zeros(d)

# 톰슨 샘플링
for i in range(N):
    selected = 0    # 선택된 슬롯머신
    maxRandom = 0   # 모든 슬롯머신에서 가장 높은 베타 분포 추정을 얻기 위해 사용됨

    for j in range(d):
        randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
        if randomBeta > maxRandom:
            maxRandom = randomBeta
            selected = j

    if X[i][selected] == 1:
        nPosReward[selected] += 1
    else:
        nNegReward[selected] += 1

# 최고라고 생각되는 슬롯머신 표시
nSelected = nPosReward + nNegReward
for i in range(d):
    print(f'Machine number: {i + 1} was selectd {nSelected[i]} times')
print(f'Conclusion: Best machine is machine number {np.argmax(nSelected) + 1}')