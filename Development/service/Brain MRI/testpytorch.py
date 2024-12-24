import torch
import torchvision
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Using device: {device}")

devNumber=torch.cuda.current_device()
print(f"Current device number is: {devNumber}")

devName = torch.cuda.get_device_name(devNumber)

print(f" GPU name is: {devName}")

print(f"PyTorch version: {torch.__version__}")
print(f"Torchvision version: {torchvision.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print()
print(torch.cuda.is_available())  # Should return True
print(torch.version.cuda) 
