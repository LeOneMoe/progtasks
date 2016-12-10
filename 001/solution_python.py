import sys

def abbreviations(word):
   if len(word) > 10:
       return "{0}{1}{2}".format(word[0], len(word) - 2 ,word[-1])
   else:
       return word

if __name__ == "__main__":

    for line in sys.stdin:
        print(abbreviations(line.strip("\n")))
