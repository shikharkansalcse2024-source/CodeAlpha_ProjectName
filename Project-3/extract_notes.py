# ============================================================
# extract_notes.py
# Step 1: Read all MIDI files and extract notes/chords as text
# ============================================================

import glob
from music21 import converter, note, chord


def get_notes_from_file(file_path):
    """Reads one MIDI file and returns a list of notes/chords as strings."""
    midi_data = converter.parse(file_path)
    notes = []

    # .flatten() gives us a flat sequence of all musical elements
    elements = midi_data.flatten().notes

    for element in elements:
        if isinstance(element, note.Note):
            # Single note: save its pitch name e.g. "C4", "E-5"
            notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            # Chord: save pitch numbers joined by dots e.g. "4.9"
            notes.append('.'.join(str(n) for n in element.normalOrder))

    return notes


if __name__ == "__main__":
    all_notes = []

    # Loop through every .mid file in the midi_songs folder
    for file_path in glob.glob("midi_songs/*.mid"):
        print(f"Reading: {file_path}")
        song_notes = get_notes_from_file(file_path)
        all_notes.extend(song_notes)

    print("\nTotal notes/chords extracted:", len(all_notes))
    print("First 20 notes/chords:", all_notes[:20])
