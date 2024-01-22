# in/not 연산자
list_a = [273, 32, 103, 57, 52]
print("273 in list_a :", 273 in list_a)
print("100 in list_a :", 100 in list_a)
print("100 not in list_a :", 100 not in list_a)
print("99 not in list_a :", 99 not in list_a)

# 전체를 not으로 감싸는 방법도 있긴하지만 not in이 가독성 좋음
# print("not 99 in list_a :", not 99 in list_a) 