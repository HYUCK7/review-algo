import urllib.request
from turtle import pd

import pandas as pd

from bs4 import BeautifulSoup  # bs4 = .py (module)
from urllib.request import urlopen  # pip install urlopen, bs4, lxml


class Quiz20:

    def quiz24zip(self) -> {}:
        '''a = [i for i in self.abc(soup, 'p', 'class', 'artist')]
                a = [i for i in self.abc(soup, 'p', 'class', 'title')]
                a = self.abc(soup, 'p', 'class', 'artist')
                b = self.abc(soup, 'p', 'class', 'title')
                print(a, b)'''

        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc.read(), 'lxml')  # html.parser vs lxml
        ls1 = self.find_music(soup, 'title')
        ls2 = self.find_music(soup, 'artist')
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    def find_rang(self, soup) -> None:
        for i, j in enumerate(['artist', 'title']):
            for i, j in self.find_music(soup, j):
                print(f'{i}위 : {j}')
            print('*' * 100)

    @staticmethod
    def print_music_list(soup) -> None:
        # print(soup.prettify())
        artists = soup.find_all('p', {"class": "artist"})
        # print(type(artists)) # <class 'b24.element.ResultSet'>
        artists = ([i.get_text() for i in artists])
        # print(type(artists))
        # print(''.join(i for i in artists))
        title = soup.find_all('p', {"class": "title"})
        title = ([j.get_text() for j in title])
        print(''.join(j for j in title))

    @staticmethod
    def find_music(soup, cls_name) -> []:
        ls = soup.find_all('p', {'class': cls_name})
        return [j.get_text() for j in ls]
        # print(''.join(j for j in a))

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

    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')
        return None

    def quiz29(self):
        None
