# parse하고자 하는 html 스크립트

labinfo = str(
'<html><head></head><body>' 
'<tr class="odd views-row-first">' 
'<td class="views-field views-field-title" >' 
'<a href="/lab/3%EC%B0%A8%EC%9B%90-%EB%AA%A8%EB%8D%B8%EB%A7%81-%EB%B0%8F%EC%B2%98%EB%A6%AC-%EC%97%B0%EA%B5%AC%EC%8B%A4">3차원 모델링 및 처리 연구실</a></td>' '<td class="views-field views-field-field-faculty" >' '<a href="/professor/%EA%B9%80%EB%AA%85%EC%88%98">김명수</a></td>' '<td class="views-field views-field-field-office" >302동 315-1호<br />(02) 880-1840</td>' 
'<td class="views-field views-field-field-abbreviation" >3MAP</td></tr>'
'<tr class="odd">' 
'<td class="views-field views-field-title" >' 
'<a href="/lab/%EC%9D%B8%ED%84%B0%EB%84%B7%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%EC%97%B0%EA%B5%AC%EC%8B%A4">인터넷 데이터베이스 연구실</a></td>' 
'<td class="views-field views-field-field-faculty" >' 
'<a href="/professor/%EA%B9%80%ED%98%95%EC%A3%BC">김형주</a></td>' 
'<td class="views-field views-field-field-office" >301동 453호<br/>(02) 880-1830</td>' 
'<td class="views-field views-field-field-abbreviation" >IDB</td></tr>' 
'</body></html>'
'<tr class="even">' 
'<td class="views-field views-field-title" >' 
'<a href="/lab/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%97%B0%EA%B5%AC%EC%8B%A4">데이터베이스 시스템 연구실</a></td>' 
'<td class="views-field views-field-field-faculty" >' 
'<a href="/professor/%EB%AC%B8%EB%B4%89%EA%B8%B0">문봉기</a></td>' 
'<td class="views-field views-field-field-office" >301동 418호 / 452-2호<br />(02) 880-6575</td>' 
'<td class="views-field views-field-field-abbreviation" >DBS</td></tr>'
)