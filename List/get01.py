# 딕셔너리를 선언합니다.
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    # dictionary의 키 이기도 하지만, 여러 개의 자료를 갖고 있는 리스트 이기도하다.
    "ingredient" : ["망고", "설탕", "메타종아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

# 존재하지 않는 키에 접근해 봅니다.
value = dictionary.get("taste") # 없는 키
print("값:", value)

# None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")