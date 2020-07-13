head = int(input("머리의 수를 입력하시오>"))
leg = int(input("다리의 수를 입력하시오(짝수만 가능)>"))
chicken = 0
pig = 0
for i in range(head+1):
    chicken = i
    pig = head - i
    if 2*chicken + 4*pig == leg:
        print(chicken)
        print(pig)
        break
else:
    print("답이 없음")