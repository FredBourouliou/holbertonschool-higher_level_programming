#!/usr/bin/python3
from 101-lazy_matrix_mul import lazy_matrix_mul

# Test 1: Multiplication normale
print("Test 1: Multiplication normale")
print(lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
# Devrait afficher:
# [[19 22]
#  [43 50]]

# Test 2: Multiplication avec une ligne
print("\nTest 2: Multiplication avec une ligne")
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
# Devrait afficher:
# [[13 16]]

# Test 3: Test avec des flottants
print("\nTest 3: Test avec des flottants")
print(lazy_matrix_mul([[1.5, 2.5]], [[3.0, 4.0], [5.0, 6.0]]))

# Test 4: Test d'erreur - matrice non valide
print("\nTest 4: Test d'erreur - matrice non valide")
try:
    print(lazy_matrix_mul("Holberton", [[5, 6], [7, 8]]))
except TypeError as e:
    print(e)

# Test 5: Test d'erreur - matrice vide
print("\nTest 5: Test d'erreur - matrice vide")
try:
    print(lazy_matrix_mul([[]], [[5, 6], [7, 8]]))
except ValueError as e:
    print(e)

# Test 6: Test d'erreur - élément non numérique
print("\nTest 6: Test d'erreur - élément non numérique")
try:
    print(lazy_matrix_mul([[1, "2"]], [[3, 4], [5, 6]]))
except TypeError as e:
    print(e)

# Test 7: Test d'erreur - tailles incompatibles
print("\nTest 7: Test d'erreur - tailles incompatibles")
try:
    print(lazy_matrix_mul([[1, 2, 3]], [[1, 2], [3, 4]]))
except ValueError as e:
    print(e) 