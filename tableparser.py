import requests
from bs4 import BeautifulSoup

class tableParser:

    def __init__(self, url):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'lxml')

    def get_table(self):
        table_dict_list = []
        for table in self.soup.find_all('table'):
            table_dict_list.append(self.parse_table(table))
        return table_dict_list

    def parse_table(self, table):

        columns = []
        value_list = []
        thead = table.find('thead')
        if thead:
            for th in thead.find_all('th'):
                columns.append(th.get_text())
                value_list.append([])
        tbody = table.find('tbody')
        column_marker = 0
        if tbody:
            for row in tbody.find_all('tr'):
                for datum in row.find_all('td'):
                    value_list[column_marker].append(datum.get_text())
                    if column_marker == len(value_list) - 1:
                        column_marker = 0
                    else:
                        column_marker += 1
        table_dict = {column: value for column, value in zip(columns, value_list)}
        return table_dict




