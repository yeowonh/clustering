# 파이썬 머신러닝 완벽가이드
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
%matplotlib inline

X, y = make_blobs(n_samples=200, n_features=2, centers=3, cluster_std=0.8, random_state=0)

# y target 값 분포 확인
unique, counts = np.unique(y, return_counts=True)
print(unique, counts)

# 위의 데이터세트 데이터프레임으로 정리
clusterDF = pd.DataFrame(data=X, columns=['ftr1', 'ftr2'])
clusterDF['target'] = y
clusterDF.head(3)

target_list = np.unique(y)
# 산점도별 마커값
markers = ['o', 's', '^', 'P', 'D', 'H', 'x']

# target 0,1,2로 scatter plot을 마커별 생성
for target in target_list:
	target_cluster = clusterDF[clusterDF['target']==target]
	plt.scatter(x=target_cluster['ftr1'], y=target_cluster['ftr2'], edgecolor='k',
	marker=markers[target])
plt.show()

# 군집별 시각화
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=200, random_state=0)
cluster_labels = kmeans.fit_predict(X)
clusterDF['kmeans_label'] = cluster_labels

# 중심 위치 좌표 시각화
centers = kmeans.cluster_centers_
unique_labels = np.unique(cluster_labels)

for label in unique_labels:
    label_cluster = clusterDF[clusterDF['kmeans_label']==label]
    center_x_y = centers[label]
    plt.scatter(x=label_cluster['ftr1'], y=label_cluster['ftr2'], edgecolor='k',
               marker=markers[label])
    plt.scatter(x=center_x_y[0], y=center_x_y[1], s=200, color='white',
               alpha=0.9, edgecolor='k', marker=markers[label])
    plt.scatter(x=center_x_y[0], y=center_x_y[1], s=70, color='k',
               edgecolor='k', marker='$%d$' % label)
plt.show()
