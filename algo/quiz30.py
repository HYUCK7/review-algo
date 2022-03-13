import string
from random import random

import pandas as pd
from icecream import ic

from algo.domain import myRandom


class Quiz30:
    def quiz30_df_4_by_3(self):
        # (1)
        a = []
        b = []
        c = []
        d = []
        col = [chr(i) for i in range(32, 35)]  # ['A','B','C']
        [a.append(i) if i < 4 else b.append(i) for i in range(1, 7)]
        [c.append(i) if i < 10 else d.append(i) for i in range(7, 13)]
        dict = {'1': a, '2': b, '3': c, '4': d}
        df = pd.DataFrame.from_dict(dict, orient='index', columns=col)
        ic(df)

        # (2)
        e = [[j * 3 + i for i in range(1, 4)] for j in range(4)]
        df1 = pd.DataFrame(e, index=range(1, 5), columns=col)
        ic(df1)
        # j = [1,2,3] * 3 + 1

    def quiz31_rand_2_by_3(self):
        c = [i for i in range(0, 3)]  # 0 , 1,  2
        # (1)
        # myRandom()
        # [a.append(myRandom(10,100)) for i in range(3)]
        # [b.append(myRandom(10,100)) for i in range(3)]

        # [a.append(myRandom(10, 100)) if i < 3 else b.append(myRandom(10, 100)) for i in range(6)]
        # dict = {'0': a, '1': b}
        # df = pd.DataFrame.from_dict(dict, orient='index', columns=c)
        # ic(df)

        # (2)
        e = [[myRandom(10, 100) for i in range(3)] for j in range(2)]
        df1 = pd.DataFrame(e, index=range(0, 2), columns=c)
        ic(df1)

    def quiz32_df_grade(self):
        sub = ['kor', 'eng', 'math', 'soc']
        arr2 = [''.join([string.ascii_letters[myRandom(0, 52)] for i in range(5)]) for i in range(10)]
        grade = [[myRandom(0, 100) for i in range(4)] for j in range(10)]
        df = pd.DataFrame(grade, index=arr2, columns=sub)
        ic(df)

        ''' id_make = [[''.join(string.ascii_uppercase)[myRandom(0, 26)] for i in range(5)] for i in range(10)]
                # sub = ['국어', '영어', '수학', '사회']
                # grade = [[myRandom(0, 100) for i in range(4)] for j in range(10)]
                # df2 = pd.DataFrame(grade, index=id_make, columns=sub)
                # ic(df2)'''
        '''id_make = random.()string.ascii_uppercase
        #print(id_make)
        #id = random.choice(id_make)
        # [''.join() for i in range]
        #print(id)'''
