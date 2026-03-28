# Problem: Longest Common Prefix (LeetCode #14)
# Difficulty: Easy
# Time Complexity: O(S), où S est la somme de tous les caractères dans toutes les chaînes.
# Space Complexity: O(1), car nous n'utilisons pas d'espace supplémentaire proportionnel à l'entrée.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Trouve le plus long préfixe commun parmi un tableau de chaînes.
        Méthode : Scan horizontal / Caractère par caractère.
        """
        # Si le tableau est vide, il n'y a pas de préfixe commun
        if not strs:
            return ""
        
        # On itère sur les caractères de la première chaîne
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # On compare ce caractère avec le même index dans les autres chaînes
            for string in strs[1:]:
                # Si on dépasse la taille d'une chaîne ou que le caractère diffère
                if i == len(string) or string[i] != char:
                    return strs[0][:i]
                
        return strs[0]