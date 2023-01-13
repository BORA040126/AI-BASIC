a=int(input("구구단 몇 단을 계산할 까요?:"))

for i in range(9):
    print("%dx%d=%d" %(a,i+1,a*(i+1)))

