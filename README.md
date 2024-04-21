# Mach-Zehnder Interferometer Simulation

This Python program simulates a Mach-Zehnder interferometer with two input modes and two output modes using the Strawberry Fields library. The user can choose the phase settings for each mode and the initial state preparation.

## Requirements

- Python 3.x
- Strawberry Fields library

## Installation

1. Install Python 3.x

2. Install the Strawberry Fields library using pip:
   ```
   pip install strawberryfields
   ```

## Usage

1. Run the program:
   ```
   python3 interferometer.py
   ```

2. Follow the prompts to choose the phase settings for each mode and the initial state preparation.

3. The program will run the simulation and display the most probable photon number for each output mode.

## Simulation Details

The Mach-Zehnder interferometer consists of the following components:

- Two input modes (Mode 0 and Mode 1)
- Two beam splitters (50/50)
- Two phase shifters (configurable phase settings)
- Two output modes (Mode 0 and Mode 1)
