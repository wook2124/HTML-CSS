string = input("7문자 이상 문자열을 입력하시오 :")
m = (string[0:] + string[:-1])
print(m)

# 입력값 : Hello World
# 최종 출력 : Helrld