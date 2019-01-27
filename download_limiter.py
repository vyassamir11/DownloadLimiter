"""
Script written by Samir Vyas to limit his data usage while downloading
through his Jio internet.
Run it from administrative command prompt as it requires admin privilege.
First argument is data limit in MB and the second argument is time period of update in seconds
"""
import sys
import psutil
import winsound
import os
import time
import tkinter as tk
 

# cd C:\Users\vyass\Desktop
def alert(title, message):
    box = tk.Tk()
    box.title(title)
    tk.Message(box, text=message, bg='red',
      fg='ivory').pack(padx=1, pady=1)
    tk.Button(box, text="Close", command=box.destroy)
    box.geometry('100x150')
    box.after(10000, shutdown)
    box.lift()
    box.attributes('-topmost',True)
    box.mainloop()

def show_cursor(t):
    """ shows rotatnig cursor for t seconds"""
    chars = ['-','|','/','\\','|','-']
    for i in range(int(t/0.1)):
        sys.stdout.write('\r'+chars[i%len(chars)])
        sys.stdout.flush()
        time.sleep(0.1)
        
    
def foo():
    global timeout,limit_mb
    limit = limit_mb*1024*1024
    """
    os.system('powershell.exe netstat -e > usage.txt')
    f = open('usage.txt')
    init = int(f.readlines()[4].strip().split()[1])
    f.close()
    """
    init = psutil.net_io_counters(pernic=True)['Wi-Fi'][1]

    while True:
        """
        os.system('powershell.exe netstat -e > usage.txt')
        f = open('usage.txt')
        curr = int(f.readlines()[4].strip().split()[1])
        f.close()
        """
        curr = psutil.net_io_counters(pernic=True)['Wi-Fi'][1]
        if (curr-init) > limit:
            break
        else:
            sys.stdout.write('\r'+str((limit-curr+init)/(1024*1024))+ " MB remaining\n")
            sys.stdout.flush()
            show_cursor(timeout)
    winsound.Beep(800,1000)
    time.sleep(1)
    winsound.Beep(800,1000)
    time.sleep(1)
    winsound.Beep(800,1000)
    time.sleep(1)
    alert('See this BRO!','Shutdown initiated in 10 seconds.\n Close this to cancel the shutdown')    

def shutdown():
    print('Shutting down...')
    os.system('powershell.exe shutdown /s')
    
if __name__ == "__main__":
    limit_mb = int(input('Enter the data limit in MB.\n'))
    timeout = int(input('Enter the refresh time in seconds.\n'))
    print("Runnig the script with ",limit_mb," MB limit and ",timeout," seconds of update period.")
    foo()
    
    
    
