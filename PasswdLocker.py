#!/usr/bin/python
#__author___= 'Hussam ashraf'
# PasswdLocker.py - basic password locker for keeping important passwords.
# Must run it as Administrator


import shelve as sh
import os, sys
from colorama import Fore, Style, Back
import time
import pyperclip
import string



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

    # check if username exist 
    if not list(locker.keys()):
        signUser = input(Fore.BLUE + '::' + Style.RESET_ALL + 'Enter a new username >> ')
        signPass = input(Fore.BLUE + '::' + Style.RESET_ALL + 'Enter your password >> ')
        locker[signUser.lower()] = signPass
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
            time.sleep(1.5)
            if usrName.lower() in locker:
                secCounter = 0
                while True:
                    password = input(Fore.BLUE + '::' + Style.RESET_ALL + 'Enter password for " {} " >> '.format(usrName)).lower()

                    # matching username and password
                    if locker[usrName] == password:
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

                # get the password from database
                print(' {} password is ==> '.format(getAccount) + Fore.RED + locker[getAccount] + Style.RESET_ALL)

                #copy the password to the clipboard
                pyperclip.copy(locker[getAccount])
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
                    if account == usrName:
                        continue

                    print('==> ', account)
                    time.sleep(0.5)
            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '-------------------------------------------')

        elif usrAccount.lower() == 'u':

            print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Adding a new Account/ Email          ==> ' + Fore.RED + '1' + Style.RESET_ALL)
            print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Update an existing Account/ Email    ==> ' + Fore.RED + '2' + Style.RESET_ALL)
            print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Removing an existing Account/ Email  ==> ' + Fore.RED + '3' + Style.RESET_ALL)
            print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Exit......                           ==> ' + Fore.RED + '4' + Style.RESET_ALL)
            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '------------------------------------')

            while True:
                usrDo = input(Fore.MAGENTA + '==> ' + Style.RESET_ALL)
                if usrDo == '1':
                    while True:
                        print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Enter your Account/ Email and password.[Blank to exit]')
                        print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '----------------------------------')
                        AdAccount = input(Fore.MAGENTA + 'Account/ Email  ==> ' + Style.RESET_ALL)

                        if AdAccount == '':
                            print(' Leaving.....')
                            time.sleep(0.5)
                            break

                        password = input(Fore.MAGENTA + 'Password        ==> ' + Style.RESET_ALL)

                        # updating database by the new user and password
                        locker[AdAccount.lower()] = password
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
                            break

                        if upAccount in locker:
                            print(Fore.GREEN + '==> ' + Style.RESET_ALL + 'Enter the new password.')
                            print(Fore.MAGENTA + '==> ' + Style.RESET_ALL + '-----------------------------------')
                            pasAccount = input(Fore.MAGENTA + '==> ' + Style.RESET_ALL)
                            locker[upAccount.lower()] = pasAccount
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
                            break

                        if RmAccount in locker:
                            del locker[RmAccount.lower()]
                            time.sleep(1)
                            print(' Account/ Email has been Removed.')

                        else:
                            time.sleep(1)
                            print(" This Account/ Email doesn't exist.")

                # return to main loop
                elif usrDo == '4':
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

