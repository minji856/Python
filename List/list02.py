# append(),insert()는 파괴적 함수, 원본에 영향을 끼친다.
# 리스트를 선언합니다.
list_a = [1, 2, 3]

# 리스트 뒤에 요소 1개씩 추가하기
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 1개씩 추가하기
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)
print()

# 한번에 여러 요소 추가하기
print("# 리스트 한번에 여러 요소 추가하기")
list_a.extend([4, 5, 6])
print(list_a)
print()

# 연결연산자로 list_a + list_b 하는것과 비슷해보이지만 원본에 변화가없다.
print("# 연결연산자는 extend와 비슷해 보이지만, 원본에 어떠한 변화가 없다")
list_b = [7, 7, 7]
list_c = list_a + list_b
print("list_b를 합친값 : ", list_c)
print("원본 list_a : ", list_a)