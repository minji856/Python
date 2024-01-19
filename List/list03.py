list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

# 제거 방법[1] - del 키워드
# 리스트의 특정 인덱스 제거
del list_a[1]
print("del list_a[1]:", list_a)
print()

# 제거 방법[2] - pop()
# 매개 변수를 입력하지 않으면 -1이 들어가 마지막 요소 제거
list_a.pop(2)
print("pop(2):", list_a)
print()

# 범위로 제거하기
del list_a[1:3]
print("del list_a[1:3]:", list_a)
print()

list_b = [0, 1, 2, 3, 4, 5, 6]
print("list_b", list_b)
# [:3]3을 기준으로 왼쪽을 모두 제거, 3번째는 불포함
# [3:]3을 기준으로 오른쪽 모두 제거, 3번째도 포함해서 제거
del list_b[:3]
print("del list_b[:3]:",list_b)