import os
import pyttsx3 as s
os.system("cls")
os.system("color b")
os.system("color 84")
while True:  
    print("-----------------------------------------") 
    print("I AM ACE YOUR PERSONAL COMPANION ")
    print("-----------------------------------------") 
    print("please enter your requirement :" ,end=" ")
    x = input() 
    if ("open" in x and "facebook" in x):
        s.speak("opening facebook please wait")
        os.system("start chrome www.facebook.com")
        os.system("cls")
    elif ("open" in x and "github" in x):
        s.speak("opening github please wait")
        os.system("start chrome www.github.com")
        os.system("cls")
    elif ("open" in x and ("notepad" in x or "editor" in x)):
        s.speak("opening text editor please wait")
        os.system("notepad")
        os.system("cls")
    elif 'python' in x:
        s.speak("opening python please wait")
        os.system("python")
        os.system("cls")  
    elif 'winscp' in x:
        s.speak("opening winscp please wait")
        os.system("winscp.exe")
        os.system("cls")
    elif "exit" in x:
        exit()
    else:
        s.speak("Check your spelling and try again")
        print("Check your spelling and try again")
