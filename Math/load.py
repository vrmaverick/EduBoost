import os
import numpy as np
import xml.etree.ElementTree as ET

def preprocess_strokes(strokes, max_length=100):
    """
    Normalize and pad strokes to ensure a consistent input shape.
    - Normalizes (X, Y) coordinates.
    - Pads/truncates strokes to max_length.
    """
    all_points = np.concatenate(strokes, axis=0) if strokes else np.array([[0, 0]])
    
    # Normalize X and Y to [0,1] range
    min_vals = np.min(all_points, axis=0)
    max_vals = np.max(all_points, axis=0)
    norm_strokes = [(s - min_vals) / (max_vals - min_vals + 1e-5) for s in strokes]
    
    # Flatten strokes and pad/truncate to fixed size
    flat_strokes = np.concatenate(norm_strokes, axis=0)[:max_length]
    pad_length = max_length - len(flat_strokes)
    padded_strokes = np.pad(flat_strokes, ((0, pad_length), (0, 0)), mode='constant')
    
    return padded_strokes



def parse_inkml(file_path):
    """
    Parse an InkML file and return:
    - strokes: a list of numpy arrays (each is a stroke of shape [n_points, 2])
    - label: the LaTeX label (ground truth) if available
    """
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Handling namespaces (InkML files typically use a default InkML namespace)
    ns = {'ink': 'http://www.w3.org/2003/InkML'}
    
    # Get annotation (if present)
    label = None
    for annotation in root.findall('ink:annotation', ns):
        # Choose normalizedLabel if available; fallback to label
        if annotation.get('type') == 'normalizedLabel':
            label = annotation.text.strip()
            break
        elif annotation.get('type') == 'label':
            label = annotation.text.strip()
    
    strokes = []
    # Each <trace> element contains a stroke
    for trace in root.findall('ink:trace', ns):
        trace_data = trace.text.strip()
        points = []
        # InkML usually separates points by commas and coordinates by space
        for point_str in trace_data.split(','):
            # Remove extra spaces and split by whitespace
            coords = point_str.strip().split()
            if len(coords) >= 2:
                x, y = float(coords[0]), float(coords[1])
                points.append([x, y])
        if points:
            strokes.append(np.array(points))
    
    return strokes, label

def load_dataset(inkml_dirs, num_files=1000, max_length=100):
    samples = []
    labels = []
    charset = set()

    for root_dir in inkml_dirs:
        files = [f for f in os.listdir(root_dir) if f.endswith('.inkml')][:num_files]  # Limit files
        for file in files:
            path = os.path.join(root_dir, file)
            strokes, label = parse_inkml(path)
            
            if strokes and label:
                processed_strokes = preprocess_strokes(strokes, max_length)
                samples.append(processed_strokes)
                labels.append(label)
                charset.update(label)

    # Create character mappings
    char2idx = {c: i + 1 for i, c in enumerate(sorted(charset))}
    char2idx['<pad>'] = 0
    idx2char = {v: k for k, v in char2idx.items()}

    return samples, labels, char2idx, idx2char

# Convert strokes (samples) into a padded sequence format
import tensorflow as tf

def preprocess(samples, labels, char2idx,max_label_length):
    # max_seq_length = max(len(s) for s in samples)
    target_seq_length = 110  # Find the longest stroke sequence
    padded_samples = np.array([
        np.pad(s, ((0, max(0, target_seq_length - len(s))), (0, 0)), mode='constant')[:target_seq_length]
        for s in samples
    ])
    
    # Ensure padded_samples has shape (batch_size, 110, features)
    padded_samples = np.pad(padded_samples, ((0, 0), (0, 0), (0, 1)), mode='constant')

    # Convert labels into numerical format using char2idx
    numerical_labels = [[char2idx[c] for c in label] for label in labels]

    # Pad label sequences
    # max_label_length = max(
    # max(len(label) for label in labels),
    # max(len(label) for label in test_labels))
    # Pad label sequences
    padded_labels = tf.keras.preprocessing.sequence.pad_sequences(
        numerical_labels, maxlen=max_label_length, padding='post'
    )
    # padded_labels = tf.keras.preprocessing.sequence.pad_sequences(numerical_labels, padding='post')

    # Convert to TensorFlow datasets for efficient loading
    # BATCH_SIZE = 32           

    # train_dataset = tf.data.Dataset.from_tensor_slices((padded_samples, padded_labels))
    # train_dataset = train_dataset.shuffle(10).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
    # return train_dataset
    return padded_samples, padded_labels
