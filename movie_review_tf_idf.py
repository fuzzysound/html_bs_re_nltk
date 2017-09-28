# 'movie_reviews' corpus의 카테고리별 tf-idf 상위 15개 단어들을 찾는 과제

from nltk.corpus import movie_reviews
import matplotlib.pyplot as plt
import numpy as np
from tf_idf import *

pos_tf_idf = tf_idf(movie_reviews, 'pos') # positive 카테고리의 tf-idf 딕셔너리
pos_top_df = top_n(pos_tf_idf, 15) # 그 중 상위 15개의 데이터를 담은 pandas dataframe
pos_top_df = pos_top_df.iloc[::-1, :] # plot하면 아래위가 뒤집히므로 미리 뒤집어준다
neg_tf_idf = tf_idf(movie_reviews, 'neg')
neg_top_df = top_n(neg_tf_idf, 15)
neg_top_df = neg_top_df.iloc[::-1, :] # negative 카테고리도 같은 방법으로 dataframe 만들어줌

f, axes = plt.subplots(ncols=2, nrows=1)
yticks_pos = np.arange(pos_top_df.shape[0])
pos_yticks_label = pos_top_df['key']
pos_yticks_width = pos_top_df['value']
neg_yticks_label = neg_top_df['key']
neg_yticks_width = neg_top_df['value']
axes[0].barh(yticks_pos, pos_yticks_width, align='center')
axes[0].set_yticks(yticks_pos)
axes[0].set_yticklabels(pos_yticks_label)
axes[0].set_title('Positive Reviews')
axes[1].barh(yticks_pos, neg_yticks_width, align='center', color='crimson')
axes[1].set_yticks(yticks_pos)
axes[1].set_yticklabels(neg_yticks_label)
axes[1].set_title('Negative Reviews')


plt.suptitle('Top 15 TF-IDF Words in Movie Reviews')
plt.show()