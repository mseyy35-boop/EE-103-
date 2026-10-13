# from secret_number import secretNum
#
# guess = int(input("Bir sayi tahmin et: "))

# if guess < secretNum:
#    print("Cok kucuk!")
# elif guess > secretNum:
#    print("Cok buyuk!")
# else:
#   print("Tebrikler, dogru tahmin!") 

from secret_number import secretNum

attempts = 0

while True:
    guess = int(input("Guess the secret number: "))
    attempts = attempts + 1

    if guess == secretNum:
        print("Tebrikler, buldun!")
        break
    elif guess < secretNum:
        print("Too low!")
    else:
        print("Too high!")

    # 5. yanlis tahminden sonra:
    if attempts == 5:
        break

# Eger 5 denemede dogru bulunamadiysa sonsuz donguye girer:
if guess != secretNum:
    while True:
        print("Oh! Noooooo...")