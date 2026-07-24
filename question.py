import random

def munmun():
    result = [0, 0, 0, 0, 0]
    while True:
        ranNum = random.randint(1, 5)
        if ranNum == 1 and result[0] == 0:
            print("="*10)
            print("1번문제\n다음중 어쩌구저쩌구")
            print("="*10)
            answer = input()
            if answer.strip().lower() == "정답1":
                print("정답!")
                result[0] += 1
            elif answer == "0":
                break
            else :
                print("오답!")
                print("정답은 ~")
                result[0] += 2
        elif ranNum == 2 and result[1] == 0:
            print("="*10)
            print("2번문제\n다음중 어쩌구저쩌구")
            print("="*10)
            answer = input()
            if answer.strip().lower() == "정답2":
                print("정답!")
                result[1] += 1
            elif answer == "0":
                break
            else :
                print("오답!")
                print("정답은 ~")
                result[1] += 2
        elif ranNum == 3 and result[2] == 0:
            print("="*10)
            print("3번문제\n다음중 어쩌구저쩌구")
            print("="*10)
            answer = input()
            if answer.strip().lower() == "정답3":
                print("정답!")
                result[2] += 1
            elif answer == "0":
                break
            else :
                print("오답!")
                print("정답은 ~")
                result[2] += 2
        elif ranNum == 4 and result[3] == 0:
            print("="*10)
            print("4번문제\n다음중 어쩌구저쩌구")
            print("="*10)
            answer = input()
            if answer.strip().lower() == "정답4":
                print("정답!")
                result[3] += 1
            elif answer == "0":
                break
            else :
                print("오답!")
                print("정답은 ~")
                result[3] += 2
        elif ranNum == 5 and result[4] == 0:
            print("="*10)
            print("5번문제\n다음중 어쩌구저쩌구")
            print("="*10)
            answer = input()
            if answer.strip().lower() == "정답5":
                print("정답!")
                result[4] += 1
            elif answer == "0":
                break
            else :
                print("오답!")
                print("정답은 ~")
                result[4] += 2
        elif min(result)  > 0:
            break


    return result
