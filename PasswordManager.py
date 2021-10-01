"""
Python Project by: Talita Audibert
Project Title: Password Manager

DESCRIPTION
    Zara is developing a new version of password manager.
    Earlier, she was using some third-party password manager but she figured out that it can't keep track of all the passwords which has been set for the respective account.
    As she is very concerned about the security, she decided to develop her own version of the password manager.

Objective: To develop a custom password manager using Python
Domain:  Security

"""

# Implement base class 
class BasePasswordManager:
    # old_passwords: is a list that holds all of the user's past passwords.
    # The last item of the list is the user's current password.
    old_password=[]

    # get_password method that returns the current password as a string.
    def get_password(self):
        if not self.old_password:
            print("\nOw snap! The list is empty. \nYou should choose the option to enter a password.\n")
            return 0
        else:
            return self.old_password[-1]

    # is_correct method that receives a string and returns a boolean True or False depending on whether the string is equal to the current password or not.
    def is_correct(self, password):
        return self.old_password[-1] == password

class PasswordManager (BasePasswordManager):

    # get_level method that returns the security level of the current password.
    # It can also check and return the security level of a new password passed as a string.
    # Security levels:
    #   level 0 - password consists of alphabets or numbers only.
    #   level 1 - Alphanumeric passwords.
    #   level 2 - Alphanumeric passwords with special characters.
           
    def get_level(self, data=''):
        if not data:
            data = self.get_password()
        if(data.isalpha() | data.isnumeric()):
            level=0
        elif(data.isalnum()):
            level=1
        else:
            level=2
            
        return level

    # set_password method that sets the user's password.
    def set_password(self, password):
        if(len(self.old_password) == 0):
            self.old_password.append(password)
            print("\nPassword set successfully\n")
        elif(self.get_level(password) < self.get_level()):
            print("\nThe new password must be of the highest security level for a successful password change\n")
        elif (len(password) <= 6):
            print("\nThe password must have more than 6 characters\n")
        else:
            self.old_password.append(password)
            print("\nPassword set successfully\n")
            


########################
## Main menu program ##
########################

def menu():    
    option=0
    pm = PasswordManager()
    print("=======================================")
    print(" Welcome to the Password Manager tool  ")
    print("=======================================")

    while(option < 4):
        print("\n\nChoose an option to execute:\n")
        print("1. Get latest password")
        print("2. Set a new password")
        print("3. Get the password level")
        print("4. Quit")
        
        option = input("\nType your choice:  ")
        
        try:
            option = int(option)
            if(option == 1):
                pw = pm.get_password()
                if pw:
                    print(f"\nYour current password is {pw}")
                else:
                    pw
            elif(option ==2):
                password=input("\nType the new password: ")
                pm.set_password(password)
            elif(option==3):
                password=input("\nType the password or leave blank to check the current: ")
                print(f"Level is {pm.get_level(password)}")
            else:
                print("BYEEE")
                break
        except ValueError:
            print("\n\n\n\n\nWhat are you trying to do?")
            print("Type the numer of the option you want!")
            print("Let's try again\n\n")
            menu()

menu()
