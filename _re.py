import re

string_1 = "Earth is the third planet from the Sun"
result_1 = re.match(r'\w+ \w+', string_1).group()
print(result_1)

string_2 = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'
result_2 = list(zip(*re.findall(r'(@)([\w.]+)', string_2)))[1]
print(result_2)

string_3 = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
result_3 = re.findall(r'\d{2}-\d{2}-\d{4}', string_3)
print(result_3)

string_4 = "Earth's gravity interacts with other objects in space, especially the Sun and the Moon."
result_4 = [word for word in re.split("[ ']", string_4) if re.match(r'[AEIOUaeiou][\w]+', word)]
print(result_4)

lst = ['010-256-1354', '010-1234-5576', '070-642-0384', '010-290*-4858', '0105734123']
result_5 = ['yes' if re.match(r'010-\d{3,4}?-\d{4}', number) else 'no' for number in lst]
print(result_5)