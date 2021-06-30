## 계층 군집 알고리즘 (=hierarchical clustering)

![img](https://lh5.googleusercontent.com/2zFGIo-hZPHfplqYj5DLn-xVhei_Zz9rV_q0AAp1PqOX6jMJDPSUulpv2ZDLvtnGtI7l_d23RHjJpaC_9SpaoPzb-0DsQ4_CApBuLarZUd0JpoAdAWMFVV_gy-cViAaFtPce4Gip)

> https://www.kdnuggets.com/2019/09/hierarchical-clustering.html



여러개의 군집 중에서 가장 유사도가 높은 혹은 거리가 가까운 군집 두 개를 선택하여 하나로 합치면서 군집 개수를 줄여 가는 방법

처음에는 모든 군집이 하나의 데이터만을 가지고, 따라서 데이터 개수만큼 군집이 존재하지만 군집을 합치며 최종적으로 하나의 군집만 남게 됨

계층적 군집화를 위해서는 모든 군집간의 거리를 측정해야 함





### 거리 측정법

> 군집 u가 군집 s와 군집 t가 결합하여 생겼다고 가정



* 비계층적 거리 측정법

  계층적 군집화가 아니더라도 모든 경우에 사용 가능한 거리 측정 방법계층적 거리측정법에 비해 계산량이 많음 

  ex) 중심거리, 단일거리, 완전거리, 평균거리

  

  * 중심거리

    군집의 중심점 -> 그 클래스에 포함된 모든 데이터의 평균 사용

    
    $$
    c_u = \frac{1}{|u|}\sum_{i}u_i
    $$
    두 군집의 중심점(centroid)를 정의한 다음 두 중심점의 거리를 군집간의 거리로 정의
    $$
    d(u,v) = ||c_u-c_v||_2
    $$
    

  * 단일거리(=최소거리 방법)

    군집 u의 모든 데이터 ui와 군집 v의 모든 데이터 vj의 모든 조합에 대해 데이터 사이의 거리 d(ui, vj) 측정해 가장 작은 값 구함
    $$
    d(u,v) = min(d(u_i, v_j))
    $$
    

  * 완전거리(=최장거리 방법)

    군집 u의 모든 데이터 ui와 군집 v의 모든 데이터 vj의 모든 조합에 대해 데이터 사이의 거리 d(ui, vj) 측정해 가장 큰 값 구함
    $$
    d(u,v) = max(d(u_i, v_j))
    $$
    

  * 평균거리

    군집 u의 모든 데이터 ui와 군집 v의 모든 데이터 vj의 모든 조합에 대해 데이터 사이의 거리 d(ui, vj) 측정해 평균 구함

    
    $$
    d(u,v) = \sum_{i,j}\frac{d(u_i, v_j)}{|u||v|}
    $$
    

* 계층적 거리 측정법

  계층적 군집화에서만 사용 가능 

  => 이미 어떤 두 개의 군집이 하나로 합쳐진 적이 있다고 가정비계층적 거리 측정법에 비해 계산량이 적어 효율적

  * 중앙값 거리

    중심거리 방법의 변형

    군집 u의 중심점은 새로 계산하지 않고 원래 군집의 **두 군집의 중심점의 평균**을 사용따라서 해당 군집의 모든 데이터를 평균하여 중심점을 구하는 것 보다 계산이 빠름
    $$
    C_u = \frac{1}{2}(c_s+c_t)
    $$
    위 수식을 바탕으로 산출된 군집의 중심점으로 군집간의 거리 계산

    

  * 가중 거리

    이 군집 u와 다른 군집 v 사이의 거리는 군집 u를 구성하는 **원래 군집 s, t와 v 사이의 두 거리의 평균**을 사용

    ![../_images/16.04 계층적 군집화_15_0.png](https://lh6.googleusercontent.com/09taOHg6a7t7BY_d8S2ZoAVZxHFE57egRpO-uiPdZpgnalcRoBK0sb6TsVSAUvUMAipz2PbhgwC9rTnjgZwCYM6if_CjW2gIC1MVfTQDQvGZxKwxcXNwqcRgaHLZTdy8P53MLAas)

    
    $$
    d(u, v) = \frac{1}{2}(d(s,v)+d(t,v))
    $$
    

  * 와드 거리

    와드거리는 가중거리방법의 변형

    이 군집 u와 다른 군집 v 사이의 거리를 구하는데 있어서 군집 u를 구성하는 원래 군집 s, t와 v 사이의 거리를 사용하는 것은 가중거리 방법과 같지만 원래의 두 군집 s, t가 너무 가까우면 v와의 거리가 더 먼 것으로 인식
    ![../_images/16.04 계층적 군집화_17_0.png](https://lh5.googleusercontent.com/3qtejyur_oeXdLZVrYar_3jQjsUtwuAmBqKByR3mmlPCf6ZcvbMDdyqk4agLnwyVPvUsoAH_qT0lXiFVgzbEVG6eSv7AaKVtLwpUiHTUfvPtmavkXDa_ZK_c0W7RAhR4lIrGuOxC)


$$
d(u, v) = \sqrt{\frac{|v|+|s|}{|v|+|s|+|t|}d(v,s)^2 + \frac{|v|+|s|}{|v|+|s|+|t|}d(v,t)^2 -  \frac{|v|}{|v|+|s|+|t|}d(s,t)^2}
$$


### **dendrogram**을 통한 시각화

각 단계에서 관측치의 군집화를 통해 형성된 그룹과 이들의 유사성 수준을 표시하는 트리 다이어그램 => 각 단계에서 군집이 어떻게 형성되는지 확인하고 형성된 군집의 유사성(또는 거리) 수준을 평가 가능

![img](https://support.minitab.com/ko-kr/minitab/18/cluster_obs_dendrogram_with_final_partition_glove_testers.png)

> 덴드로그램을 높게 커팅할 수록 최종 군집수와 유사성 감소
>
> 낮게 커팅하면 최종 군집수와 유사성 증가





### 병합 군집(=Agglomerative hierarchical clustering)

시작할 때 각 포인트를 하나의 클러스터로 지정하고, 그다음 종료 조건을 만족할 때까지 가장 비슷한 두 클러스터를 합침 (bottom-up)

![img](https://lh6.googleusercontent.com/i3XvjhXTwLyMVh7g_N1EGM-pMF2vTIcz8kaGglpuOOnAl7rseKBUjCZt3XCinvgEoxWg9Oztx9bVdkk1rqUSP46fFVlYFsqM-Ny46lyARe_dzEDoizJUS1N_EnL-TqUz6Bak3yZc)

![img](https://lh3.googleusercontent.com/ZjcFMQkO8VXTCMIt_Rs7exz5UiXnthldd9Szj1tbsdFNK-elNS_sGH65BoFqWViQSCB577ZhX6q8LJTCfQqcIFEM3lCWfCaZ105DnR7rdno5BXv5V4EttQuJoUsllO9bRlKEA_X-)



* 종료조건 : 클러스터 개수
* linkage : 가장 비슷한 클러스터를 측정하는 방법
  * ward (default) : 모든 클러스터 내의 분산을 가장 작게 증가시키는 두 클러스터를 합침
  * average : 클러스터 포인트 사이 평균 거리가 가장 짧은 두 클러스터를 합침
  * complete : 클러스터 포인트 사이 최대거리가 가장 짧은 두 클러스터를 합침



클러스터에 속한 포인트 수가 많이 차이날때에는 average, complete linkage를 사용한다고 한다.

```python
import mglearn
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

#mglearn 통한 시각화
mglearn.plots.plot_agglomerative_algorithm()
plt.show()
```

> https://woolulu.tistory.com/48



![img](https://lh6.googleusercontent.com/T-Z9hmiYV9qVNzEZAN-Os4fO0XDC8GHO-7bkp3nYM9gzbqK_FnvvNNYcVn9txaqfGcRxl_mQlQowSojKKiCoXldiZLbcyCSykXItJMxD56Wp_W4_ap-s0YndDiu86ZDvo4kYromi)



single linkage: **그룹 내의 점**과 euclidean **최소 거리가 가장 작은** data를 같은 그룹으로 묶음![img](https://lh5.googleusercontent.com/SMd6IeOLgT-orJw1upY2yMIhewQZrTrefh2UXOF7GDl_rODkkuhxnwKTvtVC7DhaOFd8kZSHzVAs-dDWM46liLqRSdPg-4Icug2HoT8rwu9u46_gEXLxu6yzEWfUVG-TqrQPoig6)
![img](https://lh4.googleusercontent.com/92LTOuuJJC-Nd2lAPcG0QfHHM9SQy-QmUtopRNxGowbfTtU2Un9mDUXZlGzhsEpRWZuDv0k8xZqOefHr9ofHJ61M8zLn6U5tS7PpIVPyLX4AWhgHJhvrn-nUaNHergkqtfPfwNOH)![img](https://lh6.googleusercontent.com/i3lFBf-WWqJ24JJxSdLWGVD2DwhUcl6crPA87CWDAX_oDFokB6G377QGUNZzgBxJGyatca5V55Rl8R3DOBpDJHzv4lFlA_ZsHmwVIJWUTJDo5OdYCEzmsI0n7IEQhJa3cqPy9UpM)![img](https://lh3.googleusercontent.com/vh8iw4BM48NrJv4pIhiz3FDJ9RyPTI71dhEcKseUBDgk4ODwctB64jnBZZMQmSNdZ7FT_fBzhfl3XKBxXdyCWgaYuiPsqK7zvj_UMxkbzFao6QAjjglT-YtNjU0uPTFcQKJ-xv-x)





complete linkage: **그룹 내의 점**과 euclidean **최대 거리가 가장 작은** data를 같은 그룹으로 묶음
![img](https://lh4.googleusercontent.com/_cIXTnPUZpVx3iQ5rOgC0M7dGiGZpVeWI_ARdNVeV03W9vS8iUKH3OIlVWeaXoOuHHuFVQU4ps1WiBpKyNvoI-1gqOh5LOBasI0_pRrLLak-hCGSCTU1IEDZ1_KK2oqiA0tcECWh)![img](https://lh6.googleusercontent.com/0SMreh0vUOKq2HOgYeuO-jmFEDhFpSG90eFNDSzR8rO3La2KUhHBXxG0d0KUijmA233JgS6quzgN-BVlpMvavl4ECpEXwRFY3j4lBPptYxSYx0NsBBQ-m0UYY9rZis_uqUkYOrfM)![img](https://lh4.googleusercontent.com/MMqUQiegfbP8iuqhKcD9GoCpYcDnwC_Yw6RE6MsCfkZuE-TMnUql1mQU-FmRHVOwJKXAJ73vojROHYdxe89ugBJqGXQyb3EbaH6syrSiB3H-jOyw8WQaLPkyeK04qrlwoh41LM_T)![img](https://lh4.googleusercontent.com/ZXWbEhH1j9PJGDDbXvkfe0sLXIVMc6q1yHcQPbkd_KZMalUmV-rOqhge6h-VBN7_JOu0rSmYM554bIVKGuEJCq381K9siacv4Nu-pwriNmZUYN7SHJmcWUELg619U0KQNyOgdqzE)


group average : 그룹내의 점과의 거리의 평균이 가장 작은 data를 같은 그룹으로 묶음![img](https://lh6.googleusercontent.com/FMatEO0E9ipsAq0jGr9WLKTgKAo66Jn60QyWTbASxatBWy-1g5tm5hjehMNGSuLPDbUQ3m70kYybImU4D8KcZO9AonKCeXLXFx6lexC5RP4FFZ04-xHdw3s6SQT6-VaLKSvYGebq)![img](https://lh6.googleusercontent.com/wWxyc7aiZz1Vu-LsnASXw9oplMkYUGtpQWmg0Cyw5hno9HW0FXTHIsm7gGjModc0lzjj8xWUfTUeJY42Rdyoc4hkRoAHS2WfEBgl8Ui6paUPZLhlTiYGSqnCtbxWGWPw0b6Orjwv)![img](https://lh3.googleusercontent.com/1qzhzBM__0YSlcOCF-z9id1RVIG73IlS70UMsybc3vn3oZPwuwVhhCB3CJQQBAhvFE2DhHCM6kngk57-85zExVb0v-dyaVCKWvwAxGeYV1yZ944WAo0ngx1W2K2oIXHHwHOltj_3)![img](https://lh6.googleusercontent.com/K-JWcafBCCemG3jl5LvqcbBPG5-iEZbqt_3_5BAlFIh-ibneXgfwyOdJFgxMdaVNPkOdlvp0L6S-Y6tYCk-mDmYqD5-NNaH30qVXg8UMo3Iw21o1aFAQI4uldsFZSQQs8KoNXGJl)![img](https://lh4.googleusercontent.com/c0OVDvOP_Cg0mHI6vg5xNGdtztDqH8QUwuvy_3oXw8z2Eq15lx_3fyyodBX5FQmnPmrGTXLC8F8QQdknqk586ekTVrswWh3YNGa43ABISvOZkLqfjQzmRFLe2XvJlQ5VVbgvyu0R)



### 분할 군집 (=divisive hierarchical clustering)

전체 데이터를 하나의 클러스터로 묶고 n개의 집단으로 분리 (Top-down)

하나의 군집에서 → n개의 집단으로 분리

![img](https://lh5.googleusercontent.com/0phtE2orAn11TEioO8CUpJ6rHwetlPtBHJzvTBS452N7-kn9fD4FJTgksssD1fuBf93sgiqjPcw8jIiigc40CcVkQKg8AvS5tjQFax3Wsy4LXDBo_9YBCKiEOapoUEX7YhE-gt1K) 

