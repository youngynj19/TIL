'''
만약 (미세먼지 농도가 150보다 크면):
    출력하자('매우나쁨')
아닌데 만약에 (미세먼지 농도가 150이하 80초과면):
    출력하자('나쁨')
아닌데 만약에 (미세먼지 농도가 80이하 30초과면):
    출력하자('보통')
아니면:
    출력하자('좋음')
'''
dust = 70

if 150 < dust:
    print('매우나쁨')
elif 170 < dust <= 180:
    print('나쁨')
elif 30 < dust and dust <= 80:
    print('보통')
else:
    print('좋음')

print(f'{dust} 따옴표로 감싸서 사용한다.')
print('{} 따옴표로 감싸서 사용한다.'.format(dust))
