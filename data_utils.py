import imageio.v3 as iio
import numpy as np

def extract_data_points(filename: str):
  image = iio.imread(f'data/{filename}')
  
  data_points = np.reshape(image, [image.shape[0] * image.shape[1], image.shape[2]])
  #data_points = np.unique(data_points, axis=0)
  
  return data_points

def convert_data_points_to_image(filename: str, data_points):
  image = iio.imread(f'data/{filename}')
  
  data_points = np.reshape(data_points, image.shape)
  
  iio.imwrite('test.png', data_points)