# !/usr/bin/python
# __author___= 'Hussam ashraf'
# PasswdLocker.py - basic password locker for keeping important passwords.
# Must run it as Administrator


import shelve as sh
import os, sys, shutil
from colorama import Fore, Style, Back
import time
import pyperclip
import string
import base64
#from Crypto.Cipher import AES
#from Crypto import Random
#import speech_recognition as sr
#import subprocess as sub
import pyttsx3




# get all drives on windows
availableDrives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
drive = availableDrives[1]

# saving the database into another drive than C: drive
dir = os.chdir(drive + "\$Recycle.Bin")
try:
    os.mkdir('passwdLocker')
except:
    pass
try:
    locker = sh.open(r'passwdLocker\database')
except:
    print('Run The Script As Administrator.')
    time.sleep(2)
    sys.exit()

print(Fore.GREEN +
        "####################################################################\n"
        "#       ____                           _ _               _         #\n"  
        "#      |  _ \ __ _ ___ _____      ____| | |    ___   ___| | __     #\n"
        "#      | |_) / _` / __/ __\ \ /\ / / _` | |   / _ \ / __| |/ /     #\n"
        "#      |  __/ (_| \__ \__\ \ V  V / (_| | |__| (_) | (__|   <      #\n"
        "#      |_|   \__,_|___/___/ \_/\_/ \__,_|_____\___/ \___|_|\_\     #\n"
        + Style.RESET_ALL)
print('--------------------------------------------------------------------')
print('-----------------------### Password Locker ###----------------------')

def Main():
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)    

    # Encrypting methods
    # key as a phasephare, it supports multiple keys: 16, 24 or 32
    # using key type 16(AES128)
    global key
    key = b'Sixteen byte key'

    '''
    # encryption method
    def Encrypt(usrPasswords):
        # choose a random 16-byte IV
        iv = Random.new().read(AES.block_size)

        # create AES cipher
        cipher = AES.new(key, AES.MODE_CFB, iv)

        # encrypt using AES
        encodePass = iv + cipher.encrypt(usrPasswords.encode('ascii'))

        # Encrypt the AES with base64
        bs64Pass = base64.b64encode(encodePass)
        return bs64Pass

    # decryption method
    def Decrypt(encrypted):
        # decrypt AES encrypted with base64
        decode64 = base64.b64decode(encrypted)

        # decrypt AES to plaintext
        cipher = AES.new(key, AES.MODE_CFB, decode64[:16])
        decodeAES = cipher.decrypt(decode64[16:])
        return decodeAES
    '''

    ##################################################################
    # start of the script
    # check if username exist 
    if not list(locker.keys()):
        engine.say('hey')
        engine.say('I am Yashi')
        engine.say('Welcome to your first time using password locker')
        engine.say('I will be your personal assistant here')
        engine.say('Okay !!')
        engine.say("Let's start by making a new account for you...")
        engine.say('Don\'t forget')
        engine.say('Call my name if you need me, it\'s Yashi')
        engine.runAndWait()
        
        global signUser
        signUser = input(Fore.BLUE + '::' + Style.RESET_ALL + 'Enter a new username >> ')
        signPass = input(Fore.BLUE + '::' + Style.RESET_ALL + 'Enter your password >> ').encode('ascii')

        # Encrypt password
        signPassEncrypted = base64.b64encode(signPass)
        locker[signUser.lower()] = signPassEncrypted

        data()

    # Log in if user in database
    else:
        print('--------------------------------------------------------------------')
        print(Fore.RED, '                 ########## Logging In ##########', Style.RESET_ALL)
        print()
        mainCounter = 0
        while True:
            global usrName

            usrName = input(Fore.BLUE + '::' + Style.RESET_ALL + 'Enter your username >> ').lower()
            speech = 'hey , Weome back {}'.format(usrName)
            engine.say(speech)
            engine.say('It\'s me again')
            engine.say('Please enter your password')
            engine.runAndWait()
            engine.stop()
            
            if usrName.lower() in locker:
                secCounter = 0
                while True:
                    password = input(Fore.BLUE + '::' + Style.RESET_ALL + 'Enter password for " {} " >> '.format(usrName))

                    # decrypting password from database before matching it.
                    usrNamePass = str(base64.b64decode(locker[usrName]))

                    # matching username and password
                    if usrNamePass[2:-1] == password:
                        print(Fore.BLUE + '::' + Style.RESET_ALL + 'Logging....')
                        print()
                        time.sleep(1)
                        while True:
                            data()
                            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '------------------------------------'*2)
                            continueOrNot = input(' Performing another operation [Y/n]').lower()
                            if continueOrNot == 'y':
                                data()
                            else:
                                print(Fore.BLUE + '::' + Style.RESET_ALL + ' Leaving Program....')
                                time.sleep(1)
                                locker.close()
                                sys.exit() # Exit the entire program
                    else:
                        print(' Please check your Password.')
                        secCounter += 1
                        if secCounter == 3:
                            print(Back.CYAN + ' Password is incorrect..' + Style.RESET_ALL)
                            print(Fore.BLUE + '::' + Style.RESET_ALL + ' Exiting.....')
                            time.sleep(1)
                            break
            else:
                print(Back.LIGHTBLUE_EX + ' Please Check your username and try again.' + Style.RESET_ALL)
                mainCounter += 1

                # Exit program if failed 3 times
                if mainCounter == 3:
                    print(Back.CYAN + ' Username is incorrect..' + Style.RESET_ALL)
                    print(Fore.BLUE + '::' + Style.RESET_ALL + ' Leaving Program....')
                    time.sleep(1)
                    sys.exit()

def data():

    # encryption method
    '''''
    def Encrypt(usrPasswords):
        # choose a random 16-byte IV
        iv = Random.new().read(AES.block_size)

        # create AES cipher
        cipher = AES.new(key, AES.MODE_CFB, iv)

        # encrypt using AES
        encodePass = iv + cipher.encrypt(usrPasswords.encode('ascii'))

        # Encrypt the AES with base64
        bs64Pass = base64.b64encode(encodePass)
        return bs64Pass

    # decryption method
    def Decrypt(encrypted):
        # decrypt AES encrypted with base64
        decode64 = base64.b64decode(encrypted)

        # decrypt AES to plaintext
        cipher = AES.new(key, AES.MODE_CFB, decode64[:16])
        decodeAES = cipher.decrypt(decode64[16:])
        return decodeAES
    '''''
    ##################################################################

    counter = 0

    while True:
        print(Fore.GREEN + '==> ' + Back.LIGHTWHITE_EX + 'Continue To Script....' + Style.RESET_ALL)
        print()
        print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '[G]et password  [V]iew all  [U]pdate Accounts/ Emails , [E]xit')
        print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '---------------------------------------------------------------')
        usrAccount = input(Fore.MAGENTA + '==> ' + Style.RESET_ALL)

        if usrAccount.lower() == 'g':
            print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Enter your Account/ Email.')
            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '--------------------------')
            getAccount = input(Fore.MAGENTA + '==> ' + Style.RESET_ALL).lower()
            print()
            if getAccount in locker:

                # decode password before loading it
                passDecode = str(base64.b64decode(locker[getAccount]))[2:-1]

                # get the password from database
                print(' {} password is ==> '.format(getAccount) + Fore.RED + passDecode + Style.RESET_ALL)

                # copy the password to the clipboard
                pyperclip.copy(passDecode)
                print(' Password is already copied to the Clipboard, Press ' + Fore.RED + 'CTRL+V' + Style.RESET_ALL + ' where you have to use it.')
                print()

            else:
                print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '-------------------------------------------')
                print(" This Account/ Email doesn't exist.")
                print(' Choose [V] to view all Accounts/ Emails stored in database.')
                print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '-------------------------------------------')

        elif usrAccount.lower() == 'v':
            accountList = list(locker.keys())
            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '-------------------------------------------')
            if len(accountList) <= 1:
                time.sleep(1)
                print(Fore.MAGENTA + '==> ' + Back.LIGHTWHITE_EX + 'Accounts/ Emails database is empty!' + Style.RESET_ALL)

            # printing all accounts available in database
            else:
                for account in accountList:

                    # escape printing the main username.
                    if account == usrName or account == signUser:
                        continue

                    print('==> ', account)
                    time.sleep(0.5)
            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '-------------------------------------------')

        elif usrAccount.lower() == 'u':

            while True:
                print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Adding a new Account/ Email          ==> ' + Fore.RED + '1' + Style.RESET_ALL)
                print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Update an existing Account/ Email    ==> ' + Fore.RED + '2' + Style.RESET_ALL)
                print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Removing an existing Account/ Email  ==> ' + Fore.RED + '3' + Style.RESET_ALL)
                print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Removing the entire database         ==> ' + Fore.RED + '4' + Style.RESET_ALL)
                print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Exit......                           ==> ' + Fore.RED + '5' + Style.RESET_ALL)
                print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '------------------------------------')


                usrDo = input(Fore.MAGENTA + '==> ' + Style.RESET_ALL)
                if usrDo == '1':
                    while True:
                        print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Enter your Account/ Email and password.[Blank to exit]')
                        print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '----------------------------------')
                        AdAccount = input(Fore.GREEN + 'Account/ Email ' + Fore.MAGENTA + ' ==> ' + Style.RESET_ALL)

                        if AdAccount == '':
                            print(' Leaving.....')
                            time.sleep(0.5)
                            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '----------------------------------')
                            break

                        password = input(Fore.GREEN + 'Password        ' + Fore.MAGENTA + '==> ' + Style.RESET_ALL).encode('ascii')

                        # encrypt new accounts passwords
                        passEncrypted = base64.b64encode(password)

                        # updating database by the new user and password
                        locker[AdAccount.lower()] = passEncrypted
                        time.sleep(1)
                        print(' Account/ Email has been Added.')

                elif usrDo == '2':
                    while True:
                        print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Enter an Account/ Email to update.[Blank to exit]')
                        print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '-----------------------------------')
                        upAccount = input(Fore.MAGENTA + '==> ' + Style.RESET_ALL)

                        if upAccount == '':
                            print(' Leaving.....')
                            time.sleep(0.5)
                            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '----------------------------------')
                            break

                        if upAccount in locker:
                            print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Enter the new password.')
                            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '-----------------------------------')
                            pasAccount = input(Fore.MAGENTA + '==> ' + Style.RESET_ALL)

                            # encrypt new accounts passwords
                            passAccEncrypted = base64.b64encode(pasAccount.encode('ascii'))
                            locker[upAccount.lower()] = passAccEncrypted
                            time.sleep(1)
                            print(' Account/ Email has been Updated.')
                    else:
                        time.sleep(1)
                        print(" This Account/ Email doesn't exist.")


                elif usrDo == '3':
                    while True:
                        print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Enter an Account/ Email to remove.[Blank to exit]')
                        print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '-----------------------------------')
                        RmAccount = input(Fore.MAGENTA + '==> ' + Style.RESET_ALL)

                        if RmAccount == '':
                            print(' Leaving.....')
                            time.sleep(0.5)
                            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '----------------------------------')
                            break

                        elif RmAccount in locker:
                            del locker[RmAccount.lower()]
                            time.sleep(1)
                            print(' Account/ Email has been Removed.')

                        else:
                            time.sleep(1)
                            print(" This Account/ Email doesn't exist.")
                elif usrDo == '4':
                    print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '----------------------------------------------------------------------------')
                    print(Fore.GREEN + '    ## WARNING !!! , THIS WILL REMOVE ALL YOUR ACCOUNTS AND EXIT THE PROGRAM. ## ' + Style.RESET_ALL)
                    print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '----------------------------------------------------------------------------')

                    print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '---------------------------------------')
                    print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Continue Deleting your database? [Y/n]')
                    print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '---------------------------------------')
                    delChoice = input(Fore.MAGENTA + '==> ' + Style.RESET_ALL).lower()
                    if delChoice == 'y':
                        shutil.rmtree('passwdLocker')
                        time.sleep(1)
                        print(Fore.GREEN + '        ## ....Deleted.... ## ' + Style.RESET_ALL)
                        sys.exit()
                    else:
                        print(' Leaving.....')
                        time.sleep(0.5)
                        print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '----------------------------------')

                # return to main loop
                elif usrDo == '5':
                    break
                else:
                    print(' Enter a correct choice. [1 to 4]')


        elif usrAccount.lower() == 'e':
            print(Fore.BLUE + '::' + Style.RESET_ALL + ' Leaving Program....')
            time.sleep(1)
            locker.close()
            sys.exit()


        else:
            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '----------------------------------')
            print(Fore.GREEN + '==> ' + Back.LIGHTCYAN_EX + 'Choose G / V / U or E.' + Style.RESET_ALL)
            counter += 1
            if counter == 3:
                break


if __name__ == '__main__':
    Main()
