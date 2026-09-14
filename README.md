```
  ░███████ ░███████  ░██     ░██ ░██ ░████████ ░████████ ░██       ░██    ░██ 
  ░██      ░██    ░██░██     ░██ ░██    ░██    ░██       ░██        ░██  ░██  
  ░███████ ░███████  ░██     ░██ ░██    ░██    ░███████  ░██         ░████    
  ░██      ░██   ░██ ░██     ░██ ░██    ░██    ░██       ░██          ░██     
  ░██      ░██    ░██ ░████████  ░██    ░██    ░██       ░████████    ░██     

   ░██████  ░██       ░██ ░████████  ░██████   ░██████  
  ░██    ░██░██       ░██ ░██       ░██    ░██░██    ░██
  ░██       ░████████████ ░███████   ░███████  ░███████ 
  ░██       ░██       ░██ ░██              ░██       ░██
   ░██████  ░██       ░██ ░████████  ░██████   ░██████  
```

<div align="center">

<img src="./static/hd_drosophila_fly.png" alt="Fruitfly Chess" width="480" />

**Play 3D chess against a fruit fly powered by a biological brain connectome GNN & Stockfish NNUE — complete with real-time biomechanics, outer foreleg grooming, and physical piece manipulation.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](./LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![PyG](https://img.shields.io/badge/PyTorch_Geometric-GNN-3C2179?style=for-the-badge)](https://pyg.org)
[![Three.js](https://img.shields.io/badge/Three.js-R3F-000000?style=for-the-badge&logo=three.js&logoColor=white)](https://threejs.org)
[![Stockfish 19](https://img.shields.io/badge/Stockfish-3500+_ELO-1572B6?style=for-the-badge)](https://stockfishchess.org)

[**🐛 Report Bug**](https://github.com/ayuuXploits/fruitfly-chess/issues/new?labels=bug&title=%5BBug%5D+) &nbsp;·&nbsp; [**✨ Request Feature**](https://github.com/ayuuXploits/fruitfly-chess/issues/new?labels=enhancement&title=%5BFeature%5D+) &nbsp;·&nbsp; [**📄 Read License**](./LICENSE)

<br/>

*An anatomically accurate Drosophila melanogaster sits across the chessboard. In real time, the fly breathes, twitches its wings, performs authentic foreleg grooming reflexes, and physically swoops down from its observation perch to grasp chess pieces in its forelegs and fly them to destination squares.*

<br/>

<img src="./static/fly_brain_transparent.png" width="46%" alt="Connectome Brain" /> &nbsp; <img src="./static/hd_drosophila_fly.png" width="46%" alt="NeuroMechFly 3D Model" />

</div>

---

## ✨ Features

### 🪰 The Grandmaster Insect Across the Board
Across the board sits a biological *Drosophila melanogaster* modeled after the scientific **NeuroMechFly** architecture.

| Feature | What it does |
|---|---|
| **Autonomous Flight & Move Execution** | When making a move, the fly takes off from its perch, calculates a 3D Catmull-Rom flight spline, dives onto the piece, clamps it in its forelegs, carries it through the air, and drops it onto the target square. |
| **Biological Foreleg Grooming** | In idle state, the fly’s knees splay outward laterally while its 5-segment tarsi cross in front of the proboscis to rub along the **outer (lateral & dorsal) surfaces** in rapid anti-phase strokes (~4.1 Hz). |
| **Abdominal Respiration** | Realistic biological breathing pumping rhythm expanding and contracting the 7 melanin-banded tergites. |
| **Wing Kinematics** | High-frequency aerodynamic wing flutter (85 rad/s) during flight and calculation saccades; resting in an authentic posterior V-posture over the abdomen. |
| **Neural Synaptic Aura** | Cyan synaptic particle glow radiating from the head and compound eyes whenever the fly is evaluating board positions. |

---

### 🧠 Biological Brain Connectome (GNN) + Stockfish NNUE
- **256-Neuron Biological Graph**: Direct brain wiring topology capturing Sensory Neurons (64), Mushroom Body Kenyon Cells (64), Central Complex Ring Neurons (64), and Motor Descending Output Neurons (64).
- **Graph Neural Network (GNN)**: 3-layer Graph Attention Network (GAT) propagating synaptic activation over connectome edge weights to compute move probabilities.
- **Stockfish 19 NNUE Hybrid Engine**: Combines biological connectome policy heuristics with deep alpha-beta search (depth 14, 3500+ ELO) for tactical mastery.
- **Trained on Magnus Carlsen Games**: Connectome policy weights fine-tuned on Grandmaster games via imitation learning.
- **Ultra-Light Quantized Checkpoint**: Symmetric 8-bit quantized weights (**7.1 MB**) that dequantize on boot with near-zero precision loss (<0.6% deviation).

---

### 🎮 Interactive 3D WebGL Arena
- **Full 3D Chessboard & Pieces**: Procedurally rendered low-poly 3D chess pieces with authentic wooden materials, specular rim lighting, and ambient studio occlusion shadows.
- **Orbit Controls**: Rotate, zoom, and inspect the fly and board from any angle in 3D space with smooth damping.
- **Move Highlights & Legal Move Guides**: Dynamic glowing cyan markers indicating selectable squares, legal destinations, and check status.
- **Live Neural Brain Canvas**: Real-time HUD canvas visualizing active synaptic firings, showing how signals propagate through sensory, mushroom body, and motor neuropils during thinking.
- **Eval Bar & Material Counter**: Real-time evaluation bar and captured piece differential tracker.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend Framework** | React 18 + TypeScript + Vite | Reactive UI state and hot-module reloading |
| **3D Graphics Engine** | Three.js + React Three Fiber (R3F) + Drei | WebGL rendering, lighting, shadows, and orbit controls |
| **Kinematics Engine** | Procedural Inverse Kinematics (Three.js) | Segmented insect limb joints, spline flight curves & grooming |
| **Styling** | Tailwind CSS + CSS Glassmorphism | HUD panels, brain canvas overlays, and responsive layout |
| **Backend Server** | Python 3.10+ & FastAPI + Uvicorn | High-performance asynchronous REST API |
| **Graph Neural Network** | PyTorch & PyTorch Geometric (PyG) | Drosophila connectome graph convolutions and GAT layers |
| **Chess Engine** | python-chess + Stockfish NNUE | FEN/UCI validation, move generation, and tactical evaluation |

---

## 🗂️ Project Structure

```
fruitfly-chess/
├── app.py                          # FastAPI backend & game state controller
├── connectome_chess.py             # Connectome GNN policy & Drosophila graph extractor
├── connectome_model.pt             # Quantized GNN weights (7.12 MB, int8 precision)
├── requirements.txt                # Python backend dependencies
├── LICENSE                         # MIT License with author copyright & research credits
├── README.md                       # Documentation & showcase
├── magnus_carlsen_200_games.pgn    # Grandmaster training dataset
├── magnus_training_log.csv         # Training loss & accuracy metrics
├── static/                         # Static textures, brain diagrams & fly renders
│   ├── hd_drosophila_fly.png       # High-definition fly render
│   ├── fly_brain_transparent.png   # Transparent neuropil schematic
│   ├── fly_brain.png               # High-res connectome diagram
│   ├── realistic_drosophila_body.png
│   └── realistic_drosophila_wing.png
└── frontend/                       # React Three Fiber 3D application
    ├── index.html                  # HTML entry point
    ├── package.json                # NPM scripts and dependencies
    ├── vite.config.ts              # Vite bundling configuration
    ├── tailwind.config.js          # Tailwind styling setup
    ├── dist/                       # Pre-built production bundle (ready to run!)
    └── src/
        ├── App.tsx                 # Main application controller
        ├── main.tsx                # React DOM root
        ├── api.ts                  # REST API communication client
        ├── types.ts                # TypeScript interfaces for game & connectome
        ├── components/
        │   ├── Fly3D.tsx           # NeuroMechFly 3D model & grooming kinematics
        │   ├── Board3D.tsx         # 3D chess board & interactive square highlights
        │   ├── Piece3D.tsx         # Procedural 3D chess pieces
        │   ├── ChessViewport.tsx   # Canvas, studio lighting, shadows & orbit controls
        │   ├── BrainCanvas.tsx     # Real-time connectome neural firing visualizer
        │   ├── EvalBar.tsx         # Evaluation advantage indicator
        │   ├── MoveHistory.tsx     # Move notation table with PGN export
        │   └── Header.tsx          # Status indicators and reset controls
        └── hooks/
            └── useChessGame.ts     # Game state management & API polling hook
```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+**
- **Node.js 18+** *(Optional: only needed if you want to modify and recompile the frontend)*
- A modern browser with WebGL 2.0 support (Chrome, Firefox, Safari, Edge)

---

### 1. Clone the Repository

```bash
git clone https://github.com/ayuuXploits/fruitfly-chess.git
cd fruitfly-chess
```

---

### 2. Set Up Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate       # macOS / Linux
# venv\Scriptsctivate      # Windows (Command Prompt)
# .env\Scripts\Activate.ps1 # Windows (PowerShell)

# Install dependencies
pip install -r requirements.txt
```

---

### 3. Run the Game

```bash
python app.py
```

The server will start at:
👉 **`http://127.0.0.1:8000`**

---

### 4. Frontend Development (Optional)

If you wish to edit the 3D models, shaders, or UI components:

```bash
cd frontend
npm install
npm run dev      # Starts Vite dev server with hot reload at http://localhost:5173
npm run build    # Compiles production bundle to frontend/dist/
```

---

## 🌐 API Reference

The FastAPI backend exposes the following REST endpoints:

| Method | Endpoint | Description | Payload / Parameters |
|---|---|---|---|
| `GET` | `/` | Serves the 3D WebGL React application | None |
| `GET` | `/api/state` | Retrieves the current board state, FEN, turn, check status, and legal moves | None |
| `POST` | `/api/player-move` | Validates and applies a human player move | `{ "move": "e2e4", "mode": "tactical" }` |
| `POST` | `/api/fly-move` | Prompts the Drosophila Connectome AI to compute and execute its move | `{ "mode": "tactical" }` |
| `POST` | `/api/reset` | Resets the game to start position and sets side / AI mode | `{ "player_color": "white", "mode": "tactical" }` |
| `GET` | `/api/connectome` | Fetches 256 neuron coordinates and synaptic weights for HUD visualization | None |

---

## 🔬 Biological & Biomechanical Foundations

### 1. NeuroMechFly Biomechanics
The fly model follows the anatomical articulation from the **NeuroMechFly** project (*Nature Methods*, 2022):
- **Coxa & Trochanter**: Basal thoracic ball-and-socket attachments providing anterior/lateral projection.
- **Spindle Femur**: Muscular thigh tapered at both proximal and distal ends, elevated into high-arched knees.
- **Tibial Spurs**: Distal spines used in natural leg-cleaning reflexes.
- **5-Segment Tarsus**: Articulated basitarsus (T1), tarsomeres (T2–T4), and pretarsus (T5) with claws.
- **Contralateral Foreleg Grooming**: Tarsi cross at the midline in anti-phase reciprocating strokes (~4.1 Hz) to clean their **outer lateral and dorsal surfaces**, recreating the iconic insect grooming behavior.

### 2. FlyWire Connectome Graph
- Utilizes synaptic density matrices derived from the adult *Drosophila* whole-brain electron microscopy volume (**FlyWire**, *Nature*, 2024).
- Information flows sequentially:
  `Sensory Input (64)` ➔ `Mushroom Body (64)` ➔ `Central Complex (64)` ➔ `Motor Descending (64)`
- Graph attention layers compute message-passing vectors across this wiring to output move policy distributions.

---

## 📜 Credits & Attributions

This project synthesizes original game systems with groundbreaking neuroscience and chess computing:

1. **NeuroMechFly (EPFL Biorobotics Laboratory)**
   - *Reference*: Lobato-Ríos et al., *Nature Methods*, 19(5), 620–627 (2022).
   - *Contribution*: 3D multi-segment leg joints, arched knee kinematics, and grooming limits.
2. **FlyWire / FAFB Connectome (Princeton University & Cambridge MRC LMB)**
   - *Reference*: Dorkenwald et al., *Nature* (2024).
   - *Contribution*: Whole-brain synaptic wiring diagram and neuropil groupings.
3. **Stockfish Chess Engine**
   - *Authors*: The Stockfish Developers (GPLv3).
   - *Contribution*: Tactical deep-search evaluation and NNUE positional heuristics.
4. **Python-Chess**
   - *Author*: Niklas Fiekas (GPLv3).
   - *Contribution*: Chess move generation and validation.
5. **Three.js & React Three Fiber**
   - *Authors*: Ricardo Cabello (Mr.doob) & Poimandres (MIT).
   - *Contribution*: WebGL 3D rendering pipeline.

---

## 📄 License

**Copyright © 2026 ayuuXploits. All rights reserved.**

Licensed under the [MIT License](./LICENSE).

---

<div align="center">

Built with 🪰 & ❤️ by [ayuuXploits](https://github.com/ayuuXploits)

</div>
