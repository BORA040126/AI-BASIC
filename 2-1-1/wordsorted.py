word=input("글자를 입력해 주세요:")
word_list=list(word)
for _ in range(len(word_list)):
    print(word_list.pop())