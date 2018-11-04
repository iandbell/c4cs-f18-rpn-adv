#!/usr/bin/env python3

from termcolor import colored
import readline

def calculate(arg):
    stack = []
    text = ''
    tokens = arg.split()

    for token in tokens:
       try:
            stack.append(int(token))
            if int(token) < 0:
                text += colored(token, 'red') + ' '
            else:
                text += token + ' '
       except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            elif token == '^':
                result = val1 ** val2
            stack.append(result)
            text += colored(token, 'blue') + ' '
    if len(stack) > 1:
        raise ValueError('Too many arguments on the stack, dummy')

    print(text)
    return stack[0]

def main():
    while True:
        try:
            result = calculate(input("rpn calc> "))
            print(result)
        except ValueError:
            pass

if __name__ == '__main__':
    main()
