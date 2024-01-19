# 리스트 슬라이싱
# 리스트[시작_인덱스:끝_인덱스:단계]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("numbers:", numbers)
print("numbers[0:5:2]:",numbers[0:5:2]) # 원본에 변화 X
print()

# 시작과 끝 인덱스는 자동으로 "전부"로 지정
print("# 단계가 -1이므로 반대로 출력된다 numbers[::-1]", numbers[::-1])
print("# -2단계는 반대 상태에서 2단계 씩:", numbers[::-2])