import os, time, subprocess
from os import system, name

global passcode 
passcode = "0"
information_1 = ""
lineArray = [5]
overridePW = "POC ONLY"
with open("sys.txt") as file_in:
        lines = []
        for line in file_in:
                #print(line)
                lineArray.append(line)  
        #print(len(lineArray))


terminal_number = lineArray[1]
terminal_number = terminal_number[0]
passcode = lineArray[3]
#print(passcode)
information_1 = lineArray[5]
def clearCMD() -> None:
    try:
        if name != 'nt':
                os.system('clear')
        else:
                os.system('cls')
    except:
        # For Windows
        os.system('cls')

clearCMD()

def loop() -> str:
        print("\n Terminal Number " + terminal_number + " Access Restricted.\n")
        print(" Enter Passcode to continue! ")
        text = input(" Password: ")
        text = text + "\n"
        clearCMD()
        return text
    
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(" ",timer, end="\r")  # Overwrite the previous line
        time.sleep(1)
        t -= 1

def main() -> None:
        out = loop()
        #passcode = passcode
        while(out != passcode):
                out = loop()

        #print("\n Information retrival\n")
        print("\n Information retrival\n")
        countdown(int(2))
        clearCMD()
        print("\n \n Data Uplink\n")
        countdown(int(2))
        clearCMD()
        print("\n TOP SECRET INFO\n")
              
        for i in range(5, len(lineArray)):
                information_1 = lineArray[i]
                print(" " + information_1)

        print(" TOP SECRET  \n")

                #print(" Proceded to terminal #2 for further instructions.\n")
        print(" Warning this message will self destruct in 30s\n")
        countdown(int(30))
        clearCMD()     
 

main()


