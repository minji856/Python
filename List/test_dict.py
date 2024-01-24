pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1},
]

print("# 우리 동네 애완 동물들")
for pet in pets:
    # 숫자와 문자열 사이에 빈칸이 없게 출력 str(pet["age"]),"살"
    print(pet["name"], str(pet["age"]) + "살")
print()

### 숫자가 몇 번 등장하는지 출력하는 코드 ###
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number]=1
print(counter)
print()

### type([]) is list, dict으로 출력하기 ###
charcter = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in charcter:
    if type(charcter[key]) is dict:
        for small_key in charcter[key]:
            print(small_key,":",charcter[key][small_key])
    elif type(charcter[key]) is list:
        for item in charcter[key]:
            print(key,":",item)
    else:
        print(key,":",charcter[key])