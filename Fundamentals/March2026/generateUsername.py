def generate_name(first_name, last_name, birth_year):
	fn = first_name.replace(" ", "").lower()
	ln = last_name.replace(" ", "").lower()

	if len(fn) < 3:
		first = fn
	else:
		first = fn[:3]

	if len(ln) < 3:
		last = ln
	else:
		last = ln[:3]

	dStr = str(birth_year)
	date = dStr[2:]
	return first, last, date

user = generate_name("John", "Doe", 2026)
username = "".join(str(item) for item in user)
print(username)
