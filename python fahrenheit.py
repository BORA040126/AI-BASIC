print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")


def f(x):
    return ((9/5*x))+32

x=int(input('변환하고 싶은 섭씨 온도를 입력해 주세요:'))

print("섭씨온도:%d"%x)
print("화씨온도:",f(x))
