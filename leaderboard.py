# Maybe write code to not allow duplicate users. E.G. Players highest score used

def sortid(line):

  gap = line.find(" ", 11) # Seperate the score from the other data
  individual_score = line[gap:].rstrip() #Must be in a function
  #print ("Score:" + individual_score)
  return individual_score

def show():
  file = open("leaderboard.txt", "r")
  lines = []

  for line in file:
    templ = line.rstrip()
    lines.append(templ)
    #print(templ)
  #print(lines)
  lines.sort(reverse=True, key=sortid)
  #print(f"Sorted Score: {lines}")

  print("\nLeaderboard\n" + '\n'.join(lines[:5]) + "\n")
  input("Enter to return to main menu")
      
  file.close()