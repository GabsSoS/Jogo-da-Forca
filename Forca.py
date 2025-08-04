palavra_secreta = "Pneumoultramicroscopicossilicovulcanoconiótico"
letras_descobertas = []
tentativas = 5

print("Vamos jogar forca!!!")

while True:
    exibido = ""
    for letra in palavra_secreta:
        if letra in letras_descobertas:
            exibido += letra
        else:
            exibido += "_"

    print(f"\nPalavra: {exibido}")

    if "_" not in exibido:
        print("Parabéns! Você venceu!!!")
        break

    tentativa = input("Digite uma letra: ").lower()

    if not tentativa.isalpha() or len(tentativa) != 1:
        print("Digite apenas UMA letra.")
        continue

    if tentativa in palavra_secreta:
        if tentativa in letras_descobertas:
            print("Você já tentou essa letra.")
        else:
            print("✅ Acertou!")
            letras_descobertas.append(tentativa)
    else:
        tentativas -= 1
        print(f"Errou! Tentativas restantes: {tentativas}")

    if tentativas == 0:
        print("X Você perdeu! X")
        print("A palavra era:", palavra_secreta)
        break
