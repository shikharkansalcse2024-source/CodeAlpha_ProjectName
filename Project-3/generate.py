# ============================================================
# generate.py
# Step 5: Use the trained model to generate new music
# ============================================================

import pickle
import random
import torch
from model import MusicLSTM

NUM_NOTES_TO_GENERATE = 200
TEMPERATURE = 0.8  # balanced randomness: lower = safer, higher = more creative


def sample_next_note(predictions, temperature):
    """Picks the next note using weighted randomness instead of always top choice."""
    predictions = predictions / temperature
    probabilities = torch.softmax(predictions, dim=-1)
    next_note = torch.multinomial(probabilities, num_samples=1)
    return next_note.item()


if __name__ == "__main__":
    # Load preprocessed data (for vocabulary and note mappings)
    with open("processed_data.pkl", "rb") as f:
        network_input, network_output, note_to_int, unique_notes = pickle.load(f)

    vocab_size = len(unique_notes)
    int_to_note = {number: note_name for note_name, number in note_to_int.items()}

    # Load the trained model
    model = MusicLSTM(vocab_size=vocab_size)
    model.load_state_dict(torch.load("model_final.pth"))
    model.eval()  # switch to prediction mode (turns off dropout)

    # Pick a random starting seed from the training data
    start_index = random.randint(0, len(network_input) - 1)
    pattern = list(network_input[start_index])

    generated_notes = []

    print("Generating music...")

    with torch.no_grad():  # no gradients needed during generation
        for note_index in range(NUM_NOTES_TO_GENERATE):
            input_tensor = torch.tensor([pattern])
            predictions = model(input_tensor)[0]

            next_note_id = sample_next_note(predictions, TEMPERATURE)
            generated_notes.append(int_to_note[next_note_id])

            # slide window: drop oldest note, add new prediction
            pattern.append(next_note_id)
            pattern = pattern[1:]

    print(f"Generated {len(generated_notes)} notes/chords.")
    print("Preview:", generated_notes[:20])

    # Save for next step
    with open("generated_notes.pkl", "wb") as f:
        pickle.dump(generated_notes, f)

    print("\nSaved to generated_notes.pkl")
