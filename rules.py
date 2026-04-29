def is_even(number: int) -> bool: #Verifica se un numero è pari utilizzando l'operatore modulo.
    return number % 2 == 0


def is_vowel(letter: str) -> bool: #Verifica se una lettera è una vocale, rendendola prima maiuscola.
    return letter.upper() in "AEIOU"


def compute_expected_answer(position: str, letter: str, number: int) -> bool: # Determina la risposta corretta in base alla posizione dello stimolo:
    # Se in alto (TOP): la risposta dipende dal fatto che il numero sia pari.
    # Se in basso (BOTTOM): la risposta dipende dal fatto che la lettera sia una vocale.

    if position == "TOP":
        # Regola per la posizione superiore: focus sul numero
        return is_even(number)

    # Se la posizione non è TOP (quindi è BOTTOM), focus sulla lettera
    return is_vowel(letter)
