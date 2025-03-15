Virtual-led-controller
A simple Python GUI-based LED Controller using Tkinter to toggle an LED ON/OFF. Simulates an embedded system switch with real-time UI updates.
Features  
1. Toggle LED ON/OFF using a button  
2. GUI built with Tkinter  
3. Event-driven state management  
4. Simulates embedded systems  

How to Run  
1. Install Python (if not already installed)  
2. Run the following command:
3. Click "Toggle LED" to control the LED state
   
led_controller.py
import tkinter as tk

Function to toggle LED state
def toggle_led():
    global led_state
    led_state = not led_state
    led_label.config(text="LED ON" if led_state else "LED OFF", fg="green" if led_state else "red")

Initialize GUI
root = tk.Tk()
root.title("Virtual LED Controller")
root.geometry("300x200")

led_state = False  # LED is initially OFF

LED Status Label
led_label = tk.Label(root, text="LED OFF", font=("Arial", 16), fg="red")
led_label.pack(pady=20)

Toggle Button
toggle_button = tk.Button(root, text="Toggle LED", font=("Arial", 14), command=toggle_led)
toggle_button.pack()

Run the GUI
root.mainloop()

Screenshots:
![Screenshot 2025-03-15 161339](https://github.com/user-attachments/assets/0ecd7813-57ff-467b-8857-61d2c50aad50)
![Screenshot 2025-03-15 161457](https://github.com/user-attachments/assets/27a0639d-e580-42a3-8937-5b920af9c009)

Author
Kalla Sahron Olivia(https://github.com/sharonolivia-7)
