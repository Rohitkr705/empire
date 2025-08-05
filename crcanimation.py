import tkinter as tk

# Define the CRC polynomial (x^11 + x^10 + x^9 + x^5 + x^2 + 1)
POLYNOMIAL = 0b11000110000

class CRCWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("CRC Algorithm")
        self.master.geometry("400x400")

        self.frame_input = tk.Frame(self.master)
        self.frame_input.pack()

        self.label_input = tk.Label(self.frame_input, text="Enter 12 bits:")
        self.label_input.pack(side=tk.LEFT)

        self.entry_input = tk.Entry(self.frame_input, width=20)
        self.entry_input.pack(side=tk.LEFT)

        self.button_compute = tk.Button(self.master, text="Compute", command=self.compute_crc)
        self.button_compute.pack()

        self.frame_output = tk.Frame(self.master)
        self.frame_output.pack()

        self.label_output = tk.Label(self.frame_output, text="CRC Result:")
        self.label_output.pack(side=tk.LEFT)

        self.entry_output = tk.Entry(self.frame_output, width=20, state=tk.DISABLED)
        self.entry_output.pack(side=tk.LEFT)

    def compute_crc(self):
        data = int(self.entry_input.get(), 2)  # Convert input string to integer

        # Perform CRC division
        dividend = data << 11  # Shift left by 11 bits to make room for CRC remainder
        for i in range(12):
            if dividend & (1 << (23-i)):
                dividend ^= POLYNOMIAL << (12-i-1)

            # Update graphics
            self.draw_dividend(dividend, i)
            self.master.update()
            self.master.after(500)

        crc = dividend >> 11  # Remove the 11 CRC remainder bits from the dividend
        self.entry_output.config(state=tk.NORMAL)
        self.entry_output.delete(0, tk.END)
        self.entry_output.insert(0, format(crc, "012b"))
        self.entry_output.config(state=tk.DISABLED)

    def draw_dividend(self, dividend, step):
        canvas = tk.Canvas(self.master, width=300, height=50)
        canvas.pack()

        # Draw dividend bits
        for i in range(12):
            bit = (dividend >> (11-i)) & 1
            x = i*25 + 10
            y = 25
            canvas.create_text(x, y, text=str(bit))

        # Draw vertical line
        x1 = 150
        y1 = 40
        x2 = 150
        y2 = 70
        canvas.create_line(x1, y1, x2, y2)

        # Draw polynomial bits
        for i in range(11):
            bit = (POLYNOMIAL >> (10-i)) & 1
            x = i*25 + 10
            y = 100
            canvas.create_text(x, y, text=str(bit))

        # Draw horizontal line
        x1 = 150
        y1 = 85
        x2 = 150 + (12-step)*25
        y2 = 85
        canvas.create_line(x1, y1, x2, y2)

        canvas.update()
        canvas.after(500)

if __name__ == "__main__":
    root = tk.Tk()
    app = CRCWindow(root)
    root.mainloop()
