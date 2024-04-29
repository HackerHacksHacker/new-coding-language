import lamp

while True:
		text = input('lamp > ')
		result, error = lamp.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)
