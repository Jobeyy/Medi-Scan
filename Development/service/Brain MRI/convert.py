import torch
from model import YourModelClass

model = YourModelClass()
model.load_state_dict(torch.load("your_model.pth"))
model.eval()
scripted_model = torch.jit.script(model)  # or torch.jit.trace(model, example_input)
torch.jit.save(scripted_model, "your_model_scripted.pt")
