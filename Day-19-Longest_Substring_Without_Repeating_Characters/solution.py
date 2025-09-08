

def lengthOfLongestSubstring(s):
    if len(s) <= 1:
        return len(s)

    left_pt = 0
    right_pt = 1
    substring = s[0]

    max_length = 1

    while right_pt < len(s):
        new_char = s[right_pt]
        if new_char in substring:
            max_length = max(max_length, right_pt - left_pt)
            left_pt += 1
            substring = substring[1:]
        else:
            substring += new_char
            right_pt += 1

    return max(max_length, right_pt - left_pt)


def main():
    s = "abcabcbb"
    print(f"s = {s}")
    print(f"expected output = 3")
    print(f"output = {lengthOfLongestSubstring(s)}")
    print("--" * 50)

    s = "bbbbb"
    print(f"s = {s}")
    print(f"expected output = 1")
    print(f"output = {lengthOfLongestSubstring(s)}")
    print("--" * 50)

    s = "pwwkew"
    print(f"s = {s}")
    print(f"expected output = 3")
    print(f"output = {lengthOfLongestSubstring(s)}")
    print("--" * 50)

    s = "au"
    print(f"s = {s}")
    print(f"expected output = 2")
    print(f"output = {lengthOfLongestSubstring(s)}")
    print("--" * 50)


if __name__ == '__main__':
    main()
    print("Finish")
