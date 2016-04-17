# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    index = []
    for i, next in enumerate(text):
        match = True
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i))
            index.append(i+1)

        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0 or opening_brackets_stack.pop().Match(next) == False:
                match = False
                index.append(i+1)
                break
            index.pop()
            # Process closing bracket, write your code here
    # Printing answer, write your code here
    if match == False or len(opening_brackets_stack) > 0:
        print(index.pop())
    else:
        print("Success")