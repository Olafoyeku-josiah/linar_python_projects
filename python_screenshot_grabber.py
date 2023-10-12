
import pyautogui
import time
from tkinter import filedialog

def take_screenshot(file_path):
    screenshot = pyautogui.screenshot(file_path)
    return screenshot
    #screenshot.save(file_name)

def intro():
    global user_name
    user_name=input(" Pls enter your name: ")
    print("Hello {} ,This program is designed to take a screenshot of your screen ".format(user_name))
intro()

def main():
    user_choice1=input(" would you like to take a screenshot? enter either(yes or no): ")
    if user_choice1=="yes":
        print(" Dear {} ,This program allows you to take a screenshot of the screen and saves it as a png file \n Press 'ok' to take a screenshot...".format(user_name))
        if pyautogui.confirm(" Dear {} ,This program allows you to take a screenshot of the screen and saves it as a png file \n Press 'ok' to take a screenshot...".format(user_name)) == "OK":
            time.sleep(4)
            take_screenshot(file_path=filedialog.asksaveasfilename(defaultextension=".png"))
            print("Screenshot already saved in the file path specified")
    
main()