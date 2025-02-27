import numpy as np
import matplotlib.pyplot as plt
import random

# 매개변수 설정
N = 10000   # 고객 수
d = 9       # 전략 수

# 시뮬레이션 내 환경 생성
conversion_rates = [0.05, 0.13, 0.09, 0.16, 0.11, 0.04, 0.20, 0.08, 0.01]
X = np.zeros(shape=(N,d))
for i in range(N):
    for j in range(d):
        if np.random.rand() <= conversion_rates[j]:
            X[i][j] = 1

# 무작위 선택과 톰슨 샘플링 구현
strategies_selected_rs = []     # 무작위 선택 알고리즘에 의해 선택된 전략
strategies_selected_ts = []     # 톰슨 샘플링 AI 모델에 의해 선택된 전략
total_rewards_rs = 0            # 무작위 선택 알고리즘에 의한 누적 보상의 총합
total_rewards_ts = 0            # 톰슨 샘플링 AI 모델에 의한 누적 보상의 총합
number_of_rewards_1 = [0] * d   # 각 전략이 보상으로 1을 받은 횟수
number_of_rewards_0 = [0] * d   # 각 전략이 보상으로 0을 받은 횟수

for n in range(N):
    # 무작위 선택 
    strategy_rs = random.randrange(d)
    strategies_selected_rs.append(strategy_rs)
    reward_rs = X[n, strategy_rs]
    total_rewards_rs += reward_rs

    # 톰슨 샘플링 구현
    strategy_ts = 0
    max_random = 0
    for i in range(d):
        random_beta = random.betavariate(number_of_rewards_1[i] + 1, number_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            strategy_ts = i
    reward_ts = X[n, strategy_ts]
    if reward_ts == 1:
        number_of_rewards_1[strategy_ts] += 1
    else:
        number_of_rewards_0[strategy_ts] += 1
    strategies_selected_ts.append(strategy_ts)
    total_rewards_ts += reward_ts

# 상대 수익률 계산
relative_return = (total_rewards_ts - total_rewards_rs) / total_rewards_rs * 100
print(f"Relative Return: {relative_return}")

# 선택에 대한 히스토그램
plt.hist(strategies_selected_ts)
plt.title("Histogram of Selections")
plt.xlabel('Strategy')
plt.ylabel('Number of times the strategy was selected')
plt.savefig("Chapter 06/result.png")
plt.show()