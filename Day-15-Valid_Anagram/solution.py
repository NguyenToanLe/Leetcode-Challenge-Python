

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    if len(s) == 1 and s != t:
        return False

    letter_count_s = {}
    for letter in s:
        if letter not in letter_count_s:
            letter_count_s[letter] = 1
        else:
            letter_count_s[letter] += 1

    letter_count_t = {}
    for letter in t:
        if letter not in letter_count_s:    # There is a letter that is not in s
            return False

        if letter not in letter_count_t:
            letter_count_t[letter] = 1
        else:
            letter_count_t[letter] += 1

        if letter_count_t[letter] > letter_count_s[letter]:     # This letter occurs more in t than in s
            return False

    return True


def main():
    s = "anagram"
    t = "nagaram"
    print(f"s = {s}, t = {t}")
    print(f"expected output = true")
    print(f"output = {isAnagram(s, t)}")
    print("--" * 50)

    s = "rat"
    t = "car"
    print(f"s = {s}, t = {t}")
    print(f"expected output = false")
    print(f"output = {isAnagram(s, t)}")
    print("--" * 50)


if __name__ == '__main__':
    main()
    print("Finish")
