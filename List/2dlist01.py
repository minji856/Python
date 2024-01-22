# 파이썬 튜터로 이해하기 인덱스 숫자만큼 반복 출력하는 느낌이다
# [1, 2, 3][1, 2, 3][1, 2, 3] 으로 출력되는
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for items in list_of_list:
    for item in items:
        print(items)
    # item를 출력하면 1,2,3,4,5,6,7,8,9 만 출력된다