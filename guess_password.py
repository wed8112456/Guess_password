# 可自由設定開始，結束值
# 每猜一次計算，並告知使用者猜大猜小區間＆並猜幾次
# 如果猜對告知猜了共幾次

import random

star = int(input('輸入起始值：'))
end = int(input('輸入結束值：'))

ans = random.randint(star, end)
count = 0
while True:
    user_guess = int(input('請猜數字：'))
    count += 1
    if user_guess == ans:
        print(f'恭喜你！猜對了....你總共猜了{count}次')
        break
    else:
        if user_guess > ans:
            end = user_guess
            print(f'比答案大..介於{star}-{end}之間..這是你猜的第{count}次')
        else:
            star = user_guess
            print(f'比答案小..介於{star}-{end}之間..這是你猜的第{count}次')
