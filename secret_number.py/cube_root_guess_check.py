# Kullanıcıdan tam sayı alıyoruz
given_number = int(input("Enter an integer: "))

# Sayının mutlak değerini (işaretsiz halini) alıyoruz
abs_number = abs(given_number)

guess_number = 0

# Tahminin küpü sayıdan küçük olduğu sürece tahmini 1 artırıyoruz
while guess_number ** 3 < abs_number:
    guess_number += 1

# Tahminin küpü mutlak değere eşit mi kontrol ediyoruz
if guess_number ** 3 == abs_number:
    # Sayı başlangıçta negatifse sonucun işaretini eksi yapıyoruz
    if given_number < 0:
        guess_number = -guess_number
    print(f"The cube root of {given_number} is {guess_number}")
else:
    print(f"{given_number} is not a perfect cube.")
