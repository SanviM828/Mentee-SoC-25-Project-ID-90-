import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import torch


def plot_metrics(loss_list, acc_list):
    plt.figure()
    plt.plot(loss_list, label='Loss')
    plt.plot(acc_list, label='Accuracy')
    plt.xlabel("Epochs")
    plt.ylabel("Value")
    plt.legend()
    plt.savefig("plots/loss_accuracy.png")


def show_confusion(model, val_loader):
    all_preds = torch.tensor([])
    all_labels = torch.tensor([])
    model.eval()
    with torch.no_grad():
        for images, labels in val_loader:
            outputs = model(images)
            _, preds = torch.max(outputs, 1)
            all_preds = torch.cat((all_preds, preds), dim=0)
            all_labels = torch.cat((all_labels, labels), dim=0)

    cm = confusion_matrix(all_labels.numpy(), all_preds.numpy())
    sns.heatmap(cm, annot=True, fmt='d')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.savefig("plots/confusion_matrix.png")