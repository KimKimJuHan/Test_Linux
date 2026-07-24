import random

def munmun():
    result = [0, 0, 0, 0, 0]
    qlist = [
        "복사하는 명령어는 무엇인가요?",
        "디렉토리를 만드는 명령어는 무엇인가요?",
        "파일및 디렉토리를 지우는 명령어는 무엇인가요?",
        "권한을 변경하는 명령어는 무엇인가요?",
        "사용자를 추가하는 명령어는 무엇인가요?"
    ]
    alist = [
        "cp",
        "mkdir",
        "rm",
        "chmod",
        "adduser"
    ]
    cnt = 0

    while True:
        ranNum = random.randint(1, 5)
        if cnt == 3:
            break
        else :
            if ranNum == 1 and result[0] == 0:
                cnt += 1
                print("="*20)
                print(qlist[ranNum-1])
                print("="*20)
                answer = input()
                if answer.strip().lower() == alist[0]:
                    print("정답!")
                    result[0] += 1
                elif answer == "0":
                    break
                else :
                    print("오답!")
                    print(alist[ranNum-1])
                    result[0] += 2
            elif ranNum == 2 and result[1] == 0:
                cnt += 1
                print("="*20)
                print(qlist[ranNum-1])
                print("="*20)
                answer = input()
                if answer.strip().lower() == alist[1]:
                    print("정답!")
                    result[1] += 1
                elif answer == "0":
                    break
                else :
                    print("오답!")
                    print(alist[ranNum-1])
                    result[1] += 2
            elif ranNum == 3 and result[2] == 0:
                cnt += 1
                print("="*20)
                print(qlist[ranNum-1])
                print("="*20)
                answer = input()
                if answer.strip().lower() == alist[2]:
                    print("정답!")
                    result[2] += 1
                elif answer == "0":
                    break
                else :
                    print("오답!")
                    print(alist[ranNum-1])
                    result[2] += 2
            elif ranNum == 4 and result[3] == 0:
                cnt += 1
                print("="*20)
                print(qlist[ranNum-1])
                print("="*20)
                answer = input()
                if answer.strip().lower() == alist[3]:
                    print("정답!")
                    result[3] += 1
                elif answer == "0":
                    break
                else :
                    print("오답!")
                    print(alist[ranNum-1])
                    result[3] += 2
            elif ranNum == 5 and result[4] == 0:
                cnt += 1
                print("="*20)
                print(qlist[ranNum-1])
                print("="*20)
                answer = input()
                if answer.strip().lower() == alist[4]:
                    print("정답!")
                    result[4] += 1
                elif answer == "0":
                    break
                else :
                    print("오답!")
                    print(alist[ranNum-1])
                    result[4] += 2
            elif min(result)  > 0:
                print("문제를 모두 풀었습니다!")
                break


    return result
