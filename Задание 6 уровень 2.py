a = -4.0
b = 4.0
s = 0.5
print("x | y(x)")
print("-" * 10)
i = a
while i <= b:
  y = 0.5 * i**2 - 7 * i
  print(i, "|", y)
  i += s
