

def isValid(s):
    if len(s) % 2 != 0:
        return False

    pair_mapping = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    open_brackets = list(pair_mapping.keys())

    while len(s)>0:
        for i in range(len(s)):
            if i == len(s) - 1:
                return False
            if s[i] in open_brackets:
                if s[i+1] == pair_mapping[s[i]]:
                    s = s[:i] + s[i+1:]
                    s = s[:i] + s[i+1:]
                    break

    return True


def main():
    s1 = "()"
    print(s1)
    print(isValid(s1))
    print("--"*30)
    s2 = "()[]{}"
    print(s2)
    print(isValid(s2))
    print("--"*30)
    s3 = "(]"
    print(s3)
    print(isValid(s3))
    print("--"*30)
    s4 = "([])"
    print(s4)
    print(isValid(s4))
    print("--"*30)
    s5 = "([)]"
    print(s5)
    print(isValid(s5))
    print("--"*30)
    s6 = "(}{)"
    print(s6)
    print(isValid(s6))
    print("--"*30)
    s7 = "(){}}{"
    print(s7)
    print(isValid(s7))
    print("--"*30)


if __name__ == '__main__':
    main()
    print("Finish")
