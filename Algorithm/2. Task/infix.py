#2019.10.9
def push(item):  # 삽입 연산
    stack.append(item)

def peek():  # top 항목 접근
    if len(stack) != 0:
        return stack[-1]

def pop():  # 삭제 연산
    if len(stack) != 0:
        item = stack.pop(-1)
        return item

def plus():
    num2 = pop()
    num1 = pop()
    stack.append(int(num1) + int(num2))

def minus():
    num2 = pop()
    num1 = pop()
    stack.append(int(num1) - int(num2))

def divi():
    num2 = pop()
    num1 = pop()
    stack.append(int(num1) / int(num2))

def mult():
    num2 = pop()
    num1 = pop()
    stack.append(int(num1) * int(num2))

a = "8 3 2 + 1 - /"
a = a.split()
stack = []

for i in a:
    if i == "+":
        plus()
    elif i == "-":
        minus()
    elif i == "/":
        divi()
    elif i == "*":
        mult()
    else:
        stack.append(i)

print("결과값 :", stack[0])