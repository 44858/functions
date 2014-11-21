# functions improvement exercise
# times-table tester
import random
# main program
print("Times-table tester")
print()
testTable = input("Which times-table do you want to be tested on? ")
testTable = int(testTable)
for questions in range(1,6):
    Num1 = testTable
    Num2 = random.randrange(2,13)
    Ans = Num1 * Num2
    UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
    UserAnswer = int(UserAnswer)
    if UserAnswer == Ans:
        print('Well done, you got the correct answer!')
        print()
        else:
            print('Sorry, you got the answer wrong. The correct answer is',Ans)
            print() 


#improved program
import random
def test_table():
    testtable = int(input("Please enter the times table you would like to be tested on: "))
    return testtable

def questions_loop(testtable):
    for questions in range(1,6):
        num1 = testtable
        num2 = random.randrange(2,13)
        ans = num1 * num2
        use_ans = int(input(str(num1) + "x" + str(num2) + " = ? "))

def 
    
