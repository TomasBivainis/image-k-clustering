import data_utils
import cluster_utils
import argparse

def colour_image_with_k_means(filepath, k, n_iterations, n_initializations, output_path):
  data_points = data_utils.extract_data_points(filepath)
  
  clusters = cluster_utils.train_clusters(data_points, k, n_iterations, n_initializations)
  
  new_data_points = data_utils.colour_image(data_points, clusters)
  
  data_utils.convert_data_points_to_image(filepath, new_data_points, output_path)

def colour_image_with_specific_colours(filepath, colours, output_path):
  data_points = data_utils.extract_data_points(filepath)
  
  clusters = []
  for color in colours:
    clusters.append(cluster_utils.Cluster([color]))
    
  new_data_points = data_utils.colour_image(data_points, clusters)
  
  data_utils.convert_data_points_to_image(filepath, new_data_points, output_path)

def main():
  # Set up argument parser
  parser = argparse.ArgumentParser(description='Quantize image colors using k-means clustering')
  parser.add_argument('--input', required=True, help='Path to input image')
  parser.add_argument('--output', default='quantized.png', help='Path to save output image')
  parser.add_argument('--k', type=int, default=3, help='Number of colors in output image')
  
  args = parser.parse_args()
  
  colour_image_with_k_means(args.input, args.k, 10, 5, args.output)

if __name__ == '__main__':
  main()
  

  
    
    
    
    


