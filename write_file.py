py_file = open("python_intro.txt", "r+")

content = py_file.read()

print(content)

py_file.write("Python is a versatile programming language.\n")

py_file.close()

