# Globale veranderlike om die laaste antwoord te stoor
# Funksie om twee getalle bymekaar te tel
laaste_antwoord = None

def optel(a, b):
    return a + b

# Funksie om twee getalle af te trek
def aftrek(a, b):
    return a - b

# Funksie om twee getalle te vermenigvuldig
def maal(a, b):
    return a * b

# Funksie om twee getalle te deel
def deel(a, b):
    if b == 0:
        return "Kan nie deur nul deel nie"
    else:
        return a / b

# Funksie om die uitset te verwyder
def verwyder():
    global laaste_antwoord
    if laaste_antwoord is not None:
        laaste_antwoord = None
        print("\nLaaste antwoord is verwyder.\n")
    else:
        print("\nDaar is geen laaste antwoord om te verwyder nie.\n")

# Hoofprogram
def main():
    global laaste_antwoord
    print("Welkom by die eenvoudige sakrekenaar!")
    sentinel = False  # Sentinel variable om die "loop" te stop
    while not sentinel:
        print("\nKies 'n operasie:")
        print("1. Optel (+)")
        print("2. Aftrek (-)")
        print("3. Vermenigvuldig (*)")
        print("4. Deel (/)")
        print("5. Uitset verwyder")
        print("6. Verlaat")
        
        keuse = input("\nJou keuse: ")

        if keuse == '6':
            print("Dankie vir die gebruik van die sakrekenaar. Tot volgende keer!")
            sentinel = True
        elif keuse in ('1', '2', '3', '4'):
            num1 = float(input("\nVoer die eerste getal in: "))
            num2 = float(input("Voer die tweede getal in: "))
            if keuse == '1':
                laaste_antwoord = optel(num1, num2)
                print("Die antwoord is:", laaste_antwoord)
            elif keuse == '2':
                laaste_antwoord = aftrek(num1, num2)
                print("Die antwoord is:", laaste_antwoord)
            elif keuse == '3':
                laaste_antwoord = maal(num1, num2)
                print("Die antwoord is:", laaste_antwoord)
            elif keuse == '4':
                laaste_antwoord = deel(num1, num2)
                print("Die antwoord is:", laaste_antwoord)
        elif keuse == '5':
            verwyder()
        else:
            print("Ongeldige keuse. Probeer asseblief weer.")

if __name__ == "__main__":
    main()