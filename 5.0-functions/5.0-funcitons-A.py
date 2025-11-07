# Een function is een manier om code in een blok te schrijven, wat herhaalbaar is
# voor extra kennis, een functie zonder return heet een procedure (idk of jullie dat nodig hebben qua kennis tho)
def multiplyToConsole(a:int, b:int) -> None:
    print(a*b)  
    
def multiply(a:int, b:int) -> int:
    return a*b

# een functie runt alleen de code ervan wanneer er een call naar wordt gemaakt zoals hieronder.
multiplyToConsole(5,6)

print(multiply(5,4))

# Hierdoor kan je ervoor zorgen dat je herhaling in je code voorkomt.
# Daardoor is het een stuk beter te lezen en ook een stuk makkelijker aan te passen.

# functies kunnen ook een default waarde hebben
def showName(name="Bob"):
    print(f"Hello {name}")
    
myName = "John Doe"
showName()
showName(myName)

# functies kunnen ook zichzelf aanroepen (recursion)
def factorial(number:int):
    if number == 1:
        return 1
    return number * factorial(number-1)

print(factorial(5))