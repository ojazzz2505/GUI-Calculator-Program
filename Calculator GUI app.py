import tkinter as tk
from tkinter import messagebox
import math


# Function to perform the calculations
def calculate():
    try:
        choice = operation_var.get()
        num1 = float(entry_num1.get()) if entry_num1.get() else None
        num2 = float(entry_num2.get()) if entry_num2.get() else None
        if choice in ['1', '2', '3', '4', '5']:
            if num1 is None or num2 is None:
                raise ValueError("Both numbers are required.")
        elif choice == '6':
            num = float(entry_num1.get()) if entry_num1.get() else None
        elif choice == '7':
            angle = float(entry_num1.get()) if entry_num1.get() else None
        elif choice == '8':
            root.destroy()
            return
        else:
            raise ValueError("Invalid choice.")

        # Perform the selected operation
        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            result = num1 / num2
        elif choice == '5':
            result = num1 ** num2
        elif choice == '6':
            result = math.sqrt(num)
        elif choice == '7':
            radian = math.radians(angle)
            result = f"sin({angle}) = {math.sin(radian)}, cos({angle}) = {math.cos(radian)}, tan({angle}) = {math.tan(radian)}"

        result_label.config(text=f"Result: {result}")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Define the GUI layout
tk.Label(root, text="Select operation:").grid(row=0, column=0, columnspan=2)

operation_var = tk.StringVar(value='8')

tk.Radiobutton(root, text="Add", variable=operation_var, value='1').grid(row=1, column=0, sticky="w")
tk.Radiobutton(root, text="Subtract", variable=operation_var, value='2').grid(row=2, column=0, sticky="w")
tk.Radiobutton(root, text="Multiply", variable=operation_var, value='3').grid(row=3, column=0, sticky="w")
tk.Radiobutton(root, text="Divide", variable=operation_var, value='4').grid(row=4, column=0, sticky="w")
tk.Radiobutton(root, text="Exponentiation", variable=operation_var, value='5').grid(row=5, column=0, sticky="w")
tk.Radiobutton(root, text="Square root", variable=operation_var, value='6').grid(row=6, column=0, sticky="w")
tk.Radiobutton(root, text="Trigonometric functions", variable=operation_var, value='7').grid(row=7, column=0,
                                                                                             sticky="w")
tk.Radiobutton(root, text="Quit", variable=operation_var, value='8').grid(row=8, column=0, sticky="w")

tk.Label(root, text="First number:").grid(row=0, column=2)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=1, column=2)

tk.Label(root, text="Second number:").grid(row=2, column=2)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=3, column=2)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=2)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=5, column=2, columnspan=2)

# Run the GUI loop
root.mainloop()
