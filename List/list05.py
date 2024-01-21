# 값으로 제거하기 : remove()
list_c = [1, 2, 1, 2]
list_c.remove(2)
print(list_c) # [1. 1. 2] 앞쪽의 2만 제거됨
# 여러 개의 값을 모두 제거하려면 반복문(while)과 조합해서 사용해야한다

# 모두제거하기 : clear()
list_d = [0, 1, 2, 3, 4, 5]
list_d.clear()
print(list_d) # []