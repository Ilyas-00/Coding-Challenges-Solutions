# Objectif :
# Écrire une fonction qui vérifie si une chaîne de caractères est un palindrome
# en utilisant l'approche des deux pointeurs

def is_palindrome(s):
    left = 0 
    right = len(s) - 1
    
    while left < right: 
        if s[left] != s[right]: 
            return False
        left += 1
        right -= 1
        
    return True