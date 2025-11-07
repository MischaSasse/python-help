# Maak een list aan met 5 unieke elementen
items = ['a', 'b', 'c', 'd', 'e']

# Print de hele list (dit laat Python het lijst-object tonen)
print(items)

# Zorg ervoor dat het niet uitmaakt hoe lang de list is.
# Gebruik range(len(...)) om door elke waarde te lopen en gebruik de index om
# het element te printen. Dit is nuttig als je de index nodig hebt.
for i in range(len(items)):
    print(f"index {i} -> {items[i]}")