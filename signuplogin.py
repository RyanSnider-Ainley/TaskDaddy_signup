# no hash yet just login class templete
import pylance

class LoginHandler:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        auth = password.encode()
        auth_hash= hashlib.md5(auth).hexdigest()
        with open("signup1.txt", "w") as f:
                signup_email, signupasswd = f.read().split("\n")
        f.close()
    def check_login(self, username, password):
        if self.username == username and self.password == password: return True 
        print("Logging in cutie! login bam!!")
        else: return False
        print("Error logging in.")

log =LoginHandler("", "")
log.check_login(raw_input(f"Enter username: "+ logId(username)),raw_input(f"Enter password: "+log_pd(password)))
#log_Id = input("Enter username: ")  + username
#log_pd = input("Enter password: ") + password
#log.check_login(log_Id, log_pd) # should I be passing these values, no values

