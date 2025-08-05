

import tkinter as tk
import turtle

def generate_blocks():
    original_data = original_data_entry.get()
    block_size = int(block_size_entry.get())
    
    blocks = [original_data[i:i+block_size] for i in range(0, len(original_data), block_size)]
    perform_checksum(blocks)

def perform_checksum(blocks):
    checksum = sum(int(block, 2) for block in blocks)
    
    while checksum >= (1 << len(blocks[0])):
        checksum = (checksum & ((1 << len(blocks[0])) - 1)) + (checksum >> len(blocks[0]))
    
    ones_complement = checksum ^ ((1 << len(blocks[0])) - 1)
    
    draw_blocks(blocks, ones_complement)

def draw_blocks(blocks, ones_complement):
    turtle.clear()
    turtle.penup()
    turtle.goto(-200, 0)
    
    # Draw the original data
    turtle.write("Original Data: " + original_data_entry.get(), align="left", font=("Arial", 14, "normal"))
    turtle.goto(-200, -30)
    
    # Draw the binary blocks
    for i, block in enumerate(blocks):
        turtle.write(block, align="left", font=("Arial", 14, "normal"))
        turtle.goto(-200, -60 - i*30)
    
    # Draw the binary addition
    turtle.goto(-200, -60 - len(blocks)*30)
    turtle.write("Checksum:", align="left", font=("Arial", 14, "normal"))
    turtle.goto(-200, -90 - len(blocks)*30)
    turtle.write(bin(ones_complement)[2:].zfill(len(blocks[0])), align="left", font=("Arial", 14, "normal"))
    
    # Draw a line after the last block value
    turtle.goto(-200, -90 - len(blocks)*30 - 30)
    turtle.pendown()
    turtle.forward(300)
    
    turtle.done()

# GUI setup
root = tk.Tk()
root.title("Checksum Algorithm Simulation")
root.geometry("400x250")

original_data_label = tk.Label(root, text="Enter the original data:")
original_data_label.pack()
original_data_entry = tk.Entry(root)
original_data_entry.pack()

block_size_label = tk.Label(root, text="Enter the block size:")
block_size_label.pack()
block_size_entry = tk.Entry(root)
block_size_entry.pack()

generate_button = tk.Button(root, text="Generate Blocks", command=generate_blocks)
generate_button.pack()

root.mainloop()

