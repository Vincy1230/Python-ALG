import os
import math
import shutil
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import turtle as t
import random as r

Project = {"Name": "交集", "Path": ".\\", "Leaves": 0, "IsLeft": True, "Max": 0}
COLOR = {
    "边框": "black",
    "树干": "peru",
    "树枝": "peru",
    "树叶": ["green", "lightgreen", "darkgreen"],
    "背景": "lightblue",
}  # 背景色不会被保存
onename_list = []


def path():
    tkinter.Tk().withdraw()
    if tkinter.messagebox.askokcancel("交  集", "将在桌面建立文件夹"):
        path_path = os.path.expanduser("~/Desktop/{}".format(Project["Name"]))
    else:
        p = tkinter.filedialog.askdirectory()
        if p == "":
            exit()
        path_path = os.path.join(p, Project["Name"])
    Project["Path"] = os.path.abspath(path_path)
    if not os.path.exists(Project["Path"]):
        os.makedirs(Project["Path"])


def setting():
    t.setup(450, 675)
    t.screensize(400, 600)
    t.bgcolor(COLOR["背景"])


def ready():
    t.resetscreen()
    t.ht()
    t.speed(0)
    t.left(90)
    t.up()
    t.goto(0, -300)
    t.down()
    t.pensize(1)
    t.pencolor(COLOR["边框"])
    t.goto(-200, -300)
    t.goto(-200, 300)
    t.goto(200, 300)
    t.goto(200, -300)
    t.goto(0, -300)
    t.pencolor(COLOR["树干"])
    for i in range(1, 30):
        t.pensize(30 - i)
        t.fd(i)


def tree(n, l):
    if Project["Leaves"] >= Project["Max"]:
        return
    t.pd()
    t.pencolor(COLOR["树枝"])
    t.pensize(n / 4)
    x, y = t.pos()
    t.forward(l)
    if n > 0:
        b = r.random() * 15 + 10
        c = r.random() * 15 + 10
        d = l * (r.random() * 0.35 + 0.6)
        if Project["IsLeft"]:
            t.right(b)
            tree(n - 1, d)
            t.left(b + c)
            tree(n - 1, d)
            t.right(c)
        else:
            t.left(b)
            tree(n - 1, d)
            t.right(b + c)
            tree(n - 1, d)
            t.left(c)
    else:
        t.right(90)
        t.pencolor(r.choice(COLOR["树叶"]))
        t.circle(2)
        t.left(90)
        Project["Leaves"] = Project["Leaves"] + 1
    t.pu()
    t.goto(x, y)


def draw(count, onenumber):
    Project["Max"] = int(math.sqrt(count))
    Project["Leaves"] = 0
    for n in range(1, 13):
        if 2 ** (n - 1) >= Project["Max"]:
            break
    l = 100 * 0.8 ** (13 - n)
    tree(n, l)


def trees(onename, onenumber):
    if onename not in onename_list:
        onename_list.append(onename)
        onepath = os.path.join(Project["Path"], onename)
        if os.path.exists(onepath):
            shutil.rmtree(onepath)
        os.makedirs(onepath)
        step = 390 / onenumber
        now = -255
        ready()
        for i in range(1, onenumber + 1):
            print()
            left = input("在故事的第{}段，你对Ta说了多少话：".format(i))
            while not left.isdigit():
                left = input("请输入整数：")
            left = eval(left)
            right = input("在故事的第{}段，你对Ta说了多少话：".format(i))
            while not right.isdigit():
                right = input("请输入整数：")
            right = eval(right)
            print("请等待完成绘制... ")
            t.up()
            t.goto(0, now)
            nowSeth = 35 * (onenumber - i) / onenumber + 10
            t.seth(90 + nowSeth)
            Project["IsLeft"] = True
            draw(left, onenumber)
            t.seth(90 - nowSeth)
            Project["IsLeft"] = False
            draw(right, onenumber)
            now = now + step
            ts = t.getscreen()
            ts.getcanvas().postscript(
                file=os.path.join(onepath, "{:0>2}.eps".format(i))
            )
            print("绘制完成...")
        print("\n至此，Ta的故事告一段落，未完且待续。")
    else:
        print("\n你已讲过有关Ta的一章。")
    print("还有吗？你可以告诉我下一个人的名字了。")
    print("如果没有更多，请只按下Enter... ")


def end():
    print("\n讲述完毕，你的故事已经凝为诗篇。")
    t.bye()
    print("按下 Enter 吧，结束你的旅途，将为你打开刻满记忆的画卷。")
    print("\nPress Enter to Exit... ")
    input()
    os.system("start explorer " + Project["Path"])
    exit()


print(
    """ 
*********************************************************** 
 
                    --  交  集  --                        
                当暖流相迎，风总会向上盘旋                   
 
*********************************************************** 
                              Software by Vincy 2021 - 2024
"""
)
path()
print(
    ''' 
            *                  
           /.\\               如果有这么一天： 
          /..'\\              烈日的光芒只来自一个方向 
          /'.'\\              少年的歌谣不再有诗和远方 
         /.''.'\\             微风还能徜徉 
         /.'.'.\\             树木仍会生长 
  "'""""/'.''.'.\\""'"'"      只是会长成人们不愿看到的模样。 
        ^^^[_]^^^              
'''
)
print("就此回忆吧，在风沙掩埋记忆之前，就此开始抒写你和Ta们的故事。")
print("\n故事不长，但也足够分得篇章。每一个人的故事，你又想分成几段讲？")
onenumber = input("告诉我吧，请输入整数：")
while not (onenumber.isdigit() and eval(onenumber) in range(2, 31)):
    onenumber = input("\n太多赘述亦难以成章。\n请输入 2 ~ 30：")
onenumber = eval(onenumber)
onename = input("\n好的。记忆里的第一个人，Ta叫什么：")
setting()
while onename != "":
    trees(onename, onenumber)
    onename = input("\n来吧，请输入：")
end()
