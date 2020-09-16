# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((next, i + 1))
        elif next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack:
                if not are_matching(opening_brackets_stack.pop()[0],next):
                    return i + 1
            else:
                return i + 1
    return "Success" if not opening_brackets_stack else opening_brackets_stack.pop()[1]

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
