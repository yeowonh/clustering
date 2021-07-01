## 평균 이동
군집의 중심으로 지속적으로 움직이면서 군집화를 수행한다는 점에서 k-means와 유사

- k-means는 중심에 소속된 **데이터의 평균 거리**를 중심으로 이동
- 평균이동은 중심을 **밀도가 가장 높은 곳**으로 이동

![img](https://lh5.googleusercontent.com/8U5PIAJwYgljbNf3AGDsLuQItnUmh1PfX1VnxaWJWlI9AsT3p7Jep8yuyT8JDCHp3IYRPBfvkZ0caBGKHeGHpvM3ozqyUpsoRax6_uVGN2OHYwoEmqHOV7Yjsz0DJR4IaFn1U_C3)

군집 중심은 밀도가 높을 것이라 생각해 확률 밀도 함수(PDF)를 도입해 확률 밀도함수의 값이 가장 큰 곳을 군집 중심으로 선정

확률 밀도 함수를 추정하는 방법으로 **KDE 커널 함수**를 사용한다.

### 커널 함수
원점을 중심으로 대칭이며 적분 값이 1인 non-negative 함수

#### 커널 함수의 특징
* $$\int_{-\infty}^{\infty}K(u)du=1$$
* $$K(u)>=0$$

대표적으로 정규분포가 사용된다.

![img](https://lh3.googleusercontent.com/1YH2WNgEOEnWMvnY0-hChvy6EmMuOa4s9JDmh9Dz7NmEbKUF3aYPWLCiaYZc3HQqlCEMffl1MHHm73ZQ6QIgUfx9s2Mmjny9mr9rpjK_Sdx2BZLtVYULVAYiWW1Pn1qzi5GueG95)

![img](https://lh6.googleusercontent.com/DfCbVhgb-VqcSpD8n8eEwLM6wqRRl7qPKtHV8XNnpUrH1OpuBIBmURSLwG2MCSPJIMij5eQ8AtB2fW9C1wFrKwmDbS2w8ooEkOBZNX22h1ONLIidZrO8S_9g0n3I9MiLXcAUbXsO)

$$KDE = \frac{1}{n}\sum_{i=1}^{n}K_h(x-x_i) = \frac{1}{nh}\sum_{i=1}^{n}K(\frac{x-x_i}{h})$$

* k : 커널 함수

* x : 확률 변수 값

* xi : 관측값

* h : 대역폭

  -> 각 데이터를 중심으로 커널 함수를 형성하고 이를 데이터 수로 나눔
  
  $$p(x) = \frac{1}{N}\sum_{n=1}^{N}\frac{1}{{2\pi h^2}^{D/2}}exp\{-\frac{||x-x_n||^2}{2h^2}\}$$
  
  가우시안을 적용한 커널함수 하나의 샘플 xn에 대해 중심(평균)이 xn이고 표준편차가 h인 가우시안 분포를 만들고 
  
  이를 합해 새로운 밀도 함수 형성, 정규화를 위해 n으로 나눔  
  
  h는 KDE 형태를 부드러운 형태로 평활화(Smoothing)하는 데 적용되며, 이 h를 어떻게 설정하느냐에 따라 확률 밀도 추정 성능이 크게 좌우
  
  
  ![img](https://lh5.googleusercontent.com/IH7ihH6C1kTsIHsjdBtXpTVGpJtadVaKnh4xi1sq2S-hRBc6wSk6KfHlk8d0euP_txOeH8B50tqNSmlrNpa2ATwHoNByxCiz-M52hcPtuWhJ6pRXQVsKLeZWHyhvtbhN03UkQ2TT)
  > 왼쪽위부터 오른쪽 아래까지 h= 1, 2.5, 5, 10 
  -> h의 증가에 따른 KDE 형태 변화


* h가 작을 경우 각 데이터가 가지는 가우시안 분포도 분산이 작아 좁고 뾰족한 KDE 형태. 변동성이 큰 방식으로 확률 밀도 함수를 추정하므로 과적합(over-fitting)하기 쉬움.
* h가 클 경우각 데이터가 가지는 가우시안 분포도 분산이 커서 크고 완만한 KDE 형태. 과도하게 smoothing 된 KDE로 인해 지나치게 단순화된 방식으로 확률 밀도 함수를 추정해 과소적합(under-fitting)하기 쉬움.

=> 적절한 KDE의 대역폭 h를 계산하는 것은 KDE 기반의 평균 이동(Mean Shift) 군집화에서 매우 중요
 
 대역폭 크기 설정이 군집화의 품질에 큰 영향을 미치기 때문에 사이킷런에서는 최적의 대역폭 계산을 위한 함수(estimate_bandwidth()) 제공
 
 
 * 장점
 
   * dataset의 형태를 특정형태나 특정 분포도 기반의 모델로 가정하지 않음 => 좀 더 유연한 군집화 가능
   * 이상치의 영향력이 크지 않음
   * 미리 군집의 개수를 정할 필요가 없음

* 단점

  * 알고리즘의 수행 시간이 오래 걸림
  * bandwidth의 크기에 따른 군집화 영향도가 매우 큼

  => 분석 업무 기반의 dataset보다는 컴퓨터 비전 영역에서 많이 사용됨(이미지&영상 데이터에서의 개체 구분/움직임 추적)

