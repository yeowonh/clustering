[sklearn.cluster.DBSCAN](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)

원형 군집이 아닌 경우 잘 동작하지 않으며, 군집 개수를 사용자가 지정해야 한다는 KMeans의 단점 극복

개념 : 밀도 기반 군집화의 대표적인 알고리즘 -> 특정 공간에 충분한 밀도를 갖추었느냐에 따라 군집화

- eps-neighbors : 개별 데이터 반경으로 입실론 반경의 원 영역 (입실론 up -> 포함하는 데이터 up, 입실론 down -> 포함하는 데이터 down)

- Minimum points : 개별 데이터의 입실론 반경안의 데이터들이 군집을 이룰 수 있는 최소 수 (사이킷런 라이브러리는 자신 포함) 

  ε 최소 거리안의 이웃 영역 안에 최소 데이터 개수 이상의 데이터가 있으면 그 데이터는 핵심(core) 데이터다. 
  이렇게 핵심 데이터를 찾아낸 다음에는 이 핵심 데이터의 이웃 영역 안에 있는 데이터를 이 핵심 데이터와 연결된 핵심 데이터로 정의한다. 
  핵심 데이터의 이웃영역안에 있는 데이터도 마찬가지로 연결된 핵심 데이터가 된다. 
  만약 고밀도 데이터에 더이상 이웃이 없으면 이 데이터는 경계(border) 데이터라고 한다. 
  핵심 데이터도 아니고 경계 데이터도 아닌 데이터를 outlier라고 한다.
  
  ![img](https://lh5.googleusercontent.com/91s5YOj9wcWElgNN_iu7uxw10G8rfz9ewV85wuHTPtZYq89BgKavIG8jlpvdhVD-9ZRVGsJ6daGfeE7aE02gdA6v82S1YR2A0cUW-DbTD_geHWvxbub9T3DAuLto0Vc92SwEiu_3)
  ![img](https://lh5.googleusercontent.com/_K9JtbqtXefsTN03wu0Nke9dW_JdhAFYyx9jPkYpAJT2BbjUIDpGHRXApfrtWZFUaVAUWLE91QKILlOZ17RheCUrEBw0mspfYc7kn7OaLedZTfWflVlmB20psS_g5RJHtur7hKh5)
  ![img](https://lh5.googleusercontent.com/1dfq0LkSOtpAinbh41OjJjrDDYAk4-euHXzk3NsH4Cx6IXYQri1_YXBBxUeNHW3WlWoMod_IxeeqaVFApNdiv2jEmJ15eCtwnmZKyL6e7TZ8T9kRC3UmvfqTAb20Z6rT40d-7gZ0)
  ![img](https://lh4.googleusercontent.com/Q0oxhEYmILwFsQmTU_e_O2J6h0iOTIEMAdwR7uhdc8TiGGid4YwkNj70rY8g8sik6UjaP0ef0Y_Kl4mscy7XdoqyQtGoi3hobxHfhhY0JQRseL9z6GlNjb3WJfu71ez5ffhn6et9)
  ![img](https://lh6.googleusercontent.com/90_2zCCbEg2LkG_85nrkQKH0H_b8OFhqhs-xO0-CM5U2738xvO2eiAGGem2eRCprvoMnGkZpkDEXrOP5Lv4d2Vl2jYY5e3WYyJjAeiY1t_f8U1sOrS9NSrxKA2xdBOneisrfHdsQ)
  ![img](https://lh5.googleusercontent.com/_kSm4poIi3D3kHG8CkM7CW-xDF15MG-Bz5eOW6ANSbrBraYKwk84j-pm05b04S8AToPBiQKwJuCB02FqpfmCGNaTg3tcz0sgR2mq2Om0j5mvW7h4W5uCzeuywEL9bqik7Nj1CF0s)
  ![img](https://lh5.googleusercontent.com/ZtfsNnICE80P2LJJyjvxQfXWdpdg4dtJlsOpk5DvBKAkXP3B3fbH-MlOxO-Bl4U69jz8_TLI7C4qkC8YP1vUGzNmyrJPC5MIIvKJaablRUiw1oaXYGg6KV04I506TwgHKAEAOi4P)
  > 6, 8번이 경계 포인트

  ![img](https://lh5.googleusercontent.com/aePIAcLuaNas1I5IwSBI2RHeTTIBox1p33VICRovfiu0MG7slgACCNf9QurSKCrfnjDxM2CwlkA_0LACFKc6PZDIaeoIgwxf64akVnL-zRtB0SpIRBnBGLEkH7Maut-lUonoVsBx)

Outlier(=잡음 포인트) : 반경 안의 데이터가 부족해 군집을 이루지도 못하고 핵심 포인트와 이웃하지도 못하는 데이터

![img](https://lh3.googleusercontent.com/x4V5VNhYH8Qp0vFA1oYa6JNc3_pFkLe4IeGyLLzav0tHgbSylrSV9DyZGl2q-hcuPm7fZOh9iy6mAb6EkpoYydeCfX0lUl5KUMV1_1JJHRo69gw3UruVlTXIzsTAMlfT2sub_7Pg)

> 군집의 크기가 다른 dataset, 볼록한 모양이 아닌(non-convex) dataset, 모양이 각기 다르고 noise가 있는 dataset에서 유용하게 쓰인다.

=> 밀도에 따라 군집들이 통합되어 가는 것이기 때문에 군집의 모양, 크기는 고려하지 않기 때문

![img](https://lh5.googleusercontent.com/GzpV58ErclRO6pVCHPUkvTSLJ2hGVu1P0qhIYtKer9L0G6b0YgBKmLSp2PcmzraLl__cY6GXcuKHzmj62YaJb1wXL-h3k2a0T116KFFdLhrCAmzXLuB4hIChusB1QV1gG35SCigh)
> 3차원에서의 dbscan

* 장점
  * 군집의 개수를 정해줄 필요 없음 -> 다양한 모양의 군집 형성
  * noise를 구분해 버림 -> 이상치 판단에 사용되기도 함
  * 계산량이 적어서 빠름

* 단점
  * 특정 군집 개수를 원할 경우 거리와 최소 개수를 조정하며 찾아야 함
  * eps 크기에 따른 성능 차이가 큼
  * 군집별로 밀도가 다른 경우 군집화가 제대로 이루어지지 않음
  * 산재되어 있는 데이터라면 제대로 군집화 할 수 없음.



