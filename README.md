
# Multiple Canvases with Moving Squares

This Python code demonstrates:

Creating multiple canvases using Tkinter
Animating objects on canvases with random movement and resizing
Managing object interactions and freezing events
Saving data to a CSV file
Key Features:

MovingSquare Class: Encapsulates square behavior and properties.
Random Number Generation: Drives both movement and freezing.
Frozen Time Tracking: Measures how long each square remains frozen.
CSV Data Logging: Saves frozen times for analysis.
Automatic Restart: Resets the simulation when all squares are frozen.
Dependencies:

Python 3.x
Tkinter (tkinter module)
Usage:

Clone or download this repository.

Run the sr2 or sr3.py file using Python:

Bash
python sr2 or sr3.py
Use code. Learn more
Visual Output:

The program creates a window with five canvases, each containing a moving square.
Squares move and resize randomly within their canvases.
Squares freeze when a generated number matches their position.
Frozen times are displayed in the console and saved to a CSV file.
The simulation restarts when all squares are frozen.
Further Exploration:

Experiment with different movement patterns and freezing conditions.
Explore visualization techniques to represent frozen times.
Integrate the simulation with other data analysis tools.
Extend the functionality to handle more complex interactions and scenarios.
Here's a breakdown of what the code does:

1. Imports Necessary Libraries:

tkinter: Used for creating graphical user interfaces (GUIs) in Python.
random: Generates random numbers for movement and freezing events.
time: Used for measuring time intervals and freezing durations.
csv: Used for saving data to a CSV file.
2. Creates a MovingSquare Class:

Represents a square that can move and resize on a canvas.
Has attributes for position, size, frozen state, and frozen time.
Has methods for:
Initializing a square at a random position.
Moving and resizing randomly.
Freezing and unfreezing.
Restarting (resetting position and frozen state).
3. Sets Up the Main Window and Canvases:

Creates a main window using tk.Tk().
Creates five canvases within the window, each 300x300 pixels in size.
Places the canvases side by side using pack().
4. Creates Moving Squares:

Instantiates five MovingSquare objects, one for each canvas.
Each square starts at a random position within its respective canvas.
5. Manages Interactions and Data:

The select_and_check() function repeatedly generates random numbers.
If a number matches a square's position, the square is frozen.
The total frozen time for each square is tracked.
When all squares are frozen, their frozen times are saved to a CSV file, and they are restarted.
The restart_squares() function resets all squares to their initial state.
6. Runs the GUI:

Starts the GUI event loop using window.mainloop(), which keeps the window visible and responsive until closed.
