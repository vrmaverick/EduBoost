import numpy as np
import random

def predict_sequence(model, encoder_input, max_length):
    """Generates a sequence step by step"""
    decoder_input = np.zeros((1, 1))  # Start token
    predictions = []

    for _ in range(max_length):
        output = model.predict([encoder_input, decoder_input])
        predicted_id = np.argmax(output[0, -1, :])  # Get most likely token

        if predicted_id == 0:  # Stop if PAD token is predicted
            break

        predictions.append(predicted_id)

        # Update decoder input for next step
        decoder_input = np.hstack([decoder_input, np.array([[predicted_id]])])

    return predictions

def convert_predictions_to_latex(predictions, idx2char):
    """
    Convert a sequence of predicted token IDs into a LaTeX equation.

    Args:
        predictions (list or np.array): List of predicted token IDs.
        idx2char (dict): Dictionary mapping token IDs to LaTeX tokens.

    Returns:
        str: LaTeX formatted equation.
    """
    latex_tokens = [idx2char.get(token, "") for token in predictions if token in idx2char]
    latex_expression = " ".join(latex_tokens)  # Join tokens with space for readability
    return f"\\[{latex_expression}\\]"  # Wrap with LaTeX math mode delimiters

def random_latex(predicted_data,idx2char):
    r = random.randint(0,len(predicted_data))
    convert_predictions_to_latex(predicted_data[r], idx2char)
