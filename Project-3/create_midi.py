# ============================================================
# create_midi.py
# Step 6: Convert generated notes into a playable MIDI file
# ============================================================

import pickle
from music21 import stream, note, chord, instrument

NOTES_DURATION = 0.5  # duration of each note in quarter-note beats


if __name__ == "__main__":
    # Load generated notes
    with open("generated_notes.pkl", "rb") as f:
        generated_notes = pickle.load(f)

    print(f"Converting {len(generated_notes)} notes to MIDI...")

    output_stream = stream.Stream()
    output_stream.append(instrument.Piano())  # set instrument to piano

    for pattern in generated_notes:
        if '.' in pattern:
            # It's a chord — split by dot and create multiple notes together
            chord_notes = pattern.split('.')
            notes_in_chord = []
            for current_note in chord_notes:
                new_note = note.Note(int(current_note))
                new_note.duration.quarterLength = NOTES_DURATION
                new_note.storedInstrument = instrument.Piano()
                notes_in_chord.append(new_note)
            new_chord = chord.Chord(notes_in_chord)
            output_stream.append(new_chord)
        else:
            # It's a single note — could be a name like "E-5" or a number like "3"
            if pattern.isdigit():
                new_note = note.Note(int(pattern))
            else:
                new_note = note.Note(pattern)
            new_note.duration.quarterLength = NOTES_DURATION
            new_note.storedInstrument = instrument.Piano()
            output_stream.append(new_note)

    # Save as MIDI file
    output_stream.write('midi', fp='output.mid')
    print("Done! Saved as output.mid")
    print("Play it: open output.mid with Windows Media Player or VLC")
