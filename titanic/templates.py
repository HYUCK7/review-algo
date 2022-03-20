import matplotlib.pyplot as plt
from icecream import ic
from matplotlib import rc, font_manager

from context.domain import Dataset
from context.models import Model

rc('font',
   family=font_manager.FontProperties(fname='/Users/youjaehyuck/Library/Fonts/D2Coding-Ver1.3.2-20180524-all.ttc')
   .get_name())


# 데이터 시각화 : entity(개체)를 차트로 표현하는 것.
# survived, pclass, sex, embarked의 feature 작성. 템플릿 메소드 패턴으로 구성

class TitanicTemplate:
    model = Model()
    dataset = Dataset()

    def __init__(self, fname):
        self.entity = self.model.new_model(fname)
        df = self.entity
        ic(f'트레인의 타입: {type(df)}')
        ic(f'트레인의 컬럼: {df.columns}')
        ic(f'트레인의 상위 5행: {df.head()}')
        ic(f'트레인의 하위 5행: {df.tail()}')

    # 시각화 템플릿
    def visualize(self) -> None:
        df = self.entity
        self.draw_survived(df)

    @staticmethod
    def draw_survived(df) -> None:
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        # f = 형태 fig nrows = 1, ncols = 2 , figsize(inch, inch)
        df['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0. 사망자 vs 1. 생존자')
