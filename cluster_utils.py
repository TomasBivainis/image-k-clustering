import numpy as np
import random

class Cluster(object):
  def __init__(self, data):
    self.data = data
    self.changed = True
  
  def set_changed(self, changed):
    self.changed = changed
  
  def append_point(self, point):
    self.data.append(point)
    self.changed = True
  
  def get_centroid(self):
    if not self.changed:
      return self.centroid
    self.centroid = np.floor(np.average(self.data, axis=0))
    
    return self.centroid

def init_cluster_centroids(points: np.array, clusters, k):
  clusters = []
  centroids = random.sample(points.tolist(), k)
  
  for ind, centroid in enumerate(centroids):
    clusters.append(Cluster([centroid]))
  
  return clusters

def distance(point1, point2):
  return np.sqrt(np.sum(np.power(point1 - point2, 2)))

def k_means_clustering(points, clusters, k=3):
  no_clusters = len(clusters) == 0
  
  if no_clusters:
    clusters = init_cluster_centroids(points, clusters, k)
    
  centroids = [cluster.get_centroid() for cluster in clusters]
  
  print(centroids)
  
  for cluster in clusters:
    cluster.data = []
    
  for point in points:
    index = 0
    min_distance = distance(point, centroids[index])
    
    for i, centroid in enumerate(centroids):
      current_distance = distance(point, centroid)
      
      if current_distance < min_distance:
        min_distance = current_distance
        index = i
    
    clusters[index].append_point(point)
  
  return clusters

if __name__ == "__main__":
  clu = Cluster([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
  assert np.array_equal(clu.get_centroid(), np.array([2, 3, 4]))
  
  