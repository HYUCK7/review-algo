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
        # artists = soup.find_all('p', {'class': 'artist'})
        # print(type(artists)) # class 'bs4.element.ResultSet
        # Resultset = Dataset, Data Structure에 담아야한다.
        # artists = [i.get_text() for i in artists]  # 배열에 담았음. 이제 타입은 리스트
        '''print(''.join([i for i in artists]))
            print('-' * 30)'''
        artists = soup.find_all('p', {'class':'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))

        titles = soup.find_all('p', {'class':'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

        self.col(soup, 'artist')
        self.col(soup, 'title')
        for i, j in enumerate(['artist', 'title']):
            print('\n'.join(i for i in [i for i in self.col(soup, i)]))
        return None

    @staticmethod
    def col(soup, a):
        cols = soup.find_all('p', {'class': a})
        cols = [i.get_text() for i in cols]
        #  print(''.join([i for i in cols]))
        return cols

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')

        artists = soup.find_all('div', {'class': 'ellipsis rank01'})
        artists = [i.get_text() for i in artists]
        artists = [i[1:-1] for i in artists]
        # print(''.join([i for i in artists]))
        print(''.join([i for i in artists]))

        print('-' * 30)

        musics = soup.find_all('div', {'class': 'ellipsis rank02'})
        musics = [i.get_text() for i in musics]
        print(''.join([i for i in musics]))
        return None

    def quiz28(self) -> str:
        a = [i if i == 0 or i == 0 else i for i in range(1)]  # a는 수열(sequence) 처리
        b = [i if i == 0 or i == 0 else i for i in []]  # 엘리먼트들이 들어간다. 객체열(자료구조)
        # 자료구조 -> 리스트, 튜플, 딕셔너리
        # 자바 -> array list, hash set, hash map
        # JS -> JSON , array
        c = [(i, j) for i, j in enumerate[0]]  #
