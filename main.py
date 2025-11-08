import file_utils
import data_utils
import cluster_utils
import numpy as np

if __name__ == '__main__':
  filenames = file_utils.get_all_image_names()
  n_iterations = 10
  k = 4

  filename = filenames[2]
  
  points = data_utils.extract_data_points(filename)
  #print(points)
  clusters = []
  past_clusters = []
  
  for _ in range(n_iterations):
    clusters = cluster_utils.k_means_clustering(points, clusters, k)
    
    if np.array_equal(clusters, past_clusters):
      break
      
    past_clusters = clusters.copy()
  
  centroids = [cluster.get_centroid() for cluster in clusters]
  
  new_points = points.copy()
  
  for i in range(len(new_points)):
    closest_centroid = centroids[0]
    min_distance = cluster_utils.distance(new_points[i], closest_centroid)
    
    for centroid in centroids:
      current_distance = cluster_utils.distance(new_points[i], centroid)
      
      if current_distance < min_distance:
        closest_centroid = centroid
        min_distance = current_distance
    
    new_points[i] = closest_centroid
    
  data_utils.convert_data_points_to_image(filename, new_points)
    
    
    
    


