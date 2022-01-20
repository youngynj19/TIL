answer = ""

while True:
    answer = input("입력!\n 'q'누르면 종료\n: ")
    if answer == "q":
        break
    print("'{0}' 입력".format(answer))

print("종료")