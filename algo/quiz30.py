import pandas as pd
from icecream import ic


class Quiz30:
    def quiz30_df_4_by_3(self):
        df = pd.DataFrame([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9],
                           [10, 11, 12]], index=range(1, 5), columns=['A', 'B', 'C'])
        # 위 식을 리스트 결합 형태로 분해해서 조립하시오
        a = []
        b = []
        c = []
        d = []
        col = [chr(i) for i in range(32, 34)]  # ['A','B','C']
        # [i, j]
        ic(df)

    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:     0   1   2
                0  97  57  52
                1  56  83  80
    '''

    def quiz31_rand_2_by_3(self) -> str:
        return None

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

    def quiz32_df_grade(self) -> str: return None
