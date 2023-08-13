import tkinter as tk
def convert_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{celsius:.2f} Celsius = {fahrenheit:.2f} Fahrenheit")
    except ValueError:
        label_result.config(text="Invalid input!")
# Create the main window
root = tk.Tk()  
root.title("Celsius to Fahrenheit Converter")
# Create labels and entry widgets
label_celsius = tk.Label(root, text="Enter Celsius:")
label_celsius.pack()
entry_celsius = tk.Entry(root)
entry_celsius.pack()
# Create the conversion button
convert_button = tk.Button(root, text="Convert", command=convert_to_fahrenheit)
convert_button.pack()
# Create a label to display the result
label_result = tk.Label(root, text="")
label_result.pack()
# Run the application
root.mainloop()
