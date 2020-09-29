w_  = input("Qual a primeira palavra a ser escolhida? ")
w__ = input("Qual a segunda palavra a ser escolhido? ")

w_  = w_ [::-1]


if (w_ != w__):
    print("As duas palavras não são iguais.")

elif (w_ == w__):
    print("As palavras estão invertidas e também são iguais.")
