"""
一共有三个关卡，每个关卡一道问题，三关全部通过则挑战成功
1.答错可以重试，每道题目三次机会，若三次均答错则挑战失败
2.若用户输入为空，则提示重新作答，不浪费作答机会
3。如果用户输入字母q，则直接退出挑战
"""
res = input("欢迎参加挑战赛！请输入答案开始挑战（输入q退出挑战）：")
ansewers =''
chapter = 3
chances = 3
if res == 'q':
    print("挑战退出，欢迎下次再来！")
    exit()
while ansewers == res:
    chapter -= 1
    print(f"恭喜你，答对了！进入第{4 - chapter}关！")
    if chapter == 0:
        print("恭喜你，三关全部通过，挑战成功！")
        break
while ansewers != res and chances > 1:
    chances -= 1
    return_msg = "回答错误，请重新作答！"
    print(return_msg)
    print(f"你还有{chances}次机会！")
    if chances == 0:
        print("很遗憾，挑战失败！")
        break
if res == '':
    print("输入不能为空，请重新作答！")
# 这里没有给出具体的题目答案，导致代码逻辑不太完善

