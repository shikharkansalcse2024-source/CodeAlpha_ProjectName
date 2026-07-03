# ============================================================
# model.py
# Step 3: Define the LSTM neural network architecture
# ============================================================

import torch
import torch.nn as nn


class MusicLSTM(nn.Module):
    def __init__(self, vocab_size, embedding_dim=100, hidden_size=256):
        super(MusicLSTM, self).__init__()

        # Turns each note-ID into a small vector of numbers (captures meaning)
        self.embedding = nn.Embedding(vocab_size, embedding_dim)

        # Two stacked LSTM layers — the "memory" of the model
        self.lstm = nn.LSTM(
            input_size=embedding_dim,
            hidden_size=hidden_size,
            num_layers=2,
            batch_first=True,
            dropout=0.3  # randomly drops 30% of connections to avoid overfitting
        )

        # Turns the LSTM's final memory into a prediction over all possible notes
        self.output_layer = nn.Linear(hidden_size, vocab_size)

    def forward(self, x):
        # x shape: (batch_size, sequence_length)
        embedded = self.embedding(x)            # -> (batch_size, sequence_length, embedding_dim)
        lstm_out, _ = self.lstm(embedded)        # -> (batch_size, sequence_length, hidden_size)
        last_step = lstm_out[:, -1, :]           # take only the LAST time step's output
        logits = self.output_layer(last_step)    # -> (batch_size, vocab_size)
        return logits


if __name__ == "__main__":
    # Quick test: build the model and verify shapes
    import pickle

    with open("processed_data.pkl", "rb") as f:
        network_input, network_output, note_to_int, unique_notes = pickle.load(f)

    vocab_size = len(unique_notes)
    model = MusicLSTM(vocab_size=vocab_size)

    print(model)

    # Test with a small fake batch
    sample_input = torch.tensor(network_input[:4])
    output = model(sample_input)

    print("\nInput shape:", sample_input.shape)
    print("Output shape:", output.shape)
