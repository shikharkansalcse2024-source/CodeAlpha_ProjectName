# ============================================================
# preprocess.py
# Step 2: Convert notes to numbers and build training sequences
# ============================================================

import glob
import pickle
import numpy as np
from music21 import converter, note, chord

SEQUENCE_LENGTH = 50  # how many past notes the model looks at to predict the next one


def get_notes_from_file(file_path):
    """Reads one MIDI file and returns a list of notes/chords as strings."""
    midi_data = converter.parse(file_path)
    notes = []
    elements = midi_data.flatten().notes

    for element in elements:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))

    return notes


def prepare_sequences(all_notes):
    """Converts notes to numbers and builds input/target training pairs."""

    # Step 1: build vocabulary — every unique note/chord gets an ID
    unique_notes = sorted(set(all_notes))
    note_to_int = {note_name: number for number, note_name in enumerate(unique_notes)}

    # Step 2: convert the whole note sequence into numbers
    notes_as_int = [note_to_int[n] for n in all_notes]

    # Step 3: sliding window — input=50 notes, output=next note
    network_input = []
    network_output = []

    for i in range(len(notes_as_int) - SEQUENCE_LENGTH):
        seq_in = notes_as_int[i: i + SEQUENCE_LENGTH]
        seq_out = notes_as_int[i + SEQUENCE_LENGTH]
        network_input.append(seq_in)
        network_output.append(seq_out)

    return network_input, network_output, note_to_int, unique_notes


if __name__ == "__main__":
    all_notes = []

    for file_path in glob.glob("midi_songs/*.mid"):
        print(f"Reading: {file_path}")
        all_notes.extend(get_notes_from_file(file_path))

    network_input, network_output, note_to_int, unique_notes = prepare_sequences(all_notes)

    print("\nTotal unique notes/chords (vocabulary size):", len(unique_notes))
    print("Total training examples:", len(network_input))
    print("Example input sequence (as numbers):", network_input[0])
    print("Its target (next note, as number):", network_output[0])

    # Save everything to disk so we don't reprocess every time
    with open("processed_data.pkl", "wb") as f:
        pickle.dump((network_input, network_output, note_to_int, unique_notes), f)

    print("\nSaved processed data to processed_data.pkl")
