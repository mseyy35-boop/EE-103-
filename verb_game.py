
# Kullanıcıdan bir fiil girmesini istiyoruz
verb = input("Please enter a verb: ")

# Aldığımız fiili cümlenin içine yerleştiriyoruz
print(f"I can {verb} better than you!")

# Fiilin sonuna bir boşluk ekleyip 5 ile çarparak aralarında boşlukla 5 kez yazdırıyoruz
print((verb + " ") * 5)