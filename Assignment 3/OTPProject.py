import sys
import random
numrand = random.randint(1, 20)
print(numrand)
firstname = input("Please Enter your First Name: ")
lastname = input("Please Enter your Last Name: ")
usernum = ''
attempt = 0
count = 4
max_tries = 1
while max_tries < count:
    try:
        usernum = int(input("Please Enter a number in the range of 1 to 20: "))
        count += 1
    except:
        print("Sorry the input must be a number. TRY AGAIN !!!")
    else:
        if(usernum > 20) and (usernum > 1):
            print("WRONG INPUT!!! TRY AGAIN")
            break

    if usernum == numrand:
        print("OTP SUCCESSFULLY MATCHED")
        break
    else:
        print("ERROR!!! ENTER THE OTP AGAIN")
        max_tries += 1

    if max_tries < 5:
        temp = input(f"Enter YES/NO to continue trying: ").lower()
        if temp == "yes":
            attempt = count - max_tries
        else:
            print("Thanks for the Attempt")
            sys.exit(1)
    else:
        print("Sorry Program Crashed")
        sys.exit(1)

