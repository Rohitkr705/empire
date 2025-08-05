

import tkinter as tk

bits_with_parity = []  # Initialize as an empty list

def calculate_parity(bits):
    """Calculates the parity bit for the given sequence of bits."""
    parity = 0
    for bit in bits:
        parity ^= bit  # XOR operation to calculate parity
    return parity

def check_parity(bits):
    """Checks if the given sequence of bits has even parity."""
    parity = calculate_parity(bits[:-1])
    return parity == bits[-1]

def add_parity_bit(bits):
    """Adds a parity bit to the given sequence of bits."""
    parity = calculate_parity(bits)
    return bits + [parity]

def simulate_error():
    """Simulates an error by flipping one of the bits."""
    bits_with_parity[2] = 1 - bits_with_parity[2]  # Flip the bit
    update_display()

def update_display():
    """Updates the display with the current bits and parity information."""
    if len(bits_with_parity) == 0:
        display.config(text="Bits with parity: ")
        status.config(text="No bits with parity.")
        return

   
    display.config(text="Bits with parity: " + " ".join(str(bit) for bit in bits_with_parity))
    is_valid = check_parity(bits_with_parity)
    if is_valid:
        status.config(text="No errors detected.", fg="green")
    else:
        status.config(text="Error detected.", fg="red")

def process_input():
    """Processes the input bits entered by the user."""
    global bits_with_parity
    input_str = input_entry.get()
    try:
        input_bits = [int(bit) for bit in input_str]
        bits_with_parity = add_parity_bit(input_bits)
        update_display()
    except ValueError:
        display.config(text="Invalid input. Please enter 0s and 1s only.")

# Initialize Tkinter window
window = tk.Tk()
window.title("Parity Check Simulation")

# Create and configure input entry widget
input_entry = tk.Entry(window)
input_entry.pack()

# Create and configure process button
process_button = tk.Button(window, text="Process Input", command=process_input)
process_button.pack()

# Create and configure display labels
display = tk.Label(window, text="Bits with parity: ")
display.pack()

# Create and configure status label
status = tk.Label(window, text="No errors detected.", fg="green")
status.pack()

# Create and configure simulate error button
error_button = tk.Button(window, text="Simulate Error", command=simulate_error)
error_button.pack()

# Update the display initially
update_display()

# Start the Tkinter event loop
window.mainloop()

