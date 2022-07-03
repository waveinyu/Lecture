import requests
from bs4 import BeautifulSoup

# headers : 헤더에서 콜을 날리지만 마치 우리가 브라우저에 콜을 날린 것처럼 보이게 함
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')



#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(4) > td.number

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(4) > td.info > a.title.ellipsis

#body-content > div.newest-list > div > table > tbody > tr:nth-child(4) > td.info > a.artist.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(3) > td.info > a.artist.ellipsis

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for tr in trs:
    rank = tr.select_one('td.number').text[0:2].strip()
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    artist = tr.select_one('td.info > a.artist.ellipsis').text
    
    print(rank, title, artist)
