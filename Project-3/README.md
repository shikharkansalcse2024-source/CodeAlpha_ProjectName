# 🎵 Music Generation with AI (LSTM)

An AI-powered music generation system that learns patterns from classical piano MIDI files and composes original music using a deep learning LSTM model.

---

## 📌 Project Overview

This project uses a Long Short-Term Memory (LSTM) neural network to learn musical patterns from classical piano MIDI files and generate new, original music compositions. The generated music is saved as a playable MIDI file.

---

## 🧠 How It Works

```
MIDI Files → Extract Notes → Preprocess → Train LSTM → Generate Notes → Output MIDI
```

1. **Data Collection**: 80+ classical piano MIDI files
2. **Preprocessing**: Notes and chords extracted using `music21`
3. **Model**: 2-layer LSTM with Embedding layer (PyTorch)
4. **Training**: 30 epochs on 60,140 note sequences
5. **Generation**: Model generates 200 new notes using learned patterns
6. **Output**: Generated notes converted to a playable MIDI file

---

## 📊 Training Results

| Parameter | Value |
|---|---|
| Total MIDI files | 80+ classical piano pieces |
| Vocabulary size | 402 unique notes/chords |
| Training examples | 60,140 sequences |
| Sequence length | 50 notes |
| LSTM hidden size | 256 units |
| Epochs trained | 30 |
| Starting loss | 3.9272 |
| Final loss | 0.4598 |

Loss dropped from **3.9272 → 0.4598** — an 88% reduction, confirming the model learned real musical patterns.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.14 | Programming language |
| PyTorch 2.12.1 | Deep learning framework |
| music21 10.5.0 | MIDI file processing |
| NumPy 2.5.0 | Numerical operations |

---

## 📁 Project Structure

```
MusicAI/
├── midi_songs/          # Training data (classical piano MIDI files)
├── extract_notes.py     # Extracts notes from MIDI files
├── preprocess.py        # Preprocesses notes into training sequences
├── model.py             # LSTM model architecture
├── train.py             # Model training script
├── generate.py          # Music generation script
├── create_midi.py       # Converts generated notes to MIDI file
├── processed_data.pkl   # Saved preprocessed data
├── model_final.pth      # Trained model weights
└── output.mid           # AI-generated music output
```

---

## ⚙️ Setup & Installation

### Install Dependencies
```bash
pip install music21 torch numpy
```

### Run Step by Step

```bash
# Step 1: Extract notes
python extract_notes.py

# Step 2: Preprocess
python preprocess.py

# Step 3: Train model (takes ~30-60 mins on CPU)
python train.py

# Step 4: Generate music
python generate.py

# Step 5: Create and play MIDI
python create_midi.py
start output.mid
```

---

## 🎯 Model Architecture

```
Input (50 notes)
      ↓
Embedding Layer (402 → 100 dimensions)
      ↓
LSTM Layer 1 (256 hidden units)
      ↓
LSTM Layer 2 (256 hidden units) + Dropout (0.3)
      ↓
Linear Output Layer (256 → 402)
      ↓
Predicted Next Note
```

---

## ⚠️ Limitations

- All notes have equal duration (no rhythm variation)
- Trained on CPU — slower than GPU training
- Small dataset compared to professional systems

---

*Internship Project — Music Generation with AI using Deep Learning*
