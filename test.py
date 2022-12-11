import time
import pyautogui

def is_end(x_old, x_new, y_old, y_new):
	return ((x_old-x_new)**2 + (y_old-y_new)**2) < 3

print(pyautogui.__version__)

for i in range(5):
	print(f"get set starts in {5-i}!")
	time.sleep(1)
x_, y_ = pyautogui.position()
x, y = pyautogui.position()
i = 1
while is_end(x_,x,y_,y):
	x, y = pyautogui.position()
	print(f'Clicked for {2*i} times!')
	pyautogui.click(clicks=2, button='left')
#	time.sleep(0.05)
	i += 1
