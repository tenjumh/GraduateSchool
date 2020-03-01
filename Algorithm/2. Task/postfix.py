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

a = "(A+B)*C"
#a = "3*(2+1)"  # 321+*
operator = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
stack = []
result = ""
for i in a:
    if i == "(":
        push(i)
    elif i == ")":
        while (peek() != "("):
            result += pop()
        pop()
    elif i in operator:
        if (not len(stack) == 0 and operator[peek()] >= operator[i]):
            result += pop()
        push(i)
    else:
        result += i
while not len(stack) == 0:
    result += pop()

print(result)