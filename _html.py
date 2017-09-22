from html.parser import HTMLParser
from labinfo import labinfo

class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.labname = []
        self.professor = []
        self.location = []
        self.phone = []
        self.abbreviation = []
        self.info_list = [self.labname, self.professor, self.location, self.phone, self.abbreviation]
        self.tr_flag = False
        self.td_num = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.tr_flag = True

    def handle_endtag(self, tag):
        if tag == 'tr':
            self.tr_flag = False
        if tag in ['td', 'br']:
            if self.td_num == 4:
                self.td_num = 0
            else:
                self.td_num += 1

    def handle_data(self, data):
        if self.tr_flag:
            self.info_list[self.td_num].append(data)

    def LabinfoDict(self):
        keys = ['labName', 'professor', 'location', 'phone', 'abbreviation']
        info_dict = {key: value for key, value in zip(keys, self.info_list)}
        return info_dict

parser = MyParser()
parser.feed(labinfo)
dic = parser.LabinfoDict()
print(dic)

