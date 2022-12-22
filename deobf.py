# scripted by Vaimsamay 
# design credits : vaimpier ritik 
# Norification for doing constant work ! 
# Cybok Hackers
# Cybok Wars 


# -----------------------imports 
try:
   from os import system,name
   from time import sleep
   from gtts import gTTS
   from plyer import notification
   from colorama import Fore
   import os
   import sys
except Exception as samay:
    try:
       system(\'pip install gtts\')
       system(\'pip install plyer\')
       system(\'pip install colorama\')
    except:
        print(\'\
\')
        print("\xe2\x94\x94\xe2\x94\x80"+"Please Check Your Internet Connection !  ")
        print(\'\
\')
        sleep(1.9)
        sys.exit()


#-----------------------------Colors

r = "\\033[1;31m"
g = "\\033[1;32m"
y = "\\033[1;33m"
b = "\\033[1;34m"
d = "\\033[2;37m"
R = "\\033[1;41m"
Y = "\\033[1;43m"
B = "\\033[1;44m"
w = "\\033[1;37m"

# ----------------requirements installation ! 


def makemkdir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
makemkdir(\'Config\')


#-------------------------------------banner

logo = """\\033[1;37m

\\033[1;37m[!] \\033[1;31mThis is use for Notification Maker, You can Unlimitedly Edit !!! BYE :_)
\\033[1;37m
\xe2\x94\x8c-=============================   -   
=      \\033[1;31m . \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80 \\033[1;37mVaim-Samay    -   
=  \\033[1;31m .\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80  \\033[1;37mB-Hat Samay            -   \\033[34m[\xe2\x9c\x94]     https://github.com/samay825        [\xe2\x9c\x94]
\\033[1;37m=    Notificaton-maker - Pro          -   \\033[34m[\xe2\x9c\x94]            Version 2.0                 [\xe2\x9c\x94]
\\033[1;37m= \\033[1;31m . \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80 \\033[1;37mBY Samay               -   \\033[91m[X] Please Don\'t Use For illegal Activity  [X]
\\033[1;37m= \\033[1;31m .     \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80 \\033[1;37mVERSION 2.0         -
\\033[1;37m\xe2\x94\x94-=============================   -

\\033[1;31m    
Disclaimer: \\033[1;32mthis tool is designed for Prank
\t    testing in an authorized simulated cyberattack
\t    Attacking targets without prior mutual consent
            is illegal!                                                               
\\033[1;37m                                    
\\033[97m """

#--------------------------About me function ! 
def bye():
\tos.system("clear")
\tbanner()
\tstring = """ 
\t\\033[1;37mDeveloper  \\033[1;34m: \\033[1;31mVAIM-SAMAY

\t\\033[1;37mGithub     \\033[1;34m: \\033[1;31msamay825 & vaimpier_ritik

\t\\033[1;37mInstagram  \\033[1;34m: \\033[1;31mcyboksamay & vaimpier_ritik

\t\\033[1;37mE-mail     \\033[1;34m: \\033[1;31mcybokhackers@gmail.com
\t"""
\tfor letter in string:
\t  sleep(0.01) 
\t  sys.stdout.write(letter)
\t  sys.stdout.flush()
\tprint("\
")

#-------------------------------------banner and tiny functions 
def funcmain(value):
    with open(\'Config/vaimsamay.txt\',\'r\') as samay:
        data = samay.readlines()
    samay_database = {}
    for i in data:
        cer = i.split(\'\\t\')
        samay_database[cer[0]] = cer[1]
    split_keys_database = {x.translate({32:None}) :y
       for x,y in samay_database.items()}
    return split_keys_database[value]
#--------------------------------------Runfile 

def runfile():
    with open(\'index.txt\',\'r\') as f:
        data = f.read()
    return data

# --------------------------------------system clear try for windows exceution ! 
def systemclear():
    if name==\'nt\':
        _ = system(\'cls\')
    else:
        _ = system(\'clear\')



def banner():
    print(logo)

def space():
    print(\'\
\')

def options():
    systemclear()
    banner()
    space()
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 1 ] Notification Maker : ")
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 2 ] Update : ")
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 3 ] About me : ")
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 4 ] Exit : ")
    space()
options()

#-------------------------------- object oriented programming ! 

class Vrushabh:
    def __init__(self,user_input):   
        self.user_input = user_input  
    def Options_Function(self):
        systemclear()
        banner()
        try:
            if self.user_input==1:
                space()
                self.title = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Title of Notification :  "+r)
                space()
                try:
                   self.icon = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Image Path to Set in Notification (optional) :  "+r)  
                except:
                    pass
                space()
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mSaving Configs You Made Almost Ready !  ")
                space()
                sleep(2)
                systemclear()
                banner()
                space()
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 1 ] Hindi Girl : ")
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 2 ] English Girl : ")
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 3 ] Marathi Girl : ")
                space()
                try:
                   self.lund = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Available Voice Pack Which You Want :  "+r))
                   if self.lund==1:
                       save = funcmain(\'hindi\')
                   elif self.lund==2:
                       save = funcmain(\'english\')
                   else:
                       save = funcmain(\'marathi\')  

                except Exception as vaimsamay:
                    print(\'\
\')
                    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mPlease Enter Number not letters fool !  ")
                    print(\'\
\')
                    sleep(1.9)
                    system(\'python main.py\')
                try:
                    self.timehour = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Minutes to Remind  :  "+r))
                except Exception as vaimsamaymandirbichari:
                    print(\'\
\')
                    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mPlease Enter Number not letters fool !  ")
                    print(\'\
\')
                    sleep(1.9)
                    system(\'python main.py\')
                sum_count = 1
                while True:
                    notification.notify(
                        title=f\'{self.title}\',
                        message=f\'{runfile()}\',
                        app_icon=f\'{self.icon}\',
                        timeout=15,
                     )
                    os.system(\'mpg123 Config/v.mp3\')
                    text_samay = runfile()
                    language = save
                    samayobject = gTTS(text=text_samay ,lang=language ,slow=False)
                    samayobject.save(\'Config/play.mp3\')
                    os.system(\'mpg123 Config/play.mp3\')
                    system(\'clear\')
                    banner()
                    space()
                    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"Running"+r+g+f" [ "+r+f"{sum_count}"+g+" ]"+w+" Minutes Over See Notification !")
                    space()
                    secs = (self.timehour * 60)
                    sleep(secs)
                    sum_count += 1
                    
            elif self.user_input==2:
                system(\'python update.py\')
            elif self.user_input==3:
                bye()
            else:
                sys.exit()             
        except Exception as vaimsamaymandirbikhari:
            pass
try:
   samay_user_input = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Desire Option :  "+r))  
except Exception as vaimsamaymandirbikhari:
    print(\'\
\')
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mPlease Enter number not letters fool !   ")
    print(\'\
\')
    sleep(1.9)
    system(\'python main.py\')
if __name__ == \'__main__\':
    samay = Vrushabh(samay_user_input)
    samay.Options_Function()

        
    
    
# scripted by Vaimsamay 
# design credits : vaimpier ritik 
# Norification for doing constant work ! 
# Cybok Hackers
# Cybok Wars 


# -----------------------imports 
try:
   from os import system,name
   from time import sleep
   from gtts import gTTS
   from plyer import notification
   from colorama import Fore
   import os
   import sys
except Exception as samay:
    try:
       system(\'pip install gtts\')
       system(\'pip install plyer\')
       system(\'pip install colorama\')
    except:
        print(\'\
\')
        print("\xe2\x94\x94\xe2\x94\x80"+"Please Check Your Internet Connection !  ")
        print(\'\
\')
        sleep(1.9)
        sys.exit()


#-----------------------------Colors

r = "\\033[1;31m"
g = "\\033[1;32m"
y = "\\033[1;33m"
b = "\\033[1;34m"
d = "\\033[2;37m"
R = "\\033[1;41m"
Y = "\\033[1;43m"
B = "\\033[1;44m"
w = "\\033[1;37m"

# ----------------requirements installation ! 


def makemkdir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
makemkdir(\'Config\')


#-------------------------------------banner

logo = """\\033[1;37m

\\033[1;37m[!] \\033[1;31mThis is use for Notification Maker, You can Unlimitedly Edit !!! BYE :_)
\\033[1;37m
\xe2\x94\x8c-=============================   -   
=      \\033[1;31m . \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80 \\033[1;37mVaim-Samay    -   
=  \\033[1;31m .\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80  \\033[1;37mB-Hat Samay            -   \\033[34m[\xe2\x9c\x94]     https://github.com/samay825        [\xe2\x9c\x94]
\\033[1;37m=    Notificaton-maker - Pro          -   \\033[34m[\xe2\x9c\x94]            Version 2.0                 [\xe2\x9c\x94]
\\033[1;37m= \\033[1;31m . \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80 \\033[1;37mBY Samay               -   \\033[91m[X] Please Don\'t Use For illegal Activity  [X]
\\033[1;37m= \\033[1;31m .     \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80 \\033[1;37mVERSION 2.0         -
\\033[1;37m\xe2\x94\x94-=============================   -

\\033[1;31m    
Disclaimer: \\033[1;32mthis tool is designed for Prank
\t    testing in an authorized simulated cyberattack
\t    Attacking targets without prior mutual consent
            is illegal!                                                               
\\033[1;37m                                    
\\033[97m """

#--------------------------About me function ! 
def bye():
\tos.system("clear")
\tbanner()
\tstring = """ 
\t\\033[1;37mDeveloper  \\033[1;34m: \\033[1;31mVAIM-SAMAY

\t\\033[1;37mGithub     \\033[1;34m: \\033[1;31msamay825 & vaimpier_ritik

\t\\033[1;37mInstagram  \\033[1;34m: \\033[1;31mcyboksamay & vaimpier_ritik

\t\\033[1;37mE-mail     \\033[1;34m: \\033[1;31mcybokhackers@gmail.com
\t"""
\tfor letter in string:
\t  sleep(0.01) 
\t  sys.stdout.write(letter)
\t  sys.stdout.flush()
\tprint("\
")

#-------------------------------------banner and tiny functions 
def funcmain(value):
    with open(\'Config/vaimsamay.txt\',\'r\') as samay:
        data = samay.readlines()
    samay_database = {}
    for i in data:
        cer = i.split(\'\\t\')
        samay_database[cer[0]] = cer[1]
    split_keys_database = {x.translate({32:None}) :y
       for x,y in samay_database.items()}
    return split_keys_database[value]
#--------------------------------------Runfile 

def runfile():
    with open(\'index.txt\',\'r\') as f:
        data = f.read()
    return data

# --------------------------------------system clear try for windows exceution ! 
def systemclear():
    if name==\'nt\':
        _ = system(\'cls\')
    else:
        _ = system(\'clear\')



def banner():
    print(logo)

def space():
    print(\'\
\')

def options():
    systemclear()
    banner()
    space()
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 1 ] Notification Maker : ")
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 2 ] Update : ")
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 3 ] About me : ")
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 4 ] Exit : ")
    space()
options()

#-------------------------------- object oriented programming ! 

class Vrushabh:
    def __init__(self,user_input):   
        self.user_input = user_input  
    def Options_Function(self):
        systemclear()
        banner()
        try:
            if self.user_input==1:
                space()
                self.title = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Title of Notification :  "+r)
                space()
                try:
                   self.icon = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Image Path to Set in Notification (optional) :  "+r)  
                except:
                    pass
                space()
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mSaving Configs You Made Almost Ready !  ")
                space()
                sleep(2)
                systemclear()
                banner()
                space()
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 1 ] Hindi Girl : ")
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 2 ] English Girl : ")
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 3 ] Marathi Girl : ")
                space()
                try:
                   self.lund = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Available Voice Pack Which You Want :  "+r))
                   if self.lund==1:
                       save = funcmain(\'hindi\')
                   elif self.lund==2:
                       save = funcmain(\'english\')
                   else:
                       save = funcmain(\'marathi\')  

                except Exception as vaimsamay:
                    print(\'\
\')
                    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mPlease Enter Number not letters fool !  ")
                    print(\'\
\')
                    sleep(1.9)
                    system(\'python main.py\')
                try:
                    self.timehour = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Minutes to Remind  :  "+r))
                except Exception as vaimsamaymandirbichari:
                    print(\'\
\')
                    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mPlease Enter Number not letters fool !  ")
                    print(\'\
\')
                    sleep(1.9)
                    system(\'python main.py\')
                sum_count = 1
                while True:
                    notification.notify(
                        title=f\'{self.title}\',
                        message=f\'{runfile()}\',
                        app_icon=f\'{self.icon}\',
                        timeout=15,
                     )
                    os.system(\'mpg123 Config/v.mp3\')
                    text_samay = runfile()
                    language = save
                    samayobject = gTTS(text=text_samay ,lang=language ,slow=False)
                    samayobject.save(\'Config/play.mp3\')
                    os.system(\'mpg123 Config/play.mp3\')
                    system(\'clear\')
                    banner()
                    space()
                    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"Running"+r+g+f" [ "+r+f"{sum_count}"+g+" ]"+w+" Minutes Over See Notification !")
                    space()
                    secs = (self.timehour * 60)
                    sleep(secs)
                    sum_count += 1
                    
            elif self.user_input==2:
                system(\'python update.py\')
            elif self.user_input==3:
                bye()
            else:
                sys.exit()             
        except Exception as vaimsamaymandirbikhari:
            pass
try:
   samay_user_input = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Desire Option :  "+r))  
except Exception as vaimsamaymandirbikhari:
    print(\'\
\')
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mPlease Enter number not letters fool !   ")
    print(\'\
\')
    sleep(1.9)
    system(\'python main.py\')
if __name__ == \'__main__\':
    samay = Vrushabh(samay_user_input)
    samay.Options_Function()

        
    
    
# scripted by Vaimsamay 
# design credits : vaimpier ritik 
# Norification for doing constant work ! 
# Cybok Hackers
# Cybok Wars 


# -----------------------imports 
try:
   from os import system,name
   from time import sleep
   from gtts import gTTS
   from plyer import notification
   from colorama import Fore
   import os
   import sys
except Exception as samay:
    try:
       system(\'pip install gtts\')
       system(\'pip install plyer\')
       system(\'pip install colorama\')
    except:
        print(\'\
\')
        print("\xe2\x94\x94\xe2\x94\x80"+"Please Check Your Internet Connection !  ")
        print(\'\
\')
        sleep(1.9)
        sys.exit()


#-----------------------------Colors

r = "\\033[1;31m"
g = "\\033[1;32m"
y = "\\033[1;33m"
b = "\\033[1;34m"
d = "\\033[2;37m"
R = "\\033[1;41m"
Y = "\\033[1;43m"
B = "\\033[1;44m"
w = "\\033[1;37m"

# ----------------requirements installation ! 


def makemkdir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
makemkdir(\'Config\')


#-------------------------------------banner

logo = """\\033[1;37m

\\033[1;37m[!] \\033[1;31mThis is use for Notification Maker, You can Unlimitedly Edit !!! BYE :_)
\\033[1;37m
\xe2\x94\x8c-=============================   -   
=      \\033[1;31m . \xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80 \\033[1;37mVaim-Samay    -   
=  \\033[1;31m .\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80  \\033[1;37mB-Hat Samay            -   \\033[34m[\xe2\x9c\x94]     https://github.com/samay825        [\xe2\x9c\x94]
\\033[1;37m=    Notificaton-maker - Pro          -   \\033[34m[\xe2\x9c\x94]            Version 2.0                 [\xe2\x9c\x94]
\\033[1;37m= \\033[1;31m . \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80 \\033[1;37mBY Samay               -   \\033[91m[X] Please Don\'t Use For illegal Activity  [X]
\\033[1;37m= \\033[1;31m .     \xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80 \\033[1;37mVERSION 2.0         -
\\033[1;37m\xe2\x94\x94-=============================   -

\\033[1;31m    
Disclaimer: \\033[1;32mthis tool is designed for Prank
\t    testing in an authorized simulated cyberattack
\t    Attacking targets without prior mutual consent
            is illegal!                                                               
\\033[1;37m                                    
\\033[97m """

#--------------------------About me function ! 
def bye():
\tos.system("clear")
\tbanner()
\tstring = """ 
\t\\033[1;37mDeveloper  \\033[1;34m: \\033[1;31mVAIM-SAMAY

\t\\033[1;37mGithub     \\033[1;34m: \\033[1;31msamay825 & vaimpier_ritik

\t\\033[1;37mInstagram  \\033[1;34m: \\033[1;31mcyboksamay & vaimpier_ritik

\t\\033[1;37mE-mail     \\033[1;34m: \\033[1;31mcybokhackers@gmail.com
\t"""
\tfor letter in string:
\t  sleep(0.01) 
\t  sys.stdout.write(letter)
\t  sys.stdout.flush()
\tprint("\
")

#-------------------------------------banner and tiny functions 
def funcmain(value):
    with open(\'Config/vaimsamay.txt\',\'r\') as samay:
        data = samay.readlines()
    samay_database = {}
    for i in data:
        cer = i.split(\'\\t\')
        samay_database[cer[0]] = cer[1]
    split_keys_database = {x.translate({32:None}) :y
       for x,y in samay_database.items()}
    return split_keys_database[value]
#--------------------------------------Runfile 

def runfile():
    with open(\'index.txt\',\'r\') as f:
        data = f.read()
    return data

# --------------------------------------system clear try for windows exceution ! 
def systemclear():
    if name==\'nt\':
        _ = system(\'cls\')
    else:
        _ = system(\'clear\')



def banner():
    print(logo)

def space():
    print(\'\
\')

def options():
    systemclear()
    banner()
    space()
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 1 ] Notification Maker : ")
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 2 ] Update : ")
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 3 ] About me : ")
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 4 ] Exit : ")
    space()
options()

#-------------------------------- object oriented programming ! 

class Vrushabh:
    def __init__(self,user_input):   
        self.user_input = user_input  
    def Options_Function(self):
        systemclear()
        banner()
        try:
            if self.user_input==1:
                space()
                self.title = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Title of Notification :  "+r)
                space()
                try:
                   self.icon = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Image Path to Set in Notification (optional) :  "+r)  
                except:
                    pass
                space()
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mSaving Configs You Made Almost Ready !  ")
                space()
                sleep(2)
                systemclear()
                banner()
                space()
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 1 ] Hindi Girl : ")
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 2 ] English Girl : ")
                print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 3 ] Marathi Girl : ")
                space()
                try:
                   self.lund = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Available Voice Pack Which You Want :  "+r))
                   if self.lund==1:
                       save = funcmain(\'hindi\')
                   elif self.lund==2:
                       save = funcmain(\'english\')
                   else:
                       save = funcmain(\'marathi\')  

                except Exception as vaimsamay:
                    print(\'\
\')
                    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mPlease Enter Number not letters fool !  ")
                    print(\'\
\')
                    sleep(1.9)
                    system(\'python main.py\')
                try:
                    self.timehour = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Minutes to Remind  :  "+r))
                except Exception as vaimsamaymandirbichari:
                    print(\'\
\')
                    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mPlease Enter Number not letters fool !  ")
                    print(\'\
\')
                    sleep(1.9)
                    system(\'python main.py\')
                sum_count = 1
                while True:
                    notification.notify(
                        title=f\'{self.title}\',
                        message=f\'{runfile()}\',
                        app_icon=f\'{self.icon}\',
                        timeout=15,
                     )
                    os.system(\'mpg123 Config/v.mp3\')
                    text_samay = runfile()
                    language = save
                    samayobject = gTTS(text=text_samay ,lang=language ,slow=False)
                    samayobject.save(\'Config/play.mp3\')
                    os.system(\'mpg123 Config/play.mp3\')
                    system(\'clear\')
                    banner()
                    space()
                    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"Running"+r+g+f" [ "+r+f"{sum_count}"+g+" ]"+w+" Minutes Over See Notification !")
                    space()
                    secs = (self.timehour * 60)
                    sleep(secs)
                    sum_count += 1
                    
            elif self.user_input==2:
                system(\'python update.py\')
            elif self.user_input==3:
                bye()
            else:
                sys.exit()             
        except Exception as vaimsamaymandirbikhari:
            pass
try:
   samay_user_input = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter Desire Option :  "+r))  
except Exception as vaimsamaymandirbikhari:
    print(\'\
\')
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mPlease Enter number not letters fool !   ")
    print(\'\
\')
    sleep(1.9)
    system(\'python main.py\')
if __name__ == \'__main__\':
    samay = Vrushabh(samay_user_input)
    samay.Options_Function()

        
    
    

\'\'\'













# Anonymous Coders 
# scripted by shark and samay 
# design : vaimpier ritik 
# modules -----

#-----------------------imports 
try:
   import os 
   import sys
   import requests
   import random
   import string
   import threading
   from os import system,name
   from requests import get
   from time import sleep
   from colorama import Fore
except Exception as samay:
    _ = system(\'pip install requests\')
    _ = system(\'pip install colorama\')
    

#---------------------colors 
r = "\\033[1;31m"
g = "\\033[1;32m"
y = "\\033[1;33m"
b = "\\033[1;34m"
d = "\\033[2;37m"
R = "\\033[1;41m"
Y = "\\033[1;43m"
B = "\\033[1;44m"
w = "\\033[1;37m"
g = "\\033[0;90m"
gg = "\\033[1;32m"
y = r

#---------------------------banners and programs 

#----------------------clear function for windows and linux
def clear():
    system(\'cls\' if name==\'nt\' else \'clear\')

# clear function!
def space():
    print(\'\
\')

# ----------------------------------banner 
def banner():
    print(y+y+"               ) ")
    print(w+y+"              (( ")
    print(w+y+"              ) \\ ")
    print(w+y+"            (   ) ") 
    print(w+y+"            (  )  ) ") 
    print(w+y+"            ) (  ( \\ ")
    print(w+y+"          (   )$ )  ) ")
    print(w+y+"          ($$  ( \\   )           ")
    print(w+b+"    ^^^^^"+w+g+",r@@@@@@@@@@e,"+w+b+"^^^^^^   \xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/")
    print(w+b+"      ^^^"+w+g+"@@@@@@@@@@@@@@@@"+w+b+"^^^    "+w+b+"Email Spam ( Pro ) - version 1.0             /")
    print(w+g+"      \\@@/"+r+",:::,"+w+g+"\\/"+r+",:::,"+w+g+"\\@@       "+w+"\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/")
    print(w+g+"     /@@@|"+r+":::::"+w+g+"||"+r+":::::"+w+g+"|@@@\\\\     "+w+"Author by "+y+"@Sh2rk @VaimZork                 /")
    print(w+g+"    / @@@\\\\"+r+"\':::\'"+w+g+"/\\\\"+r+"\':::\'"+w+g+"/@@@ \\\\    "+w+"The author is not responsible             /")
    print(w+g+"   /  /@@@@@@@//\\\\\\@@@@@@@\\  \\\\   "+w+"for any issues or damage                 /")
    print(w+g+"  (  /  \'@@@@@====@@@@@\'  \\  )  "+w+"caused by this program                  /")
    print(w+g+"   \\(     /          \\     )/ "+"\\033[1;33m  \xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/")
    print(w+g+"     \\   (            )   /")
    print(w+g+"          \\          /"+w)

#----------------------------------bye function @
def bye():
\tsystem(\'cls\' if name==\'nt\' else \'clear\')
\tbanner()
\tstring = """ 
\t\\033[1;37mDeveloper  \\033[1;34m: \\033[1;31mShark-VaimSamay

\t\\033[1;37mGithub     \\033[1;34m: \\033[1;31m@Vaimpierritik @Samay825

\t\\033[1;37mInstagram     \\033[1;34m: \\033[1;31m@el._samay @vaimpier_ritik @travazapping
\t"""
\tfor letter in string:
\t  sleep(0.01) 
\t  sys.stdout.write(letter)
\t  sys.stdout.flush()
\tprint("\
")

#-------------------------open file ip 
try:
   with open(\'sincryption.txt\',\'w\') as samay:
       samay.write(get(\'https://api.ipify.org\').text)
except:
    space()
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mPlease Check Your Internet Connection !")
    space()
    sys.exit()
#-----------------------------password encyption
clear()
banner()
space()
samay_user = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the private key :  "+r)
def password(samay):
    if samay==get(\'https://api.ipify.org\').text + "sincryption":
        return True
    else:
        return False
ops = password(samay_user)
if ops:
    pass
else:
    while True:
        space()
        print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mWrong Key ! ")
        space()
        sleep(0.5)
        sys.exit()
        break

#------------------------------excute

clear()
banner()
space()
print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 1 ] Email Spam : ")
print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 2 ] About us  : ")
print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m[ 3 ] Exit : ")
space()
try:
    samay_user = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Desire Option : "+r))
except Exception as samay:
    pass
if samay_user==1:
    clear()
    banner()
    space()
    email = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Email Address : "+r)
    msg = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Message : "+r)
    space()
    clear()
    banner()
    space()
    print(b+\'|\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/\'+r)
    print(gg+\'|                  Spamming                   /\')
    print(b+\'|\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/\'+gg)
    space()
    print(Fore.BLUE+"     Maxspeed = 20 ")
    space()
    se = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Speed :  "+r))
    space()
    clear()
    banner()
    space()
    print(b+\'|\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/\'+r)
    print(gg+\'|                  Spamming started...        /\')
    print(b+\'|\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/\'+gg)
    space()
    if se>20:
        sys.exit()

elif samay_user==3:
    space()
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mExiting...  "+r)
    space()
    sleep(0.3)
    sys.exit()

elif samay_user==2:
    bye()
    space()
    sleep(0.9)
    sys.exit()


def spam():
    sum = 1
    while 1:
        try:
            word = msg+\'                        \'
            chars = \'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\'
            for i in range(30):
                word += random.choice(chars)

            data = {
                \'uploader_email\': email,
                \'accept_tos\': 1,
                \'original_filename\': word,
                \'file_path\': \'/mnt/filehosting/21/files/1/5/f/15ffb040ce6abd6e\',
                \'file_size\': \'13650\',
                \'file_type\': \'text/plain\'
            }
            r = requests.post(\'https://www.filehosting.org/file/upload\', data=data).status_code
            if r == 200:
                print(Fore.RED+f\'\xe2\x94\x94\xe2\x94\x80 \'+Fore.GREEN+f\'Spammed Successfully \'+Fore.RED+f\'{sum}\')
                sum += 1
             
            else:
                print(Fore.BLUE+f\'\xe2\x94\x94\xe2\x94\x80 \'+Fore.RED+f\'Bad Request !\')
            
        except:
            print(\' To much requests!\')
            pass
            
       

for i in range(se):
    t = threading.Thread(target=spam)
    t.start()
