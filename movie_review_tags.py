from nltk.corpus import movie_reviews
from nltk import pos_tag, FreqDist
import re
import matplotlib.pyplot as plt
import numpy as np

movie_reviews_tagged = pos_tag(movie_reviews.words())
movie_reviews_tagged = [(word, tag) for word, tag in movie_reviews_tagged if re.match('[\w]+', tag)]
movie_reviews_tagged_fd = FreqDist(tag for (word, tag) in movie_reviews_tagged)
movie_reviews_tagged_fd_mc = movie_reviews_tagged_fd.most_common()

f, ax = plt.subplots(figsize=(30, 10))
xticks_pos = np.arange(len(movie_reviews_tagged_fd_mc))
tags, height = list(zip(*movie_reviews_tagged_fd_mc))
ax.bar(xticks_pos, height)
ax.set_xticks(xticks_pos)
ax.set_xticklabels(tags)
plt.title('Movie Reviews PoS Frequency')
plt.xlabel('Part of Speech')
plt.ylabel('Frequency')
plt.show()