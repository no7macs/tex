import time
import random
import urllib.request
import ssl
import urllib
import webbrowser
import pyautogui
import csv

print("")
print("'########::::::'########::::::'##::::'##::::'##:::::::::::::::'#####:::")
print("... ##..::::::: ##.....:::::::. ##::'##::::: ##:::'##::::::::'##.. ##::")
print("::: ##::::::::: ##:::::::::::::. ##'##:::::: ##::: ##:::::::'##:::: ##:")
print("::: ##::::::::: ######::::::::::. ###::::::: ##::: ##::::::: ##:::: ##:")
print("::: ##::::::::: ##...::::::::::: ## ##:::::: #########:::::: ##:::: ##:")
print("::: ##::::'###: ##:::::::'###:: ##:. ##:::::...... ##::'###:. ##:: ##::")
print("::: ##:::: ###: ########: ###: ##:::. ##:::::::::: ##:: ###::. #####:::")
print(":::..:::::...::........::...::..:::::..:::::::::::..:::...::::.....::::")  
print("")
time.sleep(0.5)
print("")
print("'########::'##:::'##::::'##::: ##::'#######::'########:'##::::'##::::'###:::::'######::")
print(" ##.... ##:. ##:'##::::: ###:: ##:'##.... ##: ##..  ##: ###::'###:::'## ##:::'##... ##:")
print(" ##:::: ##::. ####:::::: ####: ##: ##:::: ##:..:: ##::: ####'####::'##:. ##:: ##:::..::")
print(" ########::::. ##::::::: ## ## ##: ##:::: ##:::: ##:::: ## ### ##:'##:::. ##: ##:::::::")
print(" ##.... ##:::: ##::::::: ##. ####: ##:::: ##::: ##::::: ##. #: ##: #########: ##:::::::")
print(" ##:::: ##:::: ##::::::: ##:. ###: ##:::: ##::: ##::::: ##:.:: ##: ##.... ##: ##::: ##:")
print(" ########::::: ##::::::: ##::. ##:. #######:::: ##::::: ##:::: ##: ##:::: ##:. ######::")
print("........::::::..::::::::..::::..:::.......:::::..::::::..:::::..::..:::::..:::......:::")

def Main():
    time.sleep((int(Postdelay)))
    if Ttspreset == "Y":
        pyautogui.typewrite('/tts ')
    elif Ttspreset == "y":
        pyautogui.typewrite('/tts ')
    else:
        print("")

    if Everyonepreset == "Y":
        pyautogui.typewrite('@everyone ')
    elif Everyonepreset == "y":
        pyautogui.typewrite('@everyone ')
    else:
        print("")

    if Herepreset == "Y":
        pyautogui.typewrite('@here ')
    elif Herepreset == "y":
        pyautogui.typewrite('@here ')
    else:
        print("")

    pyautogui.typewrite(Currentmessage)
    pyautogui.press('enter')

    Main()

    
def Options():
    global Postdelay
    global Ttspreset
    global Everyonepreset
    global Herepreset
    global Currentmessagenumber
    
    def Messagemaker():
        global Currentmessage
        Currentmessage = input("What do you want your message to be?:")
        Keepmessagecheck = input("Keep message? Y/N")
        if Keepmessagecheck == "Y":
            Main()
        elif Keepmessagecheck == "y":
            Main()            
        elif Keepmessagecheck == "yes":
            Main()
        elif Keepmessagecheck == "Yes":
            Main()
        else:
            Messagemaker()
            
    print("|--OPTIONS--|")
    Postdelay = input("Delay between posts(MUST BE A NUMBER):")
    Ttspreset = input("Use /tts? Y/N")
    Everyonepreset = input("Use @everyone? Y/N")
    Herepreset = input("Use @here? Y/N")
    Messagemaker()

def Start():
    print("You need a code to enter")
    print("1.Enter Code")
    print("2.Get Code")
    Startcode = input("Select one:")

    if Startcode == "1":
        Actualstartcode = input("Enter Code Here:")
        if Actualstartcode == "KLADISCORDSERVER40001":
            print("CORRECT!")
            Options()
        else:
            print("--INVALID--")
            print("your version migth be outdated, go here to update it: http://bit.ly/2ZEFx6L")
            Start()
    elif Startcode == "2":
        webbrowser.open('https://clk.ink/tex4code')
        Start()
    else:
        print("--INVALID OPTION--")
        Start()        
    time.sleep(1)
Start()
