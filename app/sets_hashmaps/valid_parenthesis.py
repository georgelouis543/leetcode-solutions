def valid_parenthesis(s: str):
    stk = []
    hashMap = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for i in s:
        if i not in hashMap:
            stk.append(i)
        else:
            if not stk:
                return False
            else:
                popped = stk.pop()

                if hashMap[i] != popped:
                    return False

    if not stk:
        return True

    return False


print(valid_parenthesis('{}[]()'))