#assign a name including whitespace characters to a variable then print it using lstrip, rstrip, strip on the variable each once.

name = "    shit fart\t\n\tthe narrator\t"

print(name)

print(f"{name.lstrip()}\n{name.rstrip()}\n{name.strip()}")