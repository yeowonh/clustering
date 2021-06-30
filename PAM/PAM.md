## PAM(=Partitioning Around Medoids)

PAM은 Partitioning Around Medoids라고 하여, Medoids 주위로 파티션닝 하는 것

KMeans는 각 군집을 centroid(평균)으로 나타내기에 이상치에 민감하다는 단점을 극복하기 위한 방법으로 제안됨

각 군집은 하나의 관찰치(medoid) 로 대표되며, kmean에서 유클리드 거리를 사용하는 것과 달리 PAM에서는 다른 거리 측정법도 사용할 수 있기 때문에 연속형 변수들 뿐만 아니라 **mixed data type에도 적합**



* 장점
  * 이상치에 강건함
  * 어떠한 비유사성 측정치에 대해서도 사용할 수 있음
  * 각 클러스터에서 대표적인 객체를 찾는 것이 쉬움. 즉, 해석이 용이함

* 단점
  * k-means와 동일하게 시작점에 따라서, 결과가 달라지므로, 지역적 최적해가 발생 가능
  * 각각의 포인트 끼리의 유클리디안 거리를 다 계산한 최적화를 수행해야 하기 때문에 계산 비용 많이 들어감
  * 다른 스케일 가진 변수에 대해 잘 작동하지 않음



1. K개의 관찰치(medoid)를 무작위로 선택한다.
2. 모든 관찰치에서 각medoid까지의 거리를 계산한다.
3. 각 관찰치를 가장 가까운 medoid에 할당한다.
4. 각 관찰치와 해당하는 medoid사이의 거리의 총합(총비용,total cost)을 계산한다.
5. medoid가 아닌 점 하나를 선택하여 그 점에 할당된 medoid와 바꾼다.
6. 모든 관찰치들을 가장 가까운 medoid에 할당한다.
7. 총비용을 다시 계산한다.
8. 다시계산한 총비용이 더 작다면 새 점들을 medoid로 유지한다.
9. medoid가 바뀌지 않을 때까지 5-8단계를 반복한다.

> https://rstudio-pubs-static.s3.amazonaws.com/249084_09c0daf4ceb24212a81ceddca97ba1ea.html



![k-means와 k-medoid 비교](https://heung-bae-lee.github.io/image/k_means_versus_k_medoid.png)

> https://heung-bae-lee.github.io/2020/05/30/machine_learning_19/



```python
from sklearn_extra.cluster import KMedoids
import numpy as np

X = np.asarray([[1, 2], [1, 4], [1, 0],
                [4, 2], [4, 4], [4, 0]])
kmedoids = KMedoids(n_clusters=2, random_state=0).fit(X)
kmedoids.labels_ # array([0, 0, 0, 1, 1, 1])
kmedoids.predict([[0,0], [4,4]])
kmedoids.cluster_centers_ # array([[1., 2.],[4., 2.]])
kmedoids.inertia_ # 8.0
```

