import tkinter as tk
from tkinter import messagebox
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Define the CRC polynomial and initial value
CRC_POLY = 0b10011
CRC_INIT = 0b1111

def crc_data_flow(message):
    # Initialize CRC value
    crc = CRC_INIT

    # Iterate over message bits and apply CRC algorithm
    for i in range(len(message)):
        # Get current message bit
        bit = (int(message[i]) >> 0) & 1

        # Calculate new CRC value
        if crc & (1 << (len("{:b}".format(CRC_POLY))-1)):
            crc = (crc << 1) ^ CRC_POLY
        else:
            crc = crc << 1

        # Update CRC value with input bit
        if bit:
            crc = crc ^ CRC_POLY

    # Convert CRC value to binary string with leading zeros
    crc_bin = "{:b}".format(crc).zfill(4)

    # Create bar graph of CRC value bits
    plt.bar(range(len(crc_bin)), [int(x) for x in crc_bin], align="center")
    plt.xticks(range(len(crc_bin)), ["D3", "D2", "D1", "D0"])
    plt.yticks([0, 1])
    plt.xlabel("CRC Value Bits")
    plt.ylabel("Bit Value")
    plt.title("CRC Algorithm Bar Graph")

    # Show plot
    plt.show()

def on_submit():
    # Get user input from text box
    message = message_box.get()

    # Validate input
    if not message:
        messagebox.showerror("Error", "Input message cannot be empty")
        return
    if not all(c in "01" for c in message):
        messagebox.showerror("Error", "Input message must be a binary string")
        return

    # Call CRC function with input message
    crc_data_flow(message)

# Create Tkinter window
root = tk.Tk()
root.title("CRC Algorithm Bar Graph")

# Add message label and text box
message_label = tk.Label(root, text="Enter a binary message:")
message_label.pack()
message_box = tk.Entry(root)
message_box.pack()

# Add submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Run Tkinter event loop
root.mainloop()
