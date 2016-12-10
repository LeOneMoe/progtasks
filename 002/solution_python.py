import sys

VOWELS = ("a", "o", "y", "e",
          "u", "i", "A", "O",
          "Y", "E", "U", "I")


def sokraschatel(word):
    word = word.lower()
    temp = ""
    for letter in word:
        if letter not in VOWELS:
            temp += "." + letter
    return temp

if __name__ == "__main__":

    for line in sys.stdin:
        print(sokraschatel(line.strip("\n")))
