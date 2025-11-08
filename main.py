import file_utils
import data_utils
import cluster_utils
import numpy as np

def colour_image_with_k_means(filename, k, n_iterations, n_initializations):
  data_points = data_utils.extract_data_points(filename)
  
  clusters = cluster_utils.train_clusters(data_points, k, n_iterations, n_initializations)
  
  new_data_points = data_utils.colour_image(data_points, clusters)
  
  data_utils.convert_data_points_to_image(filename, new_data_points)

def colour_image_with_specific_colours(filename, colours):
  data_points = data_utils.extract_data_points(filename)
  
  clusters = []
  for color in colours:
    clusters.append(cluster_utils.Cluster([color]))
    
  new_data_points = data_utils.colour_image(data_points, clusters)
  
  data_utils.convert_data_points_to_image(filename, new_data_points)
  
if __name__ == '__main__':
  print("bug")
  

  
    
    
    
    


