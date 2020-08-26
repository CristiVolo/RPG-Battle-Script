import random   # The random library


class bcolors:  # Preset colour codes
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'   # Red
    ENDC = '\033[0m'    # This is concatenated after the text (the others come before the text)
    BOLD = '\033[1m'   # Bolded text
    UNDERLINE = '\033[4m'


class Person:   # The person class has the following attributes:
    # (Max)HP, (Max)MP, Attack(between 2 limits), Defense, (A list of spells)Magic, (A list of 2 strings)Actions
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):  # Returns a random number of damage points between the 2 limits
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):  # Returns a person's HP after they take damage
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, hp):
        self.hp += hp
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_maxhp(self):    # Max HP getter
        return self.maxhp

    def get_hp(self):   # HP getter
        return self.hp

    def get_maxmp(self):    # Max MP getter
        return self.maxmp

    def get_mp(self):   # MP getter
        return self.mp

    def reduce_mp(self, cost):  # Returns the remaining MP after casting a spell
        self.mp -= cost

    def get_spell_name(self, i):    # Returns the 'i''s spell NAME in the 'magic' list
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):    # Returns the 'i''s spell COST in the 'magic' list
        return self.magic[i]["cost"]

    def choose_action(self):    # Prints the available items in the 'action' list: Attack & Magic
        i = 1
        print("\n" + bcolors.OKBLUE + "ACTIONS\n" + bcolors.ENDC)
        for action in self.actions:
            print("    " + str(i) + ".", action)
            i += 1

    def choose_magic(self):  # Prints the available spells in the 'magic' list, along some details: Cost & Damage
        i = 1
        print("\n" + bcolors.OKBLUE + "MAGIC\n" + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ".", spell.name, "| Cost:", spell.cost, "mp", "| Damage:", spell.dmg)
            i += 1

    def choose_item(self):  # Analoge like the previous two, but for items
        i = 1
        print("\n" + bcolors.OKGREEN + "ITEMS\n" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name, ":", item["item"].description, "(x" + str(item["quantity"])
                  + ")")
            i += 1

    def get_stats(self):
        # HP
        hp_bar = ""
        hp_bar_ticks = self.hp / self.maxhp * 25
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decrease = 9 - len(hp_string)
            while decrease > 0:
                current_hp += " "
                decrease -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        # MP
        mp_bar = ""
        mp_bar_ticks = self.mp / self.maxmp * 10
        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1
        while len(hp_bar) < 10:
            mp_bar += " "

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decrease = 7 - len(mp_string)
            while decrease > 0:
                current_mp += " "
                decrease -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print(
            bcolors.BOLD + str(self.name) + ":       " + current_hp + "    " + bcolors.ENDC +
            bcolors.OKGREEN + hp_bar + bcolors.ENDC +
            bcolors.BOLD + "       " + current_mp + "   " + bcolors.OKBLUE + mp_bar +
            bcolors.ENDC)

    def get_enemy_stats(self):
        print("\n")
        hp_bar = ""
        hp_bar_ticks = self.hp / self.maxhp * 50
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 11:
            decrease = 11 - len(hp_string)
            while decrease > 0:
                current_hp += " "
                decrease -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        print(
            bcolors.BOLD + str(self.name) + ":    " + current_hp + "    " + bcolors.ENDC +
            bcolors.FAIL + hp_bar + bcolors.ENDC)

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "TARGET: " + bcolors.ENDC)

        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("\n" + bcolors.BOLD + str(i) + ".", enemy.name)
                i += 1

        choice = int(input("Choose a target: ")) - 1
        return choice
