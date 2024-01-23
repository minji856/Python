# 딕셔너리를 선언합니다.
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    # dictionary의 키 이기도 하지만, 여러 개의 자료를 갖고 있는 리스트 이기도하다.
    "ingredient" : ["망고", "설탕", "메타종아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

# 사용자로부터 입력을 받습니다.
key = input("> 접근하고자 하는 키: ")

# 출력합니다.
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")