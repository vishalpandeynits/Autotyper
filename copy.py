import pyautogui
import time

file_name = input("Enter the exact location of file or simply name, if this script and your file exists in same directory.\n")
f = open(file_name,'r')
data = f.read()

print(" Click on the place where you want us to type your data under 3 seconds.")
time.sleep(3)
for i in data:
    pyautogui.typewrite(i)
    time.sleep(0.005)
