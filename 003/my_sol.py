def is_balanced(string):
    open_brackets = ("(", "[", "{")
    close_brackets = (")", "]", "}")
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for letter in string:
        if letter in open_brackets:
            stack.append(letter)
        elif letter in close_brackets:
            try:
                last = stack.pop()
            except IndexError:
                return False

            if last != pairs[letter]:
                stack.append(last)

    return not len(stack)
