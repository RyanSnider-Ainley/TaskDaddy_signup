import hashlib.sha256

#encode() will convert the input to byte format for MD5hashing

def sign_Up():
    email =input("Please enter your email address: ")
    passwd =input("Please enter your password: ")   #
    reenter=input("Please enter your password again to confirm: ")

    if reenter==passwd:
        epasswd=reenter.encode()
        hash1=hashlib.md5(epasswd).hexdigest()
    with open ("signup.txt", "w") as f:
        f.write(email +"\n")
        f.write(hash1 + " " + password + "\n")
        f.close()
        print("Sign Up Successfully Success")
    if reenter!=password:
        print("Sign Up Failure please reenter the matching passwords\n")


def login_Acess():
    email =input("Please enter your email address: ")
    passwd =input("Please enter your password: ")   #

    auth=passwd.encode()
    auth_hash= hashlib.md5(auth).hexdigest()
    with open("signup.txt", "w") as f:
        signup_email, signupasswd = f.read().split("\n")
        f.close()

        if email == signup_email && auth_hash == signupasswd: print("Logged in successful!")
        else: print("Loggin failed:")

while 1:
    print("Loggin System Access:")
    choice= input(f"Enter 1 for signup access:\n Enter 2 for login access:\nEnter 3 to EXIT:")
    if choice == 1:
         signUp()
    elif choice == 2:
        login_Acess
    elif choice ==3:
        break
    else:
        print("Not Authorized:")
        