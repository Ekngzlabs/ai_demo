# dataset_memory_test.py
import numpy as np
import psutil
 
def ram_gb(): return psutil.virtual_memory().used / 1e9
 
print(f'RAM before : {ram_gb():.2f} GB')
 
# Simulate loading 10,000 images at 224x224 pixels, 3 colour channels
# Each pixel value is a float32 (4 bytes)
# Total: 10000 x 224 x 224 x 3 x 4 bytes = 6.02 GB
num_images  = 10_000
height, width, channels = 224, 224, 3
 
print(f'Allocating simulated dataset ({num_images} images at {height}x{width}x{channels})...')
dataset = np.zeros((num_images, height, width, channels), dtype=np.float32)
 
print(f'RAM after  : {ram_gb():.2f} GB')
expected_gb = num_images * height * width * channels * 4 / 1e9
print(f'Expected increase: {expected_gb:.2f} GB')
print(f'Dataset array size: {dataset.nbytes / 1e9:.2f} GB') 

# Force the OS to actually commit physical pages by writing non-zero values
dataset[:] = 1.0  # or np.random.rand(...) — anything that touches every page
print(f'RAM after write: {ram_gb():.2f} GB')  # NOW it jumps ~6 GB

input('Press Enter to release dataset...')
del dataset
import gc; gc.collect()
print(f'RAM after release : {ram_gb():.2f} GB')
