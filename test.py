x = 0
y = 0
while (compass := input()) != "СТОП":
    steps = int(input())
    if compass == "СЕВЕР":
        y += steps
    elif compass == "ЮГ":
        y -= steps
    elif compass == "ЗАПАД":
        x -= steps
    elif compass == "ВОСТОК":
        x += steps
print(y)
print(x)