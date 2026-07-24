import question
import testResult

while True:
    print("문제 시작합니다. 종료를 원하시면 0번을 눌러주세요")
    result = question.munmun()
    clck = int(input("***3문제 이상 풀으셨습니다*** 종료를 원하시면 0번을 눌러주세요\n"))
    if clck == 0 :
        testResult.munResult(result)
        break
    else:
        continue










