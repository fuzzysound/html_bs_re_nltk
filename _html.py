# labinfo에 있는 html 스크립트를 파싱하여 원하는 데이터를 추출하는 과제

from html.parser import HTMLParser
from labinfo import labinfo

class MyParser(HTMLParser): # HTMLParser를 상속받는 커스텀 파서
    def __init__(self):
        super().__init__()
        self.labname = []
        self.professor = []
        self.location = []
        self.phone = []
        self.abbreviation = []
        self.info_list = [self.labname, self.professor, self.location, self.phone, self.abbreviation] # 인덱싱을 위해 한 리스트에 담음
        self.tr_flag = False # tr 태그 안에 있는지를 알려주는 flag
        self.td_num = 0 # 몇 번째 td 태그 안인지를 지정하는 변수

    def handle_starttag(self, tag, attrs):
        if tag == 'tr': # tr 태그가 시작될 경우
            self.tr_flag = True

    def handle_endtag(self, tag):
        if tag == 'tr': # tr 태그가 끝날 경우
            self.tr_flag = False
        if tag in ['td', 'br']: # td 혹은 br 태그가 끝날 경우. 추출하는 데이터는 두 태그 안에 있음.
            if self.td_num == 4:
                self.td_num = 0
            else:
                self.td_num += 1 # td_num은 0-4 사이에서 순환

    def handle_data(self, data):
        if self.tr_flag:
            self.info_list[self.td_num].append(data) # tr 태그 안에 있을 경우 데이터를 info_list 안의 알맞은 리스트에 추가

    def LabinfoDict(self):
        keys = ['labName', 'professor', 'location', 'phone', 'abbreviation']
        info_dict = {key: value for key, value in zip(keys, self.info_list)}
        return info_dict

parser = MyParser()
parser.feed(labinfo)
dic = parser.LabinfoDict()
print(dic)

