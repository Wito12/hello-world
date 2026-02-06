tab = [4, 6, 2, 1, 3]
max_val = tab[0]

for i in range(1, len(tab)):
    if tab[i] > max_val:
        max_val = tab[i]

print(max_val)

#Nie obsluguje pustych tablic. ale można by dodać 
#if len(tab) == 0:
#       return None  # Tablica jest pusta
#Wymaga jednokrotnego przejścia przez całą tablicę, co daje złożoność czasową O(n).
