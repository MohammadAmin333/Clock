import tkinter as tk  
import time  

def update_time():  
    current_time = time.strftime('%H:%M:%S %p')  
    label.config(text=current_time)  
    label.after(1000, update_time)  # update the label every 1 second  

# Create the main window  
root = tk.Tk()  
root.title('Digital Clock')  

# Create a label to display the time  
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')  
label.pack(anchor='center')  

# Start the time update loop  
update_time()  

# Run the application  
root.mainloop()  