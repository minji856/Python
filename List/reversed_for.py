# 역반복문 1. 매개변수 3 개 사용하는 방법
# -1로 입력해도 되지만 0 - 1로 0까지 반복하는 것을 강조 표현
for i in range(4, 0 - 1, -1):
    print("현재 반복 변수: {}".format(i))
print()

# 역반복문 2. reversed() 함수 사용
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))