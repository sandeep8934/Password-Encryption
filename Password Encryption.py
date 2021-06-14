# Password Encryption

import string
import random

#Sample username & password
username = "sandeep@gmail.com"         # User input username
password = "Sandeep@0808"              # User input password

# This function will make list for random_pass & from user input password

def extraString(list):
    a = "".join(random_pass)
    b = "".join(pass_word)
    Final_Pass = ""

    for i in a:
        if i not in b:
            Final_Pass = Final_Pass + i

    return Final_Pass[:10] + b

random_pass = []                                # List 1 for shuffle
pass_word = list(password)                      # List 2 for shuffle

random_pass.extend(string.ascii_lowercase)      # To add a,b,c,.....
random_pass.extend(string.ascii_uppercase)      # To add A,B,C,.....
random_pass.extend(string.digits)               # To add 1,2,3,.....
random_pass.extend(string.punctuation)          # To add !,@,#,.....

if __name__ == '__main__':
    random.shuffle(random_pass)
    random.shuffle(pass_word)

    result = extraString(list)
    print("User Entered Password is", password)             # It will print user entered password.
    print("Encrypted Password is", result)                  # It will print encrypted password.

    
