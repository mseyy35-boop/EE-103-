# Kullanıcıdan karekökü bulunacak sayıyı (x) ve başlangıç tahminini (g) alıyoruz
x = float(input("What x to find the square root of? "))
g = float(input("What guess to start with? "))

# Mevcut tahminin karesini ekrana yazdırıyoruz
print("Current estimate square:", g ** 2)

# Newton-Raphson formülü ile bir sonraki daha iyi tahmini hesaplıyoruz
next_guess = g - (g**2 - x) / (2 * g)

# Yeni tahmini yazdırıyoruz
print("Next guess:", next_guess)