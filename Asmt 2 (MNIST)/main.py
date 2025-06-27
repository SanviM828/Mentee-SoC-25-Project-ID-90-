import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torch.optim as optim
from model import SimpleNN, CNN
from learner import run_epochs, evaluate
from utils import plot_metrics, show_confusion

transform = transforms.Compose([transforms.ToTensor()])

train_set = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
val_set = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_set, batch_size=64, shuffle=True)
val_loader = DataLoader(val_set, batch_size=1000, shuffle=False)

model = CNN()  # or SimpleNN()
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = torch.nn.CrossEntropyLoss()

loss_list, acc_list = run_epochs(model, train_loader, val_loader, optimizer, loss_fn, num_epochs=5)
plot_metrics(loss_list, acc_list)
show_confusion(model, val_loader)

torch.save(model.state_dict(), 'saved_model.pth')
print("Model saved!")