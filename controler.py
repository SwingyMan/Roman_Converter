x = open("in/in.txt", "r").read().splitlines()
y = open("out/out.txt", "w")
import main
for letter in x:
    z = main.convert(letter)
    y.writelines(str(z) + "\n")
y.close()