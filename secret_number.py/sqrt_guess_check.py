# Kullanıcıdan tam sayı alıyoruz
given_number = int(input("Enter an integer: "))

# c) Negatif sayı kontrolü
if given_number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    guess_number = 1
    
    # a) & b) Tahminin karesi verilen sayıdan küçük olduğu sürece tahmini 1 artırıyoruz
    while guess_number ** 2 < given_number:
        guess_number += 1
    
    # Döngü bittiğinde karesi sayıya eşit mi diye bakıyoruz
    if guess_number ** 2 == given_number:
        print(f"The square root of {given_number} is {guess_number}")
    else:
        print(f"{given_number} is not a perfect square.")