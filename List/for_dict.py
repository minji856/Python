# for반복문과 딕셔너리 함께 사용
# 딕셔너리를 선언합니다.
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    # dictionary의 키 이기도 하지만, 여러 개의 자료를 갖고 있는 리스트 이기도하다.
    "ingredient" : ["망고", "설탕", "메타종아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

# for 반복문을 사용합니다.
for key in dictionary:
    # 출력합니다.
    print(key, ":", dictionary[key])