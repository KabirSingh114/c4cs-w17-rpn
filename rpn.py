#!/usr/bin/env python3

import operator

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv
}

def calculate(arg):
	List = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			List.append(operand)
		except ValueError:
			num1 = List.pop()
			num2 = List.pop()
			List.append(operators[operand](num1, num2))
	return List.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
