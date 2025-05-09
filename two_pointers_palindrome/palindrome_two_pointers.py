# Objectif :
# Écrire une fonction qui vérifie si une chaîne de caractères est un palindrome
# en utilisant l'approche des deux pointeurs


# La complexité temporelle est O(n), où n est le nombre de caractères dans la chaîne.
# Cependant, notre algorithme ne fera qu'environ n/2 itérations, puisque les deux pointeurs
# se déplacent l'un vers l'autre à chaque étape.

#La complexité spatiale est O(1'), puisque nous utilisons un espace constant pour stocker deux index.


def is_palindrome(s):
    left = 0 
    right = len(s) - 1
    
    while left < right: 
        if s[left] != s[right]: 
            return False
        left += 1
        right -= 1
        
    return True

def main():

    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("The input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".", sep='')
        print("Is it a palindrome?.....", is_palindrome(test_cases[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
