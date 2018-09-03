# 1. 打印矩阵
def s_jx():
    for i in range(0,5):
        for j in range(0,5):
            print("* ",end="")
        print()

# 2. 打印空心矩阵

def k_jx():
    for i in range(0,5):
        for j in range(0,5):
            if (i in range(1,4)) and (j in range(1,4)):
                print("  ",end="")
            else:
                print("* ",end="")
        print()


# 3. 打印直角三角形

def s_Rsjx():
    for i in range(0,5):
        print("* "*(i+1))


# 4. 打印空心直角三角形

def k_Rsjx():
    for i in range(0,5):
        for j in range(0,i+1):
            if j in range(1,i) and i in range(0,4):
                print("  ",end="")
            else:
                print("* ",end="")
        print()

# 5. 打印正三角形

def s_Zsjx():
    for i in range(0,5):
        for j in range(0,9):
            if j in range(4-i,4+i+1,2):
                print("*",end="")
            else:
                print(" ",end="")
        print()
# 6. 打印空心正三角形
def k_Zsjx():
    for i in range(0,5):
        for j in range(0,9):
            if i == 4:
                if j%2==0:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if j == 4-i or j == 4+i:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()


def PrtGraph():
    s = input("请输入要打印的图形：")
    if  s == "实心矩形":
        s_jx()
    elif s =="空心矩形":
        k_jx()
    elif s == "实心直角三角形":
        s_Rsjx()
    elif s == "空心直角三角形":
        k_Rsjx()
    elif s == "实心正三角形":
        s_Zsjx()
    elif s == "空心正三角形":
        k_Zsjx()
    else:
        print("无法识别")

if __name__ == '__main__':
    PrtGraph()
