head = int(input("머리의 수를 입력하시오>"))
leg = int(input("다리의 수를 입력하시오>"))
for chicken in range(head+1):
    pig = head - chicken
    if 2*chicken + 4*pig == leg:
        print(chicken)
        print(pig)
        break
else:
    print("답이 없음")