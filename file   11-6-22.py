
f = open("file.txt", "r")
print(f.read())

f = open("file.txt", "r")
print(f.read(5))

f = open("file.txt", "r")
print(f.readline())

f = open("file.txt", "r")
for x in f:
  print(x)


f = open("file.txt", "r")
print(f.readline())
f.close()

f = open("file.txt", "a")
f.write("what are you doing")
f.close()

f = open("file.txt", "r")
print(f.read())
