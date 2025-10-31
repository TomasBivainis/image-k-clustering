import os

def get_all_image_names():
  return os.listdir("data")
  
if __name__ == "__main__":
  print(get_all_image_names())