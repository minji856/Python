# 딕셔너리를 선언합니다.
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    # dictionary의 키 이기도 하지만, 여러 개의 자료를 갖고 있는 리스트 이기도하다.
    "ingredient" : ["망고", "설탕", "메타종아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

# 출력합니다.
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
# 리스트 안 특정 값 출력
print("ingredient[1]:", dictionary["ingredient"][1])
print("origin:", dictionary["origin"])
print()

# 값을 변경합니다.
dictionary["name"] = "8D 건조 망고"
print("바뀐 값:", dictionary["name"])
print()

# 새로운 값 추가하기 / 제거하기
dictionary["price"] = 5000
print("새로운 값 추가:", dictionary)
del dictionary["ingredient"]
print("ingerdient 제거:", dictionary)