def munResult(result):
    y,n,p = 0,0,0
    for i in result:
        if result[i] == 0:
            y += 1
        elif result[i] == 2:
            n += 1
        elif result[i] == 1:
            p += 1

    print("="*20)
    print(f"최종결과\n정답:{y}문제\n오답:{n}문제\n풀지않은문제:{p}")
    if y == 3 :
        print("A등급")
        print("="*20)
    elif y == 2 :
        print("B등급")
        print("="*20)
    elif y == 1 :
        print("C등급")
        print("="*20)
    else :
        print("F등급")
        print("="*20)