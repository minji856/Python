# 변수를 선언합니다.
list_test = [1, 2, 1, 2]
value = 2

# list_test 내부에 value가 있다면 반복
# 2가 제거될 떄까지 반복한다
while value in list_test:
    list_test.remove(value)

print(list_test)