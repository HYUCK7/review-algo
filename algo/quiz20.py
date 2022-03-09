import urllib.request

from bs4 import BeautifulSoup  # bs4 = .py (module)
from urllib.request import urlopen  # pip install urlopen, bs4, lxml


class Quiz20:
    @property
    def quiz24zip(self) -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser vs lxml ( string 값으로 바꿔준다 html을)
        # print(soup.prettify()) #( ) = 호출
        '''artist = soup.find_all('p')
        for i in artist:
            print(i.get_text())'''

        artists = soup.find_all('p', {'class': 'artist'})
        # print(type(artists)) # class 'bs4.element.ResultSet
        # Resultset = Dataset, Data Structure에 담아야한다.
        artists = [i.get_text() for i in artists]  # 배열에 담았음. 이제 타입은 리스트
        print(''.join([i for i in artists]))
        return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')

        artists = soup.find_all('div', {'class': 'ellipsis rank01'})
        artists = [i.get_text() for i in artists]
        artists = [i[1:-1] for i in artists]
        #print(''.join([i for i in artists]))
        print(''.join([i for i in artists]))


        print('-'*30)

        musics = soup.find_all('div', {'class': 'ellipsis rank02'})
        musics = [i.get_text() for i in musics]
        print(''.join([i for i in musics]))
        return None
