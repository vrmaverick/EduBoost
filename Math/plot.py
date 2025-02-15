import matplotlib.pyplot as plt
import numpy as np

def plot_curves(history,training_metrics,validation_metrics):

    # Plot accuracy
    plt.figure(figsize=(12, 5))

    # Subplot 1: Accuracy
    plt.subplot(1, 2, 1)
    plt.plot(history.history[training_metrics], label='Train Accuracy')
    plt.plot(history.history[validation_metrics], label='Val Accuracy')
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.title("Training and Validation Accuracy")

    # Subplot 2: Loss
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Val Loss')
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.title("Training and Validation Loss")

    # Show the plots
    plt.show()

def evaluate_model(model,x,y):
    start_token = 0 
    decoder_inputs = np.pad(y[:, :-1], ((0, 0), (1, 0)), constant_values=start_token)
    train_loss, train_acc = model.evaluate([x, decoder_inputs], y)
    print(f"Train Accuracy: {train_acc:.4f}")