import os
from Model.modul import exist


class Domaine:

    def __init__(self, search, name, combo_list):
        self.search = search
        self.name = name
        self.combo_list = combo_list
        print("Le nouveau domaine est", name, ", pour une recherche de", search, "a été ajouté pour chercher la combo")
        all_search.append(search)

    def get_search(self):
        return self.search

    def get_name(self):
        return self.name

    def get_combo(self):
        return self.combo_list

    def set_search(self, search):
        self.search = search

    def set_name(self, name):
        self.name = name

    def set_combo(self, combo_list):
        self.combo_list = combo_list

    @staticmethod
    def create_txt(search, name, combo_list):
        directory = "Combo/{}.txt".format(name)
        if os.path.exists(directory):
            os.remove(directory)
        for combo in combo_list:
            if search in combo:
                with open(directory, "a+") as file:
                    file.write(combo)
                    file.close()
        exist(directory)

    @staticmethod
    def create_txt_not(search, name, combo_list):
        directory = "Combo/{}.txt".format(name)
        if os.path.exists(directory):
            os.remove(directory)
        for combo in combo_list:
            if search not in combo:
                with open(directory, "a+") as file:
                    file.write(combo)
                    file.close()
        exist(directory)

    @staticmethod
    def create_txt_mdp(search, name, combo_list):
        directory = "Mdp/{}.txt".format(name)
        if os.path.exists(directory):
            os.remove(directory)
        list_combo = []
        for combo in combo_list:
            len_pass_start = int(combo.find(":") + 1)
            for characters in search:
                pass_indicator = combo.find(characters, len_pass_start)
                if pass_indicator > 1:
                    if list_combo.count(combo) < 1:
                        list_combo.append(combo)
        for combo in list_combo:
            with open(directory, "a+") as file:
                file.write(combo)
                file.close()
        exist(directory)

    @staticmethod
    def create_txt_mdp_search(search, name, combo_list):
        directory = "Mdp/{}.txt".format(name)
        if os.path.exists(directory):
            os.remove(directory)
        for combo in combo_list:
            len_pass_start = int(combo.find(":") + 1)
            pass_indicator = combo.find(search, len_pass_start)
            if pass_indicator > 1:
                with open(directory, "a+") as file:
                    file.write(combo)
                    file.close()
        exist(directory)


all_search = []
