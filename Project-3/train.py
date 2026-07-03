# ============================================================
# train.py
# Step 4: Train the LSTM model on preprocessed music data
# ============================================================

import pickle
import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from model import MusicLSTM

BATCH_SIZE = 64
EPOCHS = 30
LEARNING_RATE = 0.001


class NoteDataset(Dataset):
    """Wraps our input/output lists so PyTorch can load them in batches."""
    def __init__(self, inputs, outputs):
        self.inputs = torch.tensor(inputs)
        self.outputs = torch.tensor(outputs)

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, idx):
        return self.inputs[idx], self.outputs[idx]


if __name__ == "__main__":
    # Load the preprocessed data
    with open("processed_data.pkl", "rb") as f:
        network_input, network_output, note_to_int, unique_notes = pickle.load(f)

    vocab_size = len(unique_notes)

    dataset = NoteDataset(network_input, network_output)
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

    model = MusicLSTM(vocab_size=vocab_size)

    # CrossEntropyLoss: standard for "pick correct note out of 402 options" problems
    loss_function = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

    print(f"Training on {len(dataset)} examples, vocab size {vocab_size}")
    print(f"Batches per epoch: {len(dataloader)}\n")

    loss_history = []  # track loss per epoch for plotting

    for epoch in range(1, EPOCHS + 1):
        total_loss = 0

        for batch_inputs, batch_targets in dataloader:
            optimizer.zero_grad()               # clear old gradients
            predictions = model(batch_inputs)   # forward pass
            loss = loss_function(predictions, batch_targets)
            loss.backward()                     # backpropagation
            optimizer.step()                    # update model weights

            total_loss += loss.item()

        avg_loss = total_loss / len(dataloader)
        loss_history.append(round(avg_loss, 4))
        print(f"Epoch {epoch}/{EPOCHS} - Average Loss: {avg_loss:.4f}")

        # Save a checkpoint every 5 epochs
        if epoch % 5 == 0:
            torch.save(model.state_dict(), "model_checkpoint.pth")
            print(f"  -> Saved checkpoint at epoch {epoch}")

    # Save the final trained model
    torch.save(model.state_dict(), "model_final.pth")
    print("\nTraining complete! Saved as model_final.pth")

    # Save loss history for plotting
    with open("loss_history.json", "w") as f:
        json.dump(loss_history, f)
    print("Loss history saved to loss_history.json")
