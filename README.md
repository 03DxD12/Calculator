# OmniCalc 🧮

A modern, high-precision, and responsive **All-in-One Calculator** featuring **Standard Arithmetic**, **Scientific Computations**, and a **Cash & Change Denomination Calculator** (Philippine Peso ₱), wrapped in a sleek glassmorphism UI with tactile animations and keyboard shortcuts.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![GitHub Repository](https://img.shields.io/badge/GitHub-03DxD12%2FCalculator-181717?style=flat&logo=github)](https://github.com/03DxD12/Calculator)

---

## ✨ Features

### 1. 🔣 Three Specialized Operational Modes
- **Standard Mode**: Everyday arithmetic operations (`+`, `−`, `×`, `÷`), percentage (`%`), negation (`±`), backspace (`⌫`), and memory functions (`MC`, `MR`, `M+`, `M-`).
- **Scientific Mode**: 
  - Trigonometric functions: $\sin$, $\cos$, $\tan$, and inverses ($\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$).
  - Exponential & Logarithmic: $x^y$, $x^2$, $\sqrt{x}$, $\log_{10}$, $\ln$.
  - Constants & Combinatorics: $\pi$, $e$, factorial ($x!$), reciprocal ($1/x$), absolute value ($|x|$).
  - Degree ($\text{DEG}$) / Radian ($\text{RAD}$) angle mode toggling.
- **Cash & Change Denomination Calculator (PHP ₱)**:
  - Computes exact change from total price and amount tendered.
  - Automatically breaks down change into optimal Philippine Peso bill denominations (₱1,000, ₱500, ₱200, ₱100, ₱50, ₱20) and coin denominations (₱10, ₱5, ₱1, 25¢, 10¢, 5¢, 1¢).
  - Quick-tender helper buttons (`+₱50`, `+₱100`, `+₱500`, `+₱1,000`, and `Exact`).

### 2. 📜 Calculation History Tape
- Slide-in history drawer that records past calculations with timestamps.
- Tap any historical entry to recall and load the result into the display.
- Clear history at any time; stored persistently in `localStorage`.

### 3. 🎨 4 Modern Themes
- **Obsidian**: Deep dark mode with vibrant indigo and cyan glow.
- **Midnight**: OLED pure-black with purple and pink accents.
- **Emerald**: Futuristic cyberpunk terminal green theme.
- **Titanium**: Clean, light frosted-silver daylight aesthetic.
- Theme preference is saved locally across sessions.

### 4. 🔊 Tactile Sound & Haptic Feedback
- Web Audio API synthesizer for tactile mechanical click sounds (with mute toggle).
- Mobile device vibration feedback on keypress via the Vibration API.

### 5. 📱 Responsive & Mobile-Optimized
- Touch-friendly tap targets (`min-height: 48px`).
- Dynamic font-resizing display to prevent clipping on long numbers.
- Smooth transitions and zero horizontal overflow on small devices down to 320px.

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
| :--- | :--- |
| `0` – `9` | Input Digits |
| `.` | Decimal point |
| `+` | Addition |
| `-` | Subtraction |
| `*` or `x` | Multiplication |
| `/` | Division |
| `Enter` or `=` | Calculate / Equals |
| `Backspace` | Delete last digit |
| `Escape` | Clear All (`AC`) |
| `%` | Percentage |
| `^` | Power ($x^y$) in Scientific mode |

---

## 📁 Project Structure

```text
Calculator/
├── .gitignore       # Git ignore rules for editor, OS, and temp files
├── LICENSE          # MIT Open Source License
├── README.md        # Comprehensive documentation
├── index.html       # Flagship OmniCalc web application
├── calcu.html       # Standalone synchronized calculator page
├── styles.css       # Complete design system, theme tokens, and animations
└── filename.py      # Python reference script for Philippine Peso change distribution
```

---

## 🚀 Getting Started

### Option 1: Open in Browser Directly
Simply double-click `index.html` (or `calcu.html`) to launch the calculator directly in any modern browser (Chrome, Edge, Firefox, Safari).

### Option 2: Run with a Local Web Server
Using Python:
```bash
# Python 3
python -m http.server 8080
```
Then navigate to:
```text
http://localhost:8080
```

Using Node.js:
```bash
npx serve .
```

---

## 🐍 Python Change Distribution Script

The included [`filename.py`](filename.py) provides a CLI implementation of the Philippine Peso change calculation logic:

```bash
python filename.py
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Developed with ❤️ by [03DxD12](https://github.com/03DxD12/Calculator)
