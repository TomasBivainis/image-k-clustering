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
  
  def get_SSE(self):
    centroid = self.get_centroid()
    SSE = 0
    
    for data_point in self.data:
      SSE += distance(data_point, centroid)
      
    return SSE

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
  
  #print(centroids)
  
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

def calculate_clustering_SSE(clusters):
  SSE = 0
  
  for cluster in clusters:
    SSE += cluster.get_SSE()
    
  return SSE

def train_clusters(data_points, k=3, n_iterations=10, number_of_initialization=3):
  best_clusters = []
  minimum_SSE = -1
  
  for _i in range(number_of_initialization):
    clusters = []
    past_clusters = []
    
    for _j in range(n_iterations):
      clusters = k_means_clustering(data_points, clusters, k)
      
      if np.array_equal(clusters, past_clusters):
        break
        
      past_clusters = clusters.copy()
    
    current_SSE = calculate_clustering_SSE(clusters)
    
    if minimum_SSE == -1 or minimum_SSE > current_SSE:
      minimum_SSE = current_SSE
      best_clusters = clusters
  
  return best_clusters
  
if __name__ == "__main__":
  clu = Cluster([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
  assert np.array_equal(clu.get_centroid(), np.array([2, 3, 4]))
  
  