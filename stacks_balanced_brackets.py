from collections import deque


def is_matched(expression):
    twins = {'(': ')', '[': ']', '{': '}'}
    stack = deque()
    for item in expression:
        if item in '([{':
            stack.append(item)
        elif item in '}])':
            if len(stack) == 0:
                return False
            top = stack.pop()
            if item != twins[top]:
                return False
        else:
            raise ValueError
    return True if len(stack) == 0 else False


if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        expression = input().strip()
        if is_matched(expression) == True:
            print("YES")
        else:
            print("NO")
