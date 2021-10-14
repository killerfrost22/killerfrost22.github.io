import numpy as np
import cv2
from sklearn.cluster import KMeans

n_colors = 10

sample_img = cv2.imread('resources/girl.jpg')
w,h,_ = sample_img.shape
sample_img = sample_img.reshape(w*h,3)
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(sample_img)

# find out which cluster each pixel belongs to.
labels = kmeans.predict(sample_img)

# the cluster centroids is our color palette
identified_palette = np.array(kmeans.cluster_centers_).astype(int)

# recolor the entire image
recolored_img = np.copy(sample_img)
for index in range(len(recolored_img)):
    recolored_img[index] = identified_palette[labels[index]]
    
# reshape for display
recolored_img = recolored_img.reshape(w,h,3)

cv2.imsave('kmeans_color_q.jpg', recolored_img)