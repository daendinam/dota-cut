import win32api, win32con
import random, time
import msvcrt

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
    
#dimensions: width: 270-1270, height: 205-830
def cut_dem_trees():
    width = win32api.GetSystemMetrics(0) 
    height = win32api.GetSystemMetrics(1) 
    w1 = int(width * float(270.0/1920.0) )
    w2 = int(width * float(1270.0/1920.0) ) 
    h1 = int(height * float(205.0/1080.0) )
    h2 = int(height * float(830.0/1080.0) ) 
    w = range(w1, w2)
    h = range(h1, h2)
    while(True):
        click(random.choice(w), random.choice(h))
        time.sleep(0.1)
        # Check if `Esc` has been pressed
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            break
if __name__ == "__main__":
    cut_dem_trees()