number = int(input("정수 입력> "))

if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
{}는(은) 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
{}는(은) 홀수입니다.""".format(number, number))
    
# 출력예제에서 빈칸은 사라졌지만 코드가 이상한 구조형식
# python .\if_string01.py
# 정수 입력> 2
# 입력한 문자열은 2입니다.
# 2는(은) 짝수입니다.
# python .\if_string.py
# 정수 입력> 3
#         입력한 문자열은 3입니다.
#         3는(은) 홀수입니다.