def is_palindrome(s: str):
    s_list = [i for i in s]
    print(s_list)
    x = 0
    y = len(s_list) - 1

    while x <= y:
        if s_list[x] != s_list[y]:
            return False

        x += 1
        y -= 1

    return True


print(is_palindrome("tenet"))