import pwinput as pw
def login():
  username_verified = False
  password_verified = False

  #
  # Username Verification Below
  # 

  while username_verified == False:
    count = 0
    username = input("Login to account.\n \nAccount Username: ")
    # Pull all usernames from txt file.
    f = open("userAccounts.txt","r")
    result=[]
    for x in f:
      result.append(x.split()[0])
    f.close()
    for x in result: 
      if x == username:
        print("Username exists.")
        username_verified = True
      elif x != username:
        count += 1
      if x != username and count == len(result):
        print("User is not registered. (Usernames are casesensitive!)") 
  
  #
  # Password Verification Below
  # 

  while password_verified == False:
    count = 0
    password = pw.pwinput("\nInput your password: ")

    f = open("userAccounts.txt","r")
    result=[]
    for x in f:
      result.append(x.split())
    f.close()
    for x in result:
      if x[0] == username and x[1] == password:
        print(f"Successfully logged in to {username}\n")
        password_verified = True
        return username
      elif x[0] == username and x[1] != password:
        count += 1
        print("Password Incorrect! Try Again.")
      
