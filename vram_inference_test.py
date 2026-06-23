# vram_inference_test.py
import torch
from torchvision.models import resnet18, ResNet18_Weights 
import psutil
 
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Running on: {device}')
 
def show_memory():
    ram = psutil.virtual_memory()
    print(f'  RAM  : {ram.used/1e9:.2f} GB used  ({ram.percent:.1f}%)')
    if device == 'cuda':
        print(f'  VRAM : {torch.cuda.memory_allocated()/1e9:.2f} GB allocated')
        print(f'  VRAM : {torch.cuda.memory_reserved()/1e9:.2f} GB reserved')
 
print('Before loading model:')
show_memory()
 
# Load a pre-trained ResNet-18 (11 million parameters, ~44 MB at FP32)
model = resnet18(weights=ResNet18_Weights.DEFAULT).to(device)

model.eval()
 
print('After loading model to device:')
show_memory()
 
# Create a batch of 32 random images (simulating input data)
batch = torch.randn(32, 3, 224, 224).to(device)
 
print('After loading batch to device:')
show_memory()
 
# Run inference (no gradients needed)
with torch.no_grad():
    output = model(batch)
 
print('After inference:')
show_memory()
print(f'Output shape: {output.shape}')  # Expected: torch.Size([32, 1000])
