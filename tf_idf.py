# Corpus를 받아 카테고리에 따라 단어들의 tf-idf를 계산하는 모듈
# 각 문서들별로 단어들의 tf-idf를 계산하여, 카테고리 내 모든 단어들의 각각의 tf-idf 총합을 딕셔너리로 반환
# 계산 부분은 numpy로 구현함

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import numpy as np
import pandas as pd

lemmatizer = WordNetLemmatizer() # lemmatizing하는 인스턴스
stopwords = stopwords.words('english') # 영어의 stopwords

def preprocess(word, metadata): # 각 단어들을 분석에 알맞게 필터링하는 파이프라인 함수
    word = word.lower() # 소문자화
    if word in stopwords: # stopwords이면
        return # 거름
    if not re.match('[A-Za-z]+', word): # 알파벳이 아니어도
        return # 거름
    word = lemmatizer.lemmatize(word) # lemmatize
    metadata[word] = metadata.get(word, 0) + 1 # 여기까지 통과할 경우, metadata에 업데이트
    return

def produce_metadata(fileid, corpus): # 문서의 metadata를 만들어내는 함수
    metadata = {} # 문서의 word count 정보를 담을 딕셔너리
    words = corpus.words(fileids=fileid) # 해당 문서의 단어들을 불러옴
    for word in words:
        preprocess(word, metadata) # 모든 단어에 대해 필터링 수행, metadata 완성
    return metadata

def tf(tf_sum): # 벡터로 변환
    return np.fromiter((iter(tf_sum.values())), dtype=float, count=len(tf_sum))

def idf(inversed_index, N): # idf를 계산하는 함수
    inversed_index_vector = np.fromiter(iter(inversed_index.values()), dtype=float, count=len(inversed_index))
    return np.log(N / inversed_index_vector)

def tf_idf(corpus, category): # corpus와 category를 받아 tf-idf를 계산하는 함수
    fileids = corpus.fileids(categories=category) # 해당 카테고리에 해당하는 모든 문서들의 id
    metadata_chunk = [] # 모든 문서들의 metadata를 담을 리스트
    for fileid in fileids:
        metadata_chunk.append(produce_metadata(fileid, corpus)) # 모든 문서들에 대해 metadata 생성, metadata_chunk에 추가
    N = len(metadata_chunk) # 문서 개수
    tf_sum = {} # 각 단어들의 tf 합계가 담길 딕셔너리
    inverse_index = {} # 각 단어들의 inverse index를 담을 딕셔너리
    for metadata in metadata_chunk:
        count_vector = np.fromiter(iter(metadata.values()), dtype=float, count=len(metadata)) # 각 단어들의 빈도수만 벡터로 추출
        num_words = np.sum(count_vector) # 모든 단어들의 갯수
        for key, value in metadata.items():
            tf_sum[key] = tf_sum.get(key, 0) + value / num_words # tf summation
            inverse_index[key] = inverse_index.get(key, 0) + 1 # 단어가 발견될 때마다 inverse index 업데이트
    tf_idf_value = tf(tf_sum) * idf(inverse_index, N) # tf-idf 계산 (벡터)
    return {word: tf_idf for word, tf_idf in zip(inverse_index.keys(), tf_idf_value)} # 딕셔너리로 반환

def top_n(dictionary, n): # tf-idf 정보가 담긴 딕셔너리를 받아 상위 n개 데이터를 pandas dataframe으로 반환
    sorted_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    keys, values = list(zip(*sorted_list[:n]))
    return pd.DataFrame({'key': keys, 'value': values})




