# Physiology & Biochemistry Toolkit 🧬

A Python-based tool for calculating key physiological and biochemical parameters. Designed for pharmacy students to automate calculations found in textbooks like *Vander's Human Physiology* and *Lehninger Principles of Biochemistry*.

## Features

### 1. Cardiac Output (CO)
Calculates blood volume pumped by the heart.
- **Formula:** $CO = HR \times SV$
- **Units:** L/min

### 2. Mean Arterial Pressure (MAP)
Calculates perfusion pressure.
- **Formula:** $MAP = DP + \frac{1}{3}(SP - DP)$

### 3. Beta Oxidation ATP Yield
Calculates net energy from fatty acid breakdown.
- **Formula:** $ATP = (Rounds \times 4) + (AcetylCoA \times 10) - 2$
- **Standard:** Uses modern P/O ratios (NADH=2.5, FADH2=1.5).
- **Verification:** Palmitic Acid (16C) calculates to **106 ATP**.

## How to Run
1. Ensure Python is installed.
2. Run the command:
   ```bash
   python physiology_tool.py
