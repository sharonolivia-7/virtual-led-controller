led_controller.py
import tkinter as tk

# Function to toggle LED state
def toggle_led():
    global led_state
    led_state = not led_state
    led_label.config(text="LED ON" if led_state else "LED OFF", fg="green" if led_state else "red")

# Initialize GUI
root = tk.Tk()
root.title("Virtual LED Controller")
root.geometry("300x200")

led_state = False  # LED is initially OFF

# LED Status Label
led_label = tk.Label(root, text="LED OFF", font=("Arial", 16), fg="red")
led_label.pack(pady=20)

# Toggle Button
toggle_button = tk.Button(root, text="Toggle LED", font=("Arial", 14), command=toggle_led)
toggle_button.pack()

# Run the GUI
root.mainloop()
