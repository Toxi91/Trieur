import os
import time


def add_combo(txt):
    add_combo_input = str(input("{} (Oui/Non)".format(txt)))
    if add_combo_input == "Oui":
        with open("combo.txt", "a+") as FILE:
            FILE.write("Mettez votre combo !")
            FILE.close()
        print("Veuillez ajouter une combo svp !")
        time.sleep(5)
        quit()
    elif add_combo_input != "Non":
        print("Je ne vous ai pas compris .")
        return add_combo(txt)
    else:
        quit()


def del_dupli(x):
    return list(dict.fromkeys(x))


def create_txt_dupli(x):
    if os.path.exists(combo_dupli):
        os.remove(combo_dupli)
    for combo in x:
        with open(combo_dupli, "a+") as file:
            file.write(combo)
            file.close()


def exist(name):
    if os.path.exists(name) is not False:
        # Nombre de ligne dans la combo
        num_lines_combo = sum(1 for line in open(name))
        print("Il y a", num_lines_combo, "de", name)
    else:
        print("Il n'y a pas de {}".format(name))


combo_dupli = "Combo/Combo_Duplicate_Removed.txt"
divers = "Combo/Divers.txt"
