#Variables

ROWS = 5
COLUMNS = 6
table=[]
number1=0
row1=""

#Alphabet for each columns
def alpha():
  alpha=""
  alphabet=['A','B','C','D','E','F']
  for a in range(len(alphabet)):
    if a > 0:
      alpha = alpha + "   "
    alpha = alpha + alphabet[a]
  print("%23s" %alpha,'\n')

alpha()

#create empty seat
for i in range(ROWS) :
  row = ['E'] *COLUMNS
  number= number1 
  number1 = number + 1
  table.append(row)
  print(number,"   ".join(table[i]),end="  ")
  print()

#seating map after choosing seat
  
def after_booking():
  alpha_dict={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}
  trans=int(alpha_dict[question2])
  global question1
  global table
  global ROWS
  global COLUMNS
  number2 = 0
  for i in range(ROWS) :
    row = ['E'] *COLUMNS
    number3 = number2
    number2 = number3 + 1
    table[question1][trans] = "X"
    table.append(row)
    print(number3,"   ".join(table[i]),end="  ")
    print()

#Choose the seat    
def question():
  global question1
  global question2
  question1=int(input("Enter your row number"))
  question2=input("Enter your letter seat number")
  alpha_dict={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}
  trans=int(alpha_dict[question2])
question()

#Ask for another seat
def condition():
  global question2
  global trans
  alpha_dict={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}
  trans=int(alpha_dict[question2])
  if table[question1][trans] == "E":
    alpha()
    after_booking()
  else:
    print("The seat is taken,choose another seat")
    alpha()
    after_booking()
    question()
    alpha()
    after_booking()
condition()

question3=input("Do you want to enter another seat ? (Y/N)")
while question3 == "Y":
  question()
  condition()
  question3=input("Do you want to enter another seat ? (Y/N)")
  if question3 == "N":
    print("")
  
