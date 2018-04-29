while True:
	s = input("Знак (XOR,OR,AND,NOT): ")
	if s == '0': break
	if s in ('XOR','OR','AND'):
		x = int(input("x="))
		y = int(input("y="))
		if s == 'XOR':
			print("%.2f" % (x^y))
		elif s == 'OR':
			print("%.2f" % (x|y))
		elif s == 'AND':
			print("%.2f" % (x&y))
	elif s == 'NOT':
        m = int(input("x="))
        print("x=",(~m))
	else:
		print("Неверный знак операции!")
