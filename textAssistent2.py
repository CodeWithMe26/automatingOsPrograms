import os
import webbrowser
def openWebsites():
    print("Enter a url you want to open : ",end=' ')
    url=input().lower
    webbrowser.open_new("url")

while True:
    print(" Enter some text : ",end=' ' )
    str=input().lower()
    if((("google chrome" in str) or ("browser" in str) or ("chrome"in str) or ("internet" in str) or ("web browser" in str) or ("google" in str)) and (("run" in str) or ("open" in str) or ("execute" in str)) and (("website" in str) or ("url" in str) or ("link" in str))):
        openWebsites()

    elif((("google chrome" in str) or ("browser" in str) or ("chrome"in str) or ("internet" in str) or ("web browser" in str) or ("google" in str)) and (("run" in str) or ("open" in str) or ("execute" in str)) and(("not" not in str) and ("do not" not in str) and ("don't" not in str) and ("dont" not in str))):
        os.system("chrome")
    elif (("google chrome" in str) or ("browser" in str) or ("chrome"in str) or ("webbrowser" in str) or ("google" in str)) :
        print("Do you want to use chrome enter y or n :",end=' ')
        inp=input().lower()
        if inp=="y":
            os.system("chrome")
        elif inp=="n":
            print()
            print("call me when you want to use either of 3 \n 1. google chrome \n 2. notepad \n 3. control panel \n Thanks for using me " )
        else :
            break
        
    elif ((("editor" in str) or ("text editor" in str) or ("notepad" in str)) and (("run" in str) or ("open" in str) or ("execute" in str)) and (("not" not in str) and ("do not" not in str) and ("don't" not in str) and ("dont" not in str))):
        os.system("notepad")
    elif (("editor" in str) or ("text editor" in str) or ("notepad" in str)) :
        print("Do you want to use text editor enter y or n :",end=' ')
        inp=input().lower()
        if inp=="y":
            os.system("notepad")
        elif inp=="n":
            print()
            print("call me when you want to use either of 3 \n 1. google chrome \n 2. notepad \n 3. control panel \n Thanks for using me " )
        else :
            break
    
        
    elif((("control panel" in str) or ("panel" in str ) or ("settings" in str ) or ("control" in str))  and (("run" in str) or ("open" in str) or ("execute" in str)) and (("not" not in str) and ("do not" not in str) and ("don't" not in str) and ("dont" not in str))):
        os.system("control panel")
    elif (("control panel" in str) or ("panel" in str ) or ("settings" in str )):
          print("Do you want to use control panel enter y or n :",end=' ')
          inp=input().lower()
          if inp=="y":
              os.system("control panel")
          elif inp=="n":
              print()
              print("call me when you want to use either of 3 \n 1. google chrome \n 2. notepad \n 3. control panel \n Thanks for using me " )
          else :
              break
              
    elif (("exit" in str) or ("quit" in str) or ("shutdown" in str) ) and (("not" not in str) and ("do not" not in str) and ("don't" not in str) and ("dont" not in str)):
        break
    elif (("continue" in str) and (("not"  in str) or ("do not"  in str) or ("don't"  in str) or ("dont"  in str))):
        break
    else:
        print
        print("call me when you want to use either of 3 \n 1. google chrome \n 2. notepad \n 3. control panel \n\n Thanks for using me !! " )



