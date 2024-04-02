import tkinter as Tkinter
from datetime import datetime

time_elapsed = 0  # Tracks the elapsed time
is_running = False  # State of the stopwatch

def update_timer(label):
    """
    Update the timer label in the stopwatch GUI.
    """
    def count():
        if is_running:
            global time_elapsed
            # To manage the initial delay.
            if time_elapsed == 0:
                display = 'Ready!'
            else:
                tt = datetime.utcfromtimestamp(time_elapsed)
                display = tt.strftime('%H:%M:%S')
    
            label['text'] = display
    
            # Schedule the count function to be called after 1 second
            label.after(1000, count)
            time_elapsed += 1
    
    count()  # Triggering the start of the counter.

def start_timer(label):
    """
    Start the stopwatch.
    """
    global is_running
    is_running = True
    update_timer(label)
    start_btn['state'] = 'disabled'
    stop_btn['state'] = 'normal'
    reset_btn['state'] = 'normal'

def stop_timer():
    """
    Stop the stopwatch.
    """
    global is_running
    is_running = False
    start_btn['state'] = 'normal'
    stop_btn['state'] = 'disabled'
    reset_btn['state'] = 'normal'

def reset_timer(label):
    """
    Reset the stopwatch.
    """
    global time_elapsed
    time_elapsed = 0
    if not is_running:
        reset_btn['state'] = 'disabled'
        label['text'] = '00:00:00'
    else:
        label['text'] = '00:00:00'

root = Tkinter.Tk()
root.title("Stopwatch")

# Setting up the GUI
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text='Ready!', fg='black', font='Verdana 30 bold')
label.pack()

# Creating buttons for starting, stopping, and resetting the stopwatch
f = Tkinter.Frame(root)
start_btn = Tkinter.Button(f, text='Start', width=6, command=lambda: start_timer(label))
stop_btn = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=stop_timer)
reset_btn = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: reset_timer(label))

f.pack(anchor='center', pady=5)
start_btn.pack(side='left')
stop_btn.pack(side='left')
reset_btn.pack(side='left')

root.mainloop()
