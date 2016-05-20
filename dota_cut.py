import win32api, win32con
import random, time
import msvcrt

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    
    
#dimensions: width: 270-1270, height: 205-830
def cut_dem_trees():
    w = range(270, 1270)
    h = range(205, 830)
    while(True):
        click(random.choice(w), random.choice(h))
        time.sleep(0.1)
        # Check if `Esc` has been pressed
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            break
if __name__ == "__main__":
    cut_dem_trees()