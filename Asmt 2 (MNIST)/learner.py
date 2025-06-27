import torch


def run_epochs(model, data_loader, val_loader, optimizer, loss_fn, num_epochs):
    loss_per_epoch = []
    val_accuracy_list = []

    for epoch in range(num_epochs):
        model.train()
        total_loss = 0

        for images, labels in data_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = loss_fn(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        loss_per_epoch.append(total_loss / len(data_loader))
        acc = evaluate(model, val_loader)
        val_accuracy_list.append(acc)

        print(f"Epoch {epoch+1}/{num_epochs} | Loss: {total_loss:.4f} | Accuracy: {acc:.2f}%")

    return loss_per_epoch, val_accuracy_list


def evaluate(model, val_loader):
    model.eval()
    correct = total = 0
    with torch.no_grad():
        for images, labels in val_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return 100 * correct / total