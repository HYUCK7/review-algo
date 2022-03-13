import string
from random import random

import pandas as pd
from icecream import ic

from algo.domain import myRandom


class Quiz30:
    def quiz30_df_4_by_3(self):

        df = pd.DataFrame([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9],
                           [10, 11, 12]], index=range(1, 5), columns=['A', 'B', 'C'])
        # 위 식을 리스트 결합 형태로 분해해서 조립하시오
        #(1)
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

    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:     0   1   2
                0  97  57  52
                1  56  83  80
    '''

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
        e = [[myRandom(10,100) for i in range(3)] for j in range(2)]
        df1 = pd.DataFrame(e, index=range(0,2), columns=c)
        ic(df1)

    '''
            데이터프레임 문제 Q04.
            국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
             단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

              ic| df4:        국어  영어  수학  사회
                        lDZid  57  90  55  24
                        Rnvtg  12  66  43  11
                        ljfJt  80  33  89  10
                        ZJaje  31  28  37  34
                        OnhcI  15  28  89  19
                        claDN  69  41  66  74
                        LYawb  65  16  13  20
                        QDBCw  44  32   8  29
                        PZOTP  94  78  79  96
                        GOJKU  62  17  75  49
    '''

    def quiz32_df_grade(self):
        id_make = string.ascii_uppercase
        id = random.choice(id_make)
        ic(id)
        '''id_make = random.()string.ascii_uppercase
        #print(id_make)
        #id = random.choice(id_make)
        # [''.join() for i in range]
        #print(id)'''
