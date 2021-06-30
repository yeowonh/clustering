# 군집화
<정리할 내용>
* kmeans 알고리즘
* 계층 군집 알고리즘
* PAM 알고리즘
* DBSCAN
* 평균이동

## 군집화 개요

**군집화(클러스터링)**: 주어진 데이터 집합을 유사한 데이터들의 그룹으로 나눈것

예측 문제와 달리 특정한 독립변수, 종속변수의 구분이 없으며 목표값을 필요로 하지 않는 **비지도학습**의 일종이다.

- K-평균 군집화(K-means Clustering)
- 디비스캔 군집화(DBSCAN Clustering)
- 유사도 전파 군집화(Affinity Propagation Clustering)
- 계층적 군집화(Hierarchical Clustering)
- 스펙트럴 군집화(Spectral Clustering)

군집화 방법은 사용법과 모수 등이 서로 다르다. 예를 들어 K-평균법이나 스펙트럴 군집화 등은 군집의 개수를 미리 지정해주어야 하지만 디비스캔이나 유사도 전파법 등은 군집의 개수를 지정할 필요가 없다. 다만 이 경우에는 모형에 따라 특별한 모수를 지정해주어야 하는데 이 모수의 값에 따라 군집화 개수가 달라질 수 있다.

> https://datascienceschool.net/03%20machine%20learning/16.01%20%EA%B5%B0%EC%A7%91%ED%99%94.html

참고 자료 : 파이썬 머신러닝 완벽 가이드, 구글링(출처 별도 표기)
