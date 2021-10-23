

greenwich = 0 #Variable globale initialisée à 0


def calculHeure(decalage):

    #Vérification du décalage

    if decalage < -12 or decalage > 12:
        print("Erreur : fuseau horaire inexistant !!")
        exit(2)


    #Calcul de l'heure

    global greenwich #greenwich est la variable globale définie dans un input du main

    calcul = greenwich + decalage


    if calcul >= 0 and calcul <= 23:
        return calcul
        #Après application du décalage, il est entre 0 et 23 heures à l'heure locale

    elif calcul == 24:
        calcul = 0
        return calcul
        #S'il est 23h à Greenwich, il sera minuit à Paris (fuseau horaire + 1 en heure d'hiver)

    elif calcul < 0:
        return 24 + calcul
        #S'il est minuit à Greenwich et que vous êtes à New York (fuseau horaire -5 en heure d'hiver),
        #il sera 24 + (-5) = 19 heures dans la Grosse Pomme

    elif calcul > 23:
        return calcul -24
        #S'il est 23 heures à Greenwich et que vous êtes à Tokyo (fuseau horaire + 9),
        #la variable calcul vaudra 23 + 9 = 32 heures !!!
        #Pour résoudre ce problème on fait 32 - 24 = 8 heures à Tokyo

    else:
        print("Bug inattendu !!!")
        exit(3)





#Programme principal

def main():

    #Présentation et explications sur l'heure d'été

    print("Bonjour dans mon programme sur le décalage horaire")
    print()

    print("Note : ce programme ne tient pas compte de l'heure d'été.")
    print("L'heure de référence est l'heure d'hiver")
    print()

    print("Si vous êtes en heure d'été, ajoutez 1 heure aux villes en Amérique du Nord et en Europe (Russie et Islande exclues).")
    print("Sauf exceptions, les autres régions du monde n'observent pas l'heure d'été : l'heure reste donc inchangée tout au long de l'année")
    print()


    #Choix de l'heure à Greenwich

    global greenwich #On appelle la variable globale greenwich car on va la modifier


    greenwich = int(input("Quelle est l'heure à Greenwich ?\n(Choisissez un entier entre 0 et 23) : "))


    #Vérification de l'heure à Greenwich

    if greenwich < 0 or greenwich > 23:
        print("Erreur : heure non valide !!")
        exit(1)


    #Affichage des heures locales

    print(f"Il est {greenwich} heures à Londres, {calculHeure(+1)} heures à Paris, {calculHeure(+2)} heures à Athènes...\n")

    print(f"Il est {calculHeure(-8)} heures à Los Angeles, {calculHeure(-5)} heures à New York et Montréal, {calculHeure(-3)} heures à Rio de Janeiro...\n")

    print(f"Il est {calculHeure(+3)} heures à Moscou, {calculHeure(+4)} heures à Dubaï, {calculHeure(+5)} heures et demie à New Delhi...\n")
    print(f"Il est {calculHeure(+3)} heures à Pékin, {calculHeure(+4)} heures à Tokyo et Séoul, {calculHeure(+10)} heures à Sydney...\n")


#Appel de la fonction main

main()
