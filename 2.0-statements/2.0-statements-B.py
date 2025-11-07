"""
Oefeningen: if / if-else / if-elif-else

Bij elke oefening: verander de variabelen onderaan de oefening zodat het programma
de tekst "juist" (of vergelijkbare bevestiging) print. Elke oefening bevat een
kort hint/verwachte uitkomst in de commentaren.

Verander alleen de waarden van de variabelen (en/of het type) om te oefenen.
"""

# ---- Oefening 1: eenvoudige if (geen else) ----
# Doel: leer dat een if-blok alleen uitgevoerd wordt als de conditie True is.
# Verander 'number' zodat de conditie (number % 2 == 0) True wordt.
number = 3  # zet bijvoorbeeld 4 om de if-branch te triggeren

if number % 2 == 0:
    print("Oefening 1: goed gedaan — number is even")

# (Geen else hier opzettelijk: als de conditie False is gebeurt er niets.)


# ---- Oefening 2: if-else ----
# Doel: kies tussen twee paden — controleer een eenvoudig wachtwoord.
# Verander 'pw' zodat het matcht met 'geheim123' om de "juist"-tekst te zien.
pw = "verkeerd"  # wijzig naar 'geheim123' om de juiste uitkomst te krijgen

if pw == "geheim123":
    print("Oefening 2: succes — wachtwoord klopt")
else:
    print("Oefening 2: try again :c — wachtwoord klopt niet")


# ---- Oefening 3: if-elif-else ----
# Doel: gebruik meerdere voorwaarden (bijv. cijfers -> beoordeling).
# Verander 'score' naar een getal tussen 0 en 100.
# Verwachte uitkomst voorbeelden:
#  score >= 90 -> "A"
#  75 <= score < 90 -> "B"
#  60 <= score < 75 -> "C"
#  anders -> "F"
score = 72

if score >= 90:
    grade = "A"
    remark = "Uitstekend"
elif score >= 75:
    grade = "B"
    remark = "Goed"
elif score >= 60:
    grade = "C"
    remark = "Voldoende"
else:
    grade = "F"
    remark = "Onvoldoende"

print(f"Oefening 3: score={score} -> grade={grade} ({remark})")


if __name__ == '__main__':
    print("\nKlaar — pas variabelen aan bovenaan elke oefening en run opnieuw.")