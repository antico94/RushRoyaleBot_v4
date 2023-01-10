import numpy as np


TEST_DIR = 'C:/Users/Meiu/Desktop/unit_np/Boreas/00ad847c-7281-48f2-8988-741801f97920.png.npy'
array = np.load(TEST_DIR)

# Get the shape of the array
shape = array.shape

print(shape)