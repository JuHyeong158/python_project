import random
n = int(input("복권번호(1-99사이)를 입력하시오: "))
dangcheom = random.randint(10, 99)
result = 0
if n == dangcheom:
    result = 100
else:
    for i in range(len(str(n))):
        for j in range(len(str(dangcheom))):
            if str(n)[i] == str(dangcheom)[j]:
                result = 50
                break
        if result == 50:
            break
print(f'당첨번호는 {dangcheom}입니다')
if result == 100 or result == 50:
    print(f"상금은 {result}만원 입니다.")
else:
    print("상금은 없습니다.")

