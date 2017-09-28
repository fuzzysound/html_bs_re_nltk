# 미국 nfl 러닝백 스탯 정보를 담은 페이지의 html 스크립트를
# tableParser를 이용해 파싱한 다음
# plot하는 과제

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tableparser import tableParser

url = 'https://www.fantasypros.com/nfl/reports/leaders/rb.php?year=2015' # 대상 페이지
parser = tableParser(url) # 파서 인스턴스
tables = parser.get_table() # 테이블 추출
table = tables[0] # 여러 테이블 중 첫 번째 테이블만이 의미있음

df = pd.DataFrame(data = table)
num_cols = ['Avg', 'Games', 'Points'] # 이 column들 안의 데이터는 파이썬 float 타입으로 바꾸어야 함
for column in num_cols:
    df[column] = pd.to_numeric(df[column]) # float 타입으로 바꿈
df_top10 = df.iloc[:10, ] # 상위 10명 추출. 원 데이터가 순위대로 정렬되어 있기 때문에 따로 정렬할 필요 없음.
f, ax = plt.subplots()
ytick_labs = df_top10['Player'] # y축에 표시할 선수 이름들
ytick_pos = np.arange(df_top10.shape[0]) # x축 tick들의 위치
avg = df_top10['Avg'] # bar의 길이로 나타낼 정보
ax.barh(ytick_pos, avg, height=.2, align='center')
ax.set_yticks(ytick_pos)
ax.set_yticklabels(ytick_labs)
plt.title("Top Running Bag's Avg")
plt.xlabel('Avg')
plt.gca().invert_yaxis() # y축을 위아래로 뒤집어 높은 순위가 위에 표시되도록
plt.show()