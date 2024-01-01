"""
1. Numpy dot/matmul 함수의 차이
 - 행렬을 곱하기 위한 연산이라는 점에서 비슷하지만, 3차원 이상의 행렬에서는 차이가 있다.
   matmul 함수는 각각 마지막 2개의 축으로 이루어진 행렬을 나머지 축에 따라 쌓아놓은 것이라고 생각하고 곱셈을 수행한다.
   반면 Numpy dot 함수는 첫 번째 배열의 마지막 축과 두 번째 배열의 마지막 축에 대한 곱의 합으로 곱셈을 수행한다.
   예를 들어 shape이 (2,3,3)인 서로 다른 a,b 두 행렬이 있을 때, numpy.dot(a,b) 함수의 결과는 그대로 (2,3,3)의 shape을 가지지만
   numpy.matmul(a,b) 함수의 결과는 shape이 (2,3,2,3)인 행렬이 된다.

2. One hot encoding
 - 분류되는 클래스 중 원래 라벨을 1, 그 외의 값은 모두 0으로 구별하는 인코딩이다. 

3. GD
 - 최적의 파라미터를 찾기 위해서는 로스 함수가 최소가 되는 부분을 찾아야 한다. 하지만 일반적인 로스 함수는 매우 복잡하고, 
   파라미터 공간이 너무 커서 최솟값을 짐작할 수 없다. 이때 기울기가 음인 상태를 계속 추적해 나가면 최솟값이 되는 부분을 찾을 수 있고, 
   이를 이용하는 방법을 경사 하강법이라고 한다.

4. train, test, validation data 차이
 - train data는 매개변수 (가중치와 편향)의 학습에 이용한다.
   validation data는 하이퍼파라미터의 성능을 평가하는데 이용한다. 
   test data는 범용 성능을 확인하기 위해 마지막으로 사용한다.
   따라서 train data는 학습에 직접적으로 이용되는 만큼 전체 데이터셋에서 가장 많은 비중을 차지한다.
   반면 validation data 없이 test data 만 존재하면 하이퍼파라미터의 성능을 평가할 때 test data를 이용하게되고, 
   test data에 오버피팅되는 문제가 있기 때문에 모델의 일반화를 증가시키기 위해 test data과 분리된 validation data를 따로 분리하여 학습한다.

5. cnn 기본 구조 설명, 이미지 분류 성능을 높이기 위해 수행할 수 있는 일
 - 컨볼루션 계층, ReLU 활성화 함수, 풀링 계층을 반복해서 연산하고, 마지막으로 완전 연결 계층을 두고 결과를 softmax 로 나타내는 네트워크. 
   이미지 분류에서 일반화 성능을 높이기 위해 배치 노멀리제이션, 드롭아웃, 활성화 함수 변경, 컨볼루션 계층을 더 깊게 쌓기 등 다양한 방법을 수행할 수 있다.

6. RNN의 기본 구조와 동작설명
 - 보통 신경망은 입력층에서부터 출력층 방향으로만 학습이 진행되지만, 순환 신경망의 경우 활성화 함수를 통해 나온 결과값을 출력층 방향과 다시 은닉층 노드에 입력하여 순환하는 방향이 있다. 
   활성화 함수로는 하이퍼볼릭탄젠트 함수를 사용한다. 주로 음성이나 문장, 연속적인 수치 데이터와 같은 시퀀스 데이터에서 많이 사용한다. 
   단, 시점이 길어질수록 앞의 정보가 뒤로 충분히 전달되지 못하는 현상이 발생해 비교적 짧은 시퀀스에서만 효과를 보이는 단점이 존재한다.
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, models
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# 7. MNIST 데이터셋의 데이터를 0~1 사이의 실수로 정규화하는 코드
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0


# 8. CNN MNIST 분류 작업 예제를 텐서플로우로 작성하고 설명
x_train = x_train.reshape((60000, 28, 28, 1))
x_test = x_test.reshape((10000, 28, 28, 1))

model = models.Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.summary()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test,  y_test, verbose=2)
