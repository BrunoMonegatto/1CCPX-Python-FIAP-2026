def ler_nota(nome):
    while True:
        try:
            nota = float(input(f"Digite a nota da {nome}: "))

            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida, digite um valor entre 0 e 10.")

        except ValueError:
            print("Entrada inválida, digite um número.")


# Leitura das notas
cp1 = ler_nota("CP 01")
cp2 = ler_nota("CP 02")
cp3 = ler_nota("CP 03")
sp1 = ler_nota("Sprint 01")
sp2 = ler_nota("Sprint 02")
gs = ler_nota("GS")
