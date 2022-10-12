import pwinput as pw
# Checking that the password meets criteria.
def verify_pass(password):
  if any(char.isdigit() for char in password):
    has_digit = True
  else:
    has_digit = False
  if any(char.isupper() for char in password):
    has_upper = True
  else:
    has_upper = False
  if len(password) >= 4:
    has_chars = True
  else:
    has_chars = False
  if any(char.isspace() for char in password):
    has_space = True
  else:
    has_space = False
  return has_digit, has_upper, has_chars, has_space


def verify_user(username):
  if any(char.isspace() for char in username):
    print("\n❗ You can not use spaces in usernames.\n")
    return False
  else:
    # Pull all usernames from txt file
    f = open("userAccounts.txt","r")
    result=[]
    for x in f:
      result.append(x.split()[0])
    f.close()
    for x in result: # Search through them to check (Slow Methord)
      if x == username:
        print("\n❗ Username already taken!\n")
        return False
  return True


# Creating a NEW user account
def register():
  num_emo = cap_emo = len_emo = "❌"
  extra_error = "" # Used for adding an additional errors to password falure.
  user_verified = False
  pass_verified = False

  # Start of username creation
  while user_verified == False:
    username = input("Register an account \nType your desired username: ")
    result = verify_user(username)
    if result == True:
      user_verified = True


  # Start of password creation
  while pass_verified == False:
    password = pw.pwinput("Password must include:\n* 4+ characters\n* A Digit\n* A Letter \nCreate a password: ")

    result = verify_pass(password)
    if result == (True, True, True, False): # has_digit, has_upper, has_chars, has_space

      repeat_pass = pw.pwinput("Please re-enter your password: ")
      if repeat_pass != password:
        print("\n❗Password does not match! \n❗Please re-create a new password.\n")
        pass
      else:

        writeAccount = open("userAccounts.txt","a")
        writeAccount.write(f"{username} {password}\n")
        writeAccount.close()
        pass_verified = True
        print("\nAccount Registration Complete!")

    else:
      num_emo = cap_emo = len_emo = "❌"
      if result[0] == True:
        num_emo = "✔️"
      if result[1] == True:
        cap_emo = "✔️"
      if result[2] == True:
        len_emo = "✔️"
      if result[3] == True:
        extra_error = "\nERROR: PASSWORD CONTAINS A SPACE ❌"
      print(f"\nPassword creation failed! \nNumber: {num_emo} \nCapital: {cap_emo} \nLength: {len_emo}{extra_error}")
  # End of password creation