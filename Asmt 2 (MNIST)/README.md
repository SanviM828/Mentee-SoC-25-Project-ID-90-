# MNIST Digit Classifier - Assignment Report

## Key Findings
- A Convolutional Neural Network (CNN) was trained on the MNIST dataset to classify handwritten digits (0–9).
- The model achieved over 98% accuracy on the test set after just 5 epochs.
- The confusion matrix shows minimal misclassifications, indicating strong generalization and robustness of the CNN.
- The loss curve decreased steadily and the accuracy curve plateaued around 99%, showing stable training without overfitting.

## Model Architecture and Design Choices

### Dataset:
MNIST: Grayscale images of handwritten digits (28x28 pixels), with 60,000 training and 10,000 test samples.

### Preprocessing:
Images were converted to tensors and normalized using `transforms.ToTensor()`.

### Models Explored:

#### 1. SimpleNN (Feedforward Neural Network)
- Input: Flattened 28x28 image (784 features)
- Layers: `Linear(784 → 128)` → ReLU → `Linear(128 → 10)`
- Performs decently but lacks spatial feature extraction.

#### 2. CNN (Used for final submission)
- `Conv2d(1, 16, kernel_size=3, padding=1)` → ReLU → MaxPool(2x2)  
- `Conv2d(16, 32, kernel_size=3, padding=1)` → ReLU → MaxPool(2x2)  
- Flatten → `Linear(32 × 7 × 7 → 128)` → ReLU → `Linear(128 → 10)`  
- This structure allows the model to capture spatial patterns in images effectively.

### Optimizer & Loss:
- Adam optimizer with learning rate = 0.001  
- CrossEntropyLoss for multi-class classification

## Training Visualizations & Results

### Confusion Matrix:
Shows how well the model predicts each digit class. Almost all predictions are along the diagonal indicating very few errors and strong performance 
models.
#### ![image](https://github.com/user-attachments/assets/82565e36-97dc-42fd-a2ab-4a1c1fc6fe49)


### Loss and Accuracy Over Epochs:
Loss decreased and accuracy consistently increased, stabilizing near 99% within 5 epochs
#### ![image](https://github.com/user-attachments/assets/c22157df-b3ee-43b7-aa20-7ea0b9a49d7b)


### Training Log Output:
Below is the training log showing the model’s performance across 5 epochs. We observe a consistent decrease in loss and an increase in accuracy, 
indicating successful learning.
#### ![training_log](https://github.com/user-attachments/assets/9a54f5a5-06e6-46a4-ab5e-9e20b4350e6f)


## Conclusion
This exercise reinforced key machine learning concepts such as the effectiveness of CNNs for image classification, the use of CrossEntropyLoss for 
multi-class problems, and how Adam optimizer helps with stable convergence. Visual tools like accuracy/loss plots and the confusion matrix helped 
interpret model performance and generalization. Overall, it highlighted how architecture and training choices critically impact outcomes in computer 
vision tasks.
