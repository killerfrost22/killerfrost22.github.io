a
    1�\a  �                   @   s�   d dl Zd dlmZ d dlmZmZ dZed�Zej	\Z
ZZe�e
e d�Zeed d��e�Ze�e�Ze�ej��e�Ze�e�Zeee��D ]Zeee  ee< q�e�e
ed�Zede� dS )	�    N)�KMeans)�imread�imsave�
   zresources/girl.jpg�   )Z
n_clustersZrandom_statezkmeans_color_q.jpg)ZnumpyZnpZsklearn.clusterr   Z
skimage.ior   r   Zn_colorsZ
sample_img�shape�w�h�_ZreshapeZfitZkmeansZpredict�labels�arrayZcluster_centers_Zastype�intZidentified_palette�copyZrecolored_img�range�len�index� r   r   �Ic:\Users\josep\Documents\code\funstuff\Kmean_cluster_reduce_image\code.py�<module>   s   

