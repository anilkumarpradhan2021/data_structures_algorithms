from pip.backwardcompat import raw_input
from TestMath import summary 
import MathQuestions
number1 = raw_input("enter 1st number")
number2 = raw_input("enter 2nd number")
print("Sum of 2 number : " + summary.sum(number1, number2))
print("Multiple of 2 number : " + str(MathQuestions.multiply.mul(int(number1), int(number2))))
