import tensorflow as tf

def Intiate_model():
    # Configuration
    vocab_size = 100  # Adjust based on dataset
    embed_size = 128
    hidden_size = 256
    max_length = 150  # Max sequence length

    # Encoder
    encoder_inputs = tf.keras.Input(shape=(None, 3))  # (time steps, features)
    encoder_lstm = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(hidden_size, return_sequences=True, return_state=True))
    encoder_outputs, forward_h, forward_c, backward_h, backward_c = encoder_lstm(encoder_inputs)
    encoder_state_h = tf.keras.layers.Concatenate()([forward_h, backward_h])
    encoder_state_c = tf.keras.layers.Concatenate()([forward_c, backward_c])
    encoder_states = [encoder_state_h, encoder_state_c]

    # Decoder
    decoder_inputs = tf.keras.Input(shape=(None,))
    embedding_layer = tf.keras.layers.Embedding(vocab_size, embed_size)
    decoder_embedded = embedding_layer(decoder_inputs)

    # Match the dimensions using a Dense layer to project the encoder outputs to 128 dimensions
    encoder_projection = tf.keras.layers.Dense(128, activation="tanh")(encoder_outputs)

    # Attention Mechanism
    attention = tf.keras.layers.AdditiveAttention()
    context_vector = attention([decoder_embedded, encoder_projection])

    # Proper Concatenation Before Passing to LSTM
    decoder_lstm = tf.keras.layers.LSTM(hidden_size * 2, return_sequences=True, return_state=True)
    decoder_lstm_input = tf.keras.layers.Concatenate(axis=-1)([decoder_embedded, context_vector])
    decoder_outputs, _, _ = decoder_lstm(decoder_lstm_input, initial_state=encoder_states)

    # Output Layer
    output_layer = tf.keras.layers.Dense(vocab_size, activation='softmax')
    decoder_outputs = output_layer(decoder_outputs)

    # Full Model
    # def ctc_loss_function(y_true, y_pred):
    #     return tf.keras.backend.ctc_batch_cost(y_true, y_pred, input_length, label_length)
        
    model = tf.keras.Model([encoder_inputs, decoder_inputs], decoder_outputs)
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['sparse_categorical_accuracy'])
