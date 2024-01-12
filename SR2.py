import tkinter as tk
import random
import time
import csv

class MovingSquare:
    def __init__(self, canvas, side_length=50):
        self.canvas = canvas
        self.side_length = side_length
        self.x1, self.y1 = self.random_position()
        self.x2, self.y2 = self.x1 + side_length, self.y1 + side_length
        self.tag = f"square_{id(self)}"
        self.frozen = False  # Indicates whether the square is frozen
        self.freeze_start_time = 0  # Time when the square is frozen
        self.total_frozen_time = 0  # Total time the square has been frozen
        self.move_and_resize()

    def random_position(self):
        x = random.uniform(0, self.canvas.winfo_width() - self.side_length)
        y = random.uniform(0, self.canvas.winfo_height() - self.side_length)
        return x, y

    def move_and_resize(self):
        if not self.frozen:
            move_x = random.uniform(-5, 5)
            move_y = random.uniform(-5, 5)
            size_change = random.uniform(-10, 10)

            self.x1 += move_x
            self.y1 += move_y
            self.x2 = self.x1 + self.side_length + size_change
            self.y2 = self.y1 + self.side_length + size_change

            # Ensure the square stays within the canvas boundaries
            self.x1 = max(0, min(self.x1, self.canvas.winfo_width() - self.side_length))
            self.y1 = max(0, min(self.y1, self.canvas.winfo_height() - self.side_length))
            self.x2 = max(0, min(self.x2, self.canvas.winfo_width()))
            self.y2 = max(0, min(self.y2, self.canvas.winfo_height()))

            # Draw the updated square on the canvas
            self.canvas.delete(self.tag)
            self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black", width=2, tags=self.tag)
        else:
            # The square is frozen, update the total frozen time
            current_time = time.time()
            self.total_frozen_time += current_time - self.freeze_start_time

        # Schedule the function to be called again after a delay
        self.canvas.after(1000, self.move_and_resize)

    def restart(self):
        self.total_frozen_time = 0
        self.frozen = False
        self.move_and_resize()

    def freeze(self):
        if not self.frozen:
            self.frozen = True
            self.freeze_start_time = time.time()

# Function to select a new number and check for matches
def select_and_check():
    # Generate a new random number between 0 and 300
    new_number = random.uniform(0, 300)
    print("New number:", new_number)

    # Check if the new number matches the position of any square
    frozen_squares = 0
    for square in [square1, square2, square3, square4, square5]:
        if (
            square.x1 <= new_number <= square.x2 and
            square.y1 <= new_number <= square.y2
        ):
            square.freeze()
            print(f"Square {square.tag} is frozen at position ({square.x1}, {square.y1}) for {square.total_frozen_time:.2f} seconds")
            frozen_squares += 1

    # If all squares are frozen, save the frozen times to a CSV file and restart squares
    if frozen_squares == 5:
        save_frozen_times()
        restart_squares()

    # Schedule the function to be called again after a delay
    window.after(1000, select_and_check)

# Function to save frozen times to a CSV file
def save_frozen_times():
    filename = "frozen_times.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Square", "Total Frozen Time (seconds)"])
        for square in [square1, square2, square3, square4, square5]:
            writer.writerow([square.tag, f"{square.total_frozen_time:.2f}"])
            square.total_frozen_time = 0  # Reset the frozen time after saving

# Function to restart all squares
def restart_squares():
    print("Restarting all squares")
    for square in [square1, square2, square3, square4, square5]:
        square.restart()

# Create the main window
window = tk.Tk()
window.title("Multiple Canvases with Moving Squares")

# Create and place GUI components
canvas1 = tk.Canvas(window, width=300, height=300, bg="white")
canvas1.pack(side=tk.LEFT, padx=10)

canvas2 = tk.Canvas(window, width=300, height=300, bg="white")
canvas2.pack(side=tk.LEFT, padx=10)

canvas3 = tk.Canvas(window, width=300, height=300, bg="white")
canvas3.pack(side=tk.LEFT, padx=10)

canvas4 = tk.Canvas(window, width=300, height=300, bg="white")
canvas4.pack(side=tk.LEFT, padx=10)

canvas5 = tk.Canvas(window, width=300, height=300, bg="white")
canvas5.pack(side=tk.LEFT, padx=10)

# Create a square for each canvas
square1 = MovingSquare(canvas1)
square2 = MovingSquare(canvas2)
square3 = MovingSquare(canvas3)
square4 = MovingSquare(canvas4)
square5 = MovingSquare(canvas5)

# Start the GUI event loop
window.after(1000, select_and_check)  # Start the automatic selection of numbers
window.mainloop()
