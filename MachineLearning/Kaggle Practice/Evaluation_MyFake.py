from sklearn.base import BaseEstimator
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits

class MyFakeClassifier(BaseEstimator):
    def fit(self, x, y):
        pass

    # 입력값으로 들어오는 x 데이터 세트의 크기만큼 모두 0값으로 만들어 반환
    def predict(self, x):
        return np.zeros((len(x), 1), dtype=bool)

digits = load_digits()

# digits 번호가 7번이면 True, 이를 astype(int)로 1로 변환, 7번이 아니면 False이고 0으로 변환
y = (digits.target == 7).astype(int)
x_train, x_test, y_train, y_test = train_test_split(digits.data, y, random_state=11)

print('레이블 테스트 세트 크기:', y_test.shape)
print('테스트 세트 레이블 0과 1의 분포도')
print(pd.Series(y_test).value_counts())

fakeclf = MyFakeClassifier()
fakeclf.fit(x_train, y_train)
fakepred = fakeclf.predict(x_test)
print('모든 예측을 0으로 하여도 정확도는:{:.3f}'.format(accuracy_score(y_test, fakepred)))