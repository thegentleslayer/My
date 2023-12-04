import re
import random

def my_algorithm(chemin_fichier):
    correspondance_lettres = {
        'a': 'أ',
        'b': 'Б',
        'c': 'シ',
        'd': 'د',
        'e': 'イ',
        'f': 'ف',
        'g': 'ج',
        'h': 'ハ',
        'i': 'И',
        'j': 'ジ',
        'k': 'ك',
        'l': 'Л',
        'm': 'م',
        'n': 'Н',
        'o': 'オ',
        'p': 'П',
        'q': 'ق',
        'r': 'Р',
        's': 'セ',
        't': 'ت',
        'u': 'У',
        'v': 'В',
        'w': 'و',
        'x': 'كس',
        'y': 'У',
        'z': 'ز',
        'A': 'أ',
        'B': 'Б',
        'C': 'シ',
        'D': 'د',
        'E': 'イ',
        'F': 'ف',
        'G': 'ج',
        'H': 'ハ',
        'I': 'И',
        'J': 'ジ',
        'K': 'ك',
        'L': 'Л',
        'M': 'م',
        'N': 'Н',
        'O': 'オ',
        'P': 'П',
        'Q': 'ق',
        'R': 'Р',
        'S': 'セ',
        'T': 'ت',
        'U': 'У',
        'V': 'В',
        'W': 'و',
        'X': 'كس',
        'Y': 'У',
        'Z': 'ز'
    }

    def substituer_lettre(lettre):
        return correspondance_lettres.get(lettre, lettre)

    def traduire_substitution(caractere_chiffre):
        correspondance_inverse = {v: k for k, v in correspondance_lettres.items()}
        return correspondance_inverse.get(caractere_chiffre, caractere_chiffre)

    def chiffrement_substitution(message):
        return ''.join(substituer_lettre(caractere) for caractere in message)

    def chiffrement_substitution_fichier(chemin_fichier):
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu_original = fichier.read()
                contenu_chiffre = chiffrement_substitution(contenu_original)
                print(f"Résultat de la première substitution:\n{contenu_chiffre}\n")
                contenu_mele = decoupage_et_melange(contenu_chiffre)
                print(f"Résultat du découpage et du mélange:\n{contenu_mele}")
                return contenu_mele
        except FileNotFoundError:
            return f"Le fichier {chemin_fichier} n'a pas été trouvé."

    def decoupage_et_melange(texte_chiffre):
        morceaux = re.findall(r'\b\w+\b', texte_chiffre)
        morceaux = [(morceau, i) for i, morceau in enumerate(morceaux)]
        random.shuffle(morceaux)
        morceaux = sorted(morceaux, key=lambda x: x[1])
        texte_mele = ' '.join(morceau[0] for morceau in morceaux)
        return texte_mele

    def dechiffrement(texte_mele):
        morceaux = re.findall(r'\b\w+\b', texte_mele)
        morceaux = [(morceau, i) for i, morceau in enumerate(morceaux)]
        morceaux = sorted(morceaux, key=lambda x: x[1])
        texte_demelange = ' '.join(morceau[0] for morceau in morceaux)
        texte_substitution = ''.join(traduire_substitution(caractere) for caractere in texte_demelange)
        return texte_substitution

    chemin_fichier = 'texte.txt'
    message_chiffre_mele = chiffrement_substitution_fichier(chemin_fichier)
    texte_dechiffre = dechiffrement(message_chiffre_mele)
    print(f"Texte déchiffré : {texte_dechiffre}")

# Appeler la fonction globale avec le chemin du fichier
chemin_fichier = 'texte.txt'
my_algorithm(chemin_fichier)
