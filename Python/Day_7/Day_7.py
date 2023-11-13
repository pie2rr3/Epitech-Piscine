import random
import datetime

def get_list_of_words(path):
    with open(path, 'r') as f:
        return f.read().splitlines()

def get_best_score(mot):
    try:
        with open("best_scores.txt", "r") as fichier:
            scores = fichier.readlines()
            for line in scores:
                parts = line.strip().split(':')
                if len(parts) == 2 and parts[0] == mot:
                    return int(parts[1])
    except FileNotFoundError:
        return None

def update_best_score(mot, score):
    best_score = get_best_score(mot)
    if best_score is None or score < best_score:
        with open("best_scores.txt", "a") as fichier:
            fichier.write(f"{mot}:{score}\n")

def hangman():
    mot_liste = get_list_of_words("r.txt")
    
    mot = random.choice(mot_liste).lower()
    mot_secret = "_" * len(mot)
    lettre_utilisé = []
    
    print("Salut on va jouer au pendu \nLe mot à deviner a", len(mot), "lettres")
    
    nombre_essais = 0
    
    while nombre_essais < 11:
        a = input("Trouve une lettre : ").lower()
        
        if a == mot:
            return print("Bravo ct ca t'as réussi, t'as triché ou quoi ? ")
        
        if a in lettre_utilisé:
            print("Tu as déjà essayé la lettre", a, "gros con 😂")
            continue
        
        if a in mot:
            mot_secret_liste = list(mot_secret)
            for i in range(len(mot)):
                if mot[i] == a:
                    mot_secret_liste[i] = a
            mot_secret = "".join(mot_secret_liste)
            print(" ".join(mot_secret))
        
            if mot_secret == mot:
                nombre_essais += 1
                print(f"Ok t chaud t'as trouvé ct '{mot}', t'as réussi en {nombre_essais} essai(s).")
                update_best_score(mot, nombre_essais)
                break
        else:
            print("La lettre n'est pas dans le mot sal merde ")
            print(" ".join(mot_secret))
            nombre_essais += 1
            lettre_utilisé.append(a)
            print("Il te reste :", 11 - nombre_essais, "essai(s)")

    if nombre_essais == 11:
        print("T trop guez igo le mot ct : ", mot)

    best_score = get_best_score(mot)
    if best_score is not None:
        if nombre_essais < best_score:
            print(f"RECORD DU MONDE POUR LE MOT'{mot}' EN {nombre_essais} ESSAIS !!")
        else:
            print(f"Tu as deviné le mot '{mot}' en {nombre_essais} essais gros nulos 🥱 \nLe record est de {best_score} essais et tu l'atteindras jamais")

hangman()
