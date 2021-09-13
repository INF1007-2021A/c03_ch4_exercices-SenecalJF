#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if len(string)%2 != 0:
        return False
    return True


def remove_third_char(string: str) -> str:
    
    return string[: 2] + string[3:]


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_string = ""
    if len(string) > 0:
        for i in range(len(string)):  
            
            if string[i] == old_char:
                new_string += new_char
            else:
                new_string += string[i]
                
    return new_string


def get_nb_char(string: str, char: str) -> int:
    nb_char = 0
    if len(string) > 0:
        for i in range(len(string)):          
            if string[i] == char:
                nb_char += 1
          
                
    return nb_char


def get_nb_words(sentence: str) -> int:
    i = 0
    for letter in sentence:
        if letter == " ":
            i+=1
    return i+1


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    
    print(f"Le nombre d'occurrence de l dans hello world est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
