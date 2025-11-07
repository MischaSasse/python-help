# Onder statements vallen diverse manieren om te checken of iets waar is of niet.

x = 5
check = 10

y = f"this is true, {x} is less than {check}"
# f"" is een 'formatted string'. 
# Hierdoor kan je variabelen en berekeningen maken en deze waarden laten zien in je string

if x < check:
    print(y)

elif x == check:
    print(f"{x} == {check}")

else:
    print("%s is greater than %s" %(x, check))

# %s is een operator in python wat ervoor zorgt dat je waardes mee kan geven, een beetje zoals een f-string.
# Je zal dit vooral gebruiken om ervoor te zorgen dat er geen SQL-injections plaats kunnen vinden in je code.
# SQL-injections zijn manieren om door middel van je code, van buiten af, queries te runnen. 
# Mocht dit niet goed beveiligd zijn, dan kan het bijvoorbeeld zijn dat je database in eens leeg is.

# --------------------------------

# Ook zijn er AND, OR en NOT operators. zie de voorbeelden hieronder
if 1 < x and 1 > -check:
    print(f"1 is kleiner dan {x} en ook groter dan {-check}")

if 1 > 10 or x > 0:
    print(f"of 1 is groter dan 10, of {x} is groter dan 0")

if x != check:
    print(f"{x} en {check} zijn niet hetzelfde") 
      
# Voor de mensen die al iets meer kennis hebben en betere code willen schrijven:
wifi = True
login = True
admin = False

def seeAdminPanel() :
    return
    
def anyFunction():
    if wifi:
        if login:
            if admin:
                seeAdminPanel()
            else:
                print("must be an admin")
        else:
            print("must be logged in")
    else: 
        print("must be connected to wifi")


def betterFunction():
    if not wifi:
        print("must be connected to wifi")
        return
    if not login:
        print("must be logged in")
        return
    if not admin:
        print("must be an admin")
        return
    seeAdminPanel()
    
# anyFunction()