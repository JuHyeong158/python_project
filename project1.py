def hamsu(x):
    y = (x-100) * 0.9
    return y
a, b = map(int,input("체중과 키를 입력하시오: ").split())
if b <hamsu(a):
    print("저체중입니다.")
elif b ==hamsu(a):
    print("표준입니다.")
elif b >hamsu(a):
    print("과체중입니다.")