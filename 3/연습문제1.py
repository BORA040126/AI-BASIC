year=int(input("출생년도를 입력하시오:"))
age=2023-year+1
if(age>26 or age<8):
    print("학생이 아닙니다")
elif(age<14):
    print("초등학생")
elif(age<17):
    print("중학생")
elif(age<20):
    print("고등학생")
else:
    print("대학생")