print("숫자를 맞춰 보세요(1~100)")
import random

true_value=random.randint(1,100)
input_value=100000

while true_value!=input_value:
    input_value=int(input())
    if(input_value>true_value):
        print("숫자가 너무 큽니다")
    elif(input_value<true_value):
        print("숫자가 너무 작습니다")
    else:
        print("정답")
