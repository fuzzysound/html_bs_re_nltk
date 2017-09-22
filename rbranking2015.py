import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tableparser import tableParser

url = 'https://www.fantasypros.com/nfl/reports/leaders/rb.php?year=2015'
parser = tableParser(url)
tables = parser.get_table()
table = tables[0]

df = pd.DataFrame(data = table)
num_cols = ['Avg', 'Games', 'Points']
for column in num_cols:
    df[column] = pd.to_numeric(df[column])
df_top10 = df.iloc[:10, ]
f, ax = plt.subplots()
ytick_labs = df_top10['Player']
ytick_pos = np.arange(df_top10.shape[0])
avg = df_top10['Avg']
ax.barh(ytick_pos, avg, height=.2, align='center')
ax.set_yticks(ytick_pos)
ax.set_yticklabels(ytick_labs)
plt.title("Top Running Bag's Avg")
plt.xlabel('Avg')
plt.show()