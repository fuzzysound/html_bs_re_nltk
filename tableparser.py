# html 스크립트에서 테이블을 파싱하는 클래스 tableParser

import requests
from bs4 import BeautifulSoup

class tableParser:

    def __init__(self, url):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'lxml')

    def get_table(self): # 딕셔너리로 변환된 테이블들의 리스트를 반환하는 method
        table_dict_list = []
        for table in self.soup.find_all('table'):
            table_dict_list.append(self.parse_table(table))
        return table_dict_list

    def parse_table(self, table): # soup object를 받아 테이블을 딕셔너리로 변환하는 method

        columns = [] # 테이블의 column 이름을 담을 리스트
        value_list = [] # 테이블의 각 column에 해당하는 값들의 리스트를 담을 리스트
        thead = table.find('thead') # thead 태그 안의 모든 스크립트
        if thead:
            for th in thead.find_all('th'):
                columns.append(th.get_text()) # column 이름 저장
                value_list.append([]) # column 한 개가 추가될 때마다 value_list 안에 빈 리스트 하나를 추가
        tbody = table.find('tbody') # tbody 태그 안의 모든 스크립트
        column_marker = 0 # 현재 몇 번째 column의 데이터를 추출해야 하는지 알려주는 마커
        if tbody:
            for row in tbody.find_all('tr'):
                for datum in row.find_all('td'):
                    value_list[column_marker].append(datum.get_text()) # 해당 column의 데이터를 value_list 안의 알맞은 리스트에 추가
                    if column_marker == len(value_list) - 1:
                        column_marker = 0
                    else:
                        column_marker += 1 # column_marker는 0-len(column) 사이에서 순환
        table_dict = {column: value for column, value in zip(columns, value_list)} # 딕셔너리로 변환
        return table_dict




