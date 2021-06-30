### 군집화 알고리즘 테스트를 위한 데이터 생성

사이킷런에서 다양한 유형의 군집화 알고리즘을 테스트해보기 위한 데이터 생성기

여러 개의 클래스에 해당하는 데이터세트

하나의 클래스에 여러 개의 군집이 분포될 수 있게 데이터 생성할 수 있다.

* make_blobs() : 개별 군집의 중심점, 표준 편차 제어 기능

  * n_samples : 생성할 총 데이터 개수
  * n_features : 데이터의 피처 개수
  * centers : (int) 군집의 개수, (ndarray) 개별 군집 중심점의 좌표
  * cluster_std : 생성될 군집 데이터 표준 편차 -> 군집별로 서로 다른 표준 편차 가진 데이터 세트
  * `center_box`: 생성할 클러스터의 바운딩 박스(bounding box), 디폴트 (-10.0, 10.0))
  * 반환값:
  * `X` : [n_samples, n_features] 크기의 배열
    - 독립 변수
  * `y` : [n_samples] 크기의 배열
    - 종속 변수

  ex) X, y = make_blobs(n_samples=200, n_features=2, centers=3)

  > 총 200개의 레코드, 2개의 feature, 3개의 군집화 기반 분포도를 가진 피처 데이터 세트 X와 동시에 3개의 군집화 값을 가진 타깃 데이터 세트 y 반환

  // 본문 코드 (생성 및 시각화)

  ```python
  from sklearn.datasets import make_blobs
  
  plt.title("세개의 클러스터를 가진 가상 데이터")
  X, y = make_blobs(n_samples=300, n_features=2, centers=3, random_state=1)
  plt.scatter(X[:, 0], X[:, 1], marker='o', c=y, s=100,
              edgecolor="k", linewidth=2)
  plt.xlabel("$X_1$")
  plt.ylabel("$X_2$")
  plt.show()
  ```

  ![../_images/09.02 분류용 가상 데이터 생성_23_0.png](https://datascienceschool.net/_images/09.02%20%EB%B6%84%EB%A5%98%EC%9A%A9%20%EA%B0%80%EC%83%81%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%83%9D%EC%84%B1_23_0.png)

* make_classification() : 노이즈를 포함한 데이터를 만드는 데 유용하게 사용

  - `n_samples` : 표본 데이터의 수, 디폴트 100
  - `n_features` : 독립 변수의 수, 디폴트 20
  - `n_informative` : 독립 변수 중 종속 변수와 상관 관계가 있는 성분의 수, 디폴트 2
  - `n_redundant` : 독립 변수 중 다른 독립 변수의 선형 조합으로 나타나는 성분의 수, 디폴트 2
  - `n_repeated` : 독립 변수 중 단순 중복된 성분의 수, 디폴트 0
  - `n_classes` : 종속 변수의 클래스 수, 디폴트 2
  - `n_clusters_per_class` : 클래스 당 클러스터의 수, 디폴트 2
  - `weights` : 각 클래스에 할당된 표본 수
  - `random_state` : 난수 발생 시드
  - 반환값:
  - `X` : [n_samples, n_features] 크기의 배열
    - 독립 변수
  - `y` : [n_samples] 크기의 배열
    - 종속 변수

  

  ```python
  # 두 변수 모두 클래스와 상관관계가 있는 데이터
  plt.figure(figsize=(8, 8))
  plt.title("두개의 독립변수 모두 클래스와 상관관계가 있는 가상데이터")
  X, y = make_classification(n_samples=500, n_features=2, n_informative=2, n_redundant=0,
                             n_clusters_per_class=1, random_state=6)
  plt.scatter(X[:, 0], X[:, 1], marker='o', c=y,
              s=100, edgecolor="k", linewidth=2)
  
  plt.xlim(-4, 4)
  plt.ylim(-4, 4)
  plt.xlabel("$X_1$")
  plt.ylabel("$X_2$")
  plt.show()
  ```

  ```python
  plt.subplot(121)
  sns.distplot(X[y == 0, 0], label="y=0")
  sns.distplot(X[y == 1, 0], label="y=1")
  plt.legend()
  plt.xlabel("x_1")
  plt.subplot(122)
  sns.distplot(X[y == 0, 1], label="y=0")
  sns.distplot(X[y == 1, 1], label="y=1")
  plt.legend()
  plt.xlabel("x_2")
  plt.show()
  ```

  ![../_images/09.02 분류용 가상 데이터 생성_11_0.png](https://datascienceschool.net/_images/09.02%20%EB%B6%84%EB%A5%98%EC%9A%A9%20%EA%B0%80%EC%83%81%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%83%9D%EC%84%B1_11_0.png)

  ![../_images/09.02 분류용 가상 데이터 생성_12_0.png](https://datascienceschool.net/_images/09.02%20%EB%B6%84%EB%A5%98%EC%9A%A9%20%EA%B0%80%EC%83%81%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%83%9D%EC%84%B1_12_0.png)

* make_moons() : 초승달 모양 클러스터 두 개 형상의 데이터 생성 (직선 분류 X)

* make_gaussian_quantiles() : 다차원 가우시안 표본

> https://datascienceschool.net/03%20machine%20learning/09.02%20%EB%B6%84%EB%A5%98%EC%9A%A9%20%EA%B0%80%EC%83%81%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%83%9D%EC%84%B1.html

