n = int(input("enter a no: "))
y = n % 2
if y == 1:
        print('Weird')
elif y == 0 and n in range(2, 6):
        print("not weird")
elif y == 0 and n in range(6, 21):
        print('Weird')
elif y == 0 and n > 20:
        print('Not Weird')
