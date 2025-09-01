

def isPalindrome(s):
    if len(s) == 1:
        return True

    import re
    regex = re.compile('[^a-zA-Z0-9]')
    s = regex.sub('', s)
    s = s.lower()

    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False

    return True


def main():
    s = "A man, a plan, a canal: Panama"
    print(f"s = {s}")
    print(f"expected output = true")
    print(f"output = {isPalindrome(s)}")
    print("--" * 50)

    s = "race a car"
    print(f"s = {s}")
    print(f"expected output = false")
    print(f"output = {isPalindrome(s)}")
    print("--" * 50)

    s = " "
    print(f"s = {s}")
    print(f"expected output = true")
    print(f"output = {isPalindrome(s)}")
    print("--" * 50)


if __name__ == '__main__':
    main()
    print("Finish")
