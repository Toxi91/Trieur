from Model.modul import *
from Model.domaine import *
import string


def verif(directory):
    if os.path.exists(directory):
        pass
    else:
        print("Le fichier '{}' est introuvable !".format(directory))
        quit()


# fonction qui simplifie les commandes du fichiers domaine dans le dossier model
def _create_txt(x):
    return Domaine.create_txt(x.get_search(), x.get_name(), combo_list)


def _create_txt_not(x):
    return Domaine.create_txt_not(x.get_search(), x.get_name(), combo_list)


def _create_txt_mdp(x):
    return Domaine.create_txt_mdp(x.get_search(), x.get_name(), combo_list)


def _create_txt_mdp_search(x):
    return Domaine.create_txt_mdp_search(x.get_search(), x.get_name(), combo_list)


# fonction pour commencé si oui commence le script sinon ne commence pas
# vérifie si la proposition n'est pas différente de 'Non' sinon recomence la fonction
def start(txt):
    global start_sorte
    start_sorte = str(input("{} (Oui/Non)".format(txt)))
    if start_sorte == "Oui":
        start_sorte = True
    else:
        if start_sorte != "Non":
            print("Je ne vous ai pas compris .")
            return start(txt)
        else:
            start_sorte = False


# fonction pour vérifier si l'utilisateur écrit bien entre les deux propositions possibles (Oui/Non)
def condition(txt):
    global start_sorte
    add_domains_input = str(input("{} (Oui/Non)".format(txt)))
    if add_domains_input == "Non":
        start_sorte = False
    else:
        if add_domains_input != "Oui":
            print("Je ne vous ai pas compris .")
            return condition(txt)
        start_sorte = True


# verifie si les document indispensable au code sont présents sinon ferme le programme
verif("Model/domaine.py")
verif("Model/modul.py")
verif("Combo")
verif("Mdp")

# verifie si le fichier "combo.txt" existe , si oui le lie sinon print(..)
if os.path.exists("combo.txt"):
    with open("combo.txt", "r+") as file:
        combo_list = file.readlines()
        file.close()
else:
    print("Le fichier 'combo.txt' est introuvable !")
    add_combo("Voulez-vous ajouter le fichier 'combo.txt ?")

# trier la combo_list de A -> Z
combo_list.sort()

# Nombre d'élement dans la combo_list
num_lines_combo_list = len(combo_list)
print("Tu as mis une combo de", num_lines_combo_list)

# execute la fonction de_dupli qui verifie si 2 arguments sont identique et les enleves
combo_list = del_dupli(combo_list)

# Nombre d'élement dans la combo_list
num_lines_combo_dup_list = len(combo_list)
print("On a supprimé", num_lines_combo_list - num_lines_combo_dup_list, "duplication !")

# fonction pour creer un fichier txt sans duplie
# create_txt_dupli(combo_list)

# fonction pour commencer a ajouté une nouvelle recherche
start("Voulez-vous ajoutez une nouvelle recherche ?")

# tant que 'start_sorte est 'True' se repete
while start_sorte:
    #
    add_domaine_input = input("Veuiller entrer la recherche , et le nom ex:(.com: COM)").split(" ")

    add_domaine = Domaine(add_domaine_input[0], add_domaine_input[1], combo_list)

    _create_txt(add_domaine)

    condition("Voulez-vous ajoutez une nouvelle recherche ?")

# fonction pour commencer a ajouté une nouvelle recherche en fonction des mots de passes
start("Voulez-vous ajoutez une nouvelle recherche en fonction du mot de passe ?")

# tant que 'start_sorte est 'True' se repete
while start_sorte:
    add_domaine_input = input("Veuiller entrer la recherche , et le nom ex:(pass Pass)").split(" ")

    add_domaine = Domaine(add_domaine_input[0], add_domaine_input[1], combo_list)

    _create_txt_mdp_search(add_domaine)

    condition("Voulez-vous ajoutez une nouvelle recherche ?")

# fonction pour commencer a utilisé les recherches de tries par défault
start("Voulez-vous utilisé les recherches de tries par défault ?")

# tant que 'start_sorte est 'True' se repete
while start_sorte:

    # Domaine par défault
    fr = Domaine(".fr:", "FR", combo_list)
    com = Domaine(".com:", "COM", combo_list)
    net = Domaine(".net:", "NET", combo_list)
    user = Domaine("@", "user", combo_list)

    # def pour simplifié create_txt qui vérifie si le txt existe , et d'apres combo_list qui cherche d'apres la
    # recherche , et enfin regarde les lignes du txt si oui ou non est remplie et l'affiche
    _create_txt(fr)

    _create_txt(com)

    _create_txt(net)

    _create_txt_not(user)

    condition("Voulez-vous le reste ?")

    if start_sorte is True:
        #    a simplifié
        if os.path.exists(divers):
            os.remove(divers)
        for combo in combo_list:
            # for num in range(0 , len(all_search)): = de 0 à 3 a devellopé pour le faire automatique
            if fr.get_search() not in combo:
                if com.get_search() not in combo:
                    if net.get_search() not in combo:
                        if user.get_search() in combo:
                            with open(divers, "a+") as file:
                                file.write(combo)
                                file.close()
        # fonction qui regarde les lignes du txt si oui ou non est remplie et l'affiche .
        exist(divers)

    # Variable 'start_sorte' en 'False'
    start_sorte = False

# fonction pour lancer le triage des mots de passes
start("Voulez-vous utilisé les recherches de tries en fonction des mots de passes par défault ?")

upper_punct = (string.ascii_uppercase + string.punctuation)

# tant que 'start_sorte est 'True' se repete
while start_sorte:
    upper = Domaine(string.ascii_uppercase, "uppercase", combo_list)
    punct = Domaine(string.punctuation, "punctuation", combo_list)

    _create_txt_mdp(upper)
    _create_txt_mdp(punct)

    time.sleep(10)
    start_sorte = False


