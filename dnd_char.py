#!/usr/bin/python

# imports
from dnd_world import World
import ran_gen
import random
import die

# functions
def stat_gen(): 
    "Roll 4d6, drop the lowest, return total sum"
    
    rolls = [die.rolld(6), die.rolld(6), die.rolld(6), die.rolld(6)]
    rolls.remove(min(rolls))
            
    return sum(rolls)

def get_alig(alig_list):
    """
        First   [0] is lawful, neutral, chaotic
        Second  [1] is good, neutral, evil
    """
    
    alignment = ""
    if alig_list[0] == 1: 
        alignment = alignment + "Lawful"
    elif alig_list[0] == 2: 
        alignment = alignment + "Neutral"
    else: 
        alignment = alignment + "Chaotic"
        
    if alig_list[1] == 1: 
        alignment = alignment + " Good"
    elif alig_list[1] == 2: 
        alignment = alignment + " Neutral"
    else: 
        alignment = alignment + " Evil"
        
    if alig_list[0] == 2 and alig_list[1] == 2:
        alignment = "True Neutral"

    return alignment


class Character:

    logical_dict = {
        "Dwarf":
            {
                "pot_aligns": [98],
                "pot_alig_nums": [[1, 1]],
                "class_nums": [48, 96],
                "pot_classes": ["Fighter", "Barbarian"]
            },
        "Elf":
            {
                "pot_aligns": [88],
                "pot_align_nums": [[3, 1]],
                "class_nums": [32, 48, 68, 80, 96],
                "pot_classes": ["Ranger", "Sorcerer", "Cleric", "Wizard", "Rogue"]
            },
        "Halfling":
            {
                "pot_aligns": [97],
                "pot_alig_nums": [[1, 1]],
                "class_nums": [25, 48, 82, 92],
                "pot_classes": ["Bard", "Rogue", "Cleric", "Monk"]
            },
        "Dragonborn":
            {
                "pot_aligns": [30, 60, 78, 96],
                "pot_alig_nums": [[1, 1], [3, 1], [1, 3], [3, 3]],
                "class_nums": [18, 32, 48, 58, 72, 88],
                "pot_classes": ["Wizard", "Fighter", "Sorcerer", "Warlock", "Paladin", "Rogue"]
            },
        "Gnome":
            {
                "pot_aligns": [86, 98],
                "pot_alig_nums": [[1, 1], [3, 1]],
                "class_nums": [18, 42, 48, 58, 76, 88],
                "pot_classes": ["Wizard", "Bard", "Sorcerer", "Warlock", "Paladin", "Rogue"]
            },
        "Half-Elf":
            {
                "pot_aligns": [35, 70, 96],
                "pot_alig_nums": [[1, 1], [2, 3], [3, 3]],
                "class_nums": [22, 32, 48, 58, 72, 88],
                "pot_classes": ["Wizard", "Fighter", "Sorcerer", "Warlock", "Paladin", "Rogue"]
            },
        "Half-Orc":
            {
                "pot_aligns": [95],
                "pot_alig_nums": [[3, 2]],
                "class_nums": [40, 80, 90, 100],
                "pot_classes": ["Barbarian", "Fighter", "Monk", "Paladin"]
            },
        "Tiefling":
            {
                "pot_aligns": [85],
                "pot_alig_nums": [[3, 3]],
                "class_nums": [22, 32, 48, 58, 72, 88],
                "pot_classes": ["Wizard", "Ranger", "Sorcerer", "Warlock", "Paladin", "Rogue"]
            }
    }

    smart_permutations = {
        "Barbarian":
            {
                50:
                    {
                        "str": 0,
                        "con": 1,
                        "dex": 2,
                        "cha": 3,
                        "int": 4,
                        "wis": 5
                    },
                0:                  #this is the else case since you are rolling numbers starting at 1 this will be every time true
                    {
                        "str": 0,
                        "con": 1,
                        "cha": 2,
                        "dex": 3,
                        "int": 4,
                        "wis": 5
                    }
            },
        "Bard":
            {
                0:
                    {
                        "cha": 0,
                        "dex": 1,
                        "wis": 2,
                        "con": 3,
                        "int": 4,
                        "str": 5
                    }
            },
        "Fighter":
            {
                47:
                    {
                        "str": 0,
                        "con": 1,
                        "dex": 2,
                        "wis": 3,
                        "cha": 4,
                        "int": 5
                    },
                94:
                    {
                        "dex": 0,
                        "con": 1,
                        "wis": 2,
                        "cha": 3,
                        "int": 4,
                        "str": 5
                    },
                0:
                    {
                        "int": 0,
                        "con": 1,
                        "dex": 2,
                        "wis": 3,
                        "str": 4,
                        "cha": 5
                    }
            },
        "Cleric":
            {
                50:
                    {
                        "wis": 0,
                        "str": 1,
                        "con": 2,
                        "dex": 3,
                        "cha": 4,
                        "int": 5
                    },
                0:
                    {
                        "wis": 0,
                        "con": 1,
                        "str": 2,
                        "dex": 3,
                        "cha": 4,
                        "int": 5
                    }
            },
            "Druid":
                {
                    0:
                        {
                            "wis": 0,
                            "con": 1,
                            "dex": 2,
                            "cha": 3,
                            "int": 4,
                            "str": 5
                        }
                },
            "Monk":
                {
                    0:
                        {
                            "dex": 0,
                            "wis": 1,
                            "con": 2,
                            "cha": 3,
                            "int": 4,
                            "str": 5
                        }
                },
            "Paladin":
                {
                    50:
                        {
                            "str": 0,
                            "cha": 1,
                            "wis": 2,
                            "dex": 3,
                            "con": 4,
                            "int": 5
                        },
                    0:
                        {
                            "str": 0,
                            "cha": 1,
                            "con": 2,
                            "dex": 3,
                            "wis": 4,
                            "int": 5
                        }
                },
            "Ranger":
                {
                    92:
                        {
                            "dex": 0,
                            "wis": 1,
                            "con": 2,
                            "str": 3,
                            "int": 4,
                            "cha": 5
                        },
                    0:
                        {
                            "str": 0,
                            "wis": 1,
                            "con": 2,
                            "dex": 3,
                            "int": 4,
                            "cha": 5
                        }
                },
            "Rogue":
                {
                    60:
                        {
                            "dex": 0,
                            "cha": 1,
                            "con": 2,
                            "wis": 3,
                            "int": 4,
                            "str": 5
                        },
                    0:
                        {
                            "dex": 0,
                            "int": 1,
                            "con": 2,
                            "wis": 3,
                            "cha": 4,
                            "str": 5
                        }
                },
            "Sorcerer":
                {
                    50:
                        {
                            "cha": 0,
                            "con": 1,
                            "dex": 2,
                            "wis": 3,
                            "int": 4,
                            "str": 5,
                        },
                    0:
                        {
                            "cha": 0,
                            "con": 1,
                            "wis": 2,
                            "dex": 3,
                            "int": 4,
                            "str": 5,
                        }
                },
            "Wizard":
            {
                50:
                    {
                        "int": 0,
                        "con": 1,
                        "dex": 2,
                        "wis": 3,
                        "str": 4,
                        "cha": 5,
                    },
                66:
                    {
                        "int": 0,
                        "dex": 1,
                        "con": 2,
                        "wis": 3,
                        "str": 4,
                        "cha": 5,
                    },
                0:
                    {
                        "int": 0,
                        "dex": 1,
                        "wis": 2,
                        "con": 3,
                        "str": 4,
                        "cha": 5,
                    }
            },
            "Warlock":
            {
                50:
                    {
                        "cha": 0,
                        "con": 1,
                        "dex": 2,
                        "wis": 3,
                        "int": 4,
                        "str": 5,
                    },
                0:
                    {
                        "cha": 0,
                        "con": 1,
                        "wis": 2,
                        "dex": 3,
                        "int": 4,
                        "str": 5,
                    }
            }
    }

    def __init__(self):
        #character traits
        self.p_race      = ran_gen.rrace()
        self.p_class     = ran_gen.rclass()
        self.p_alig_val  = [die.rolld(3), die.rolld(3)]
        self.p_alignment = get_alig(self.p_alig_val)

        #attributes
        self.p_age       = self.smart_age()
        self.p_fname     = ran_gen.rfname(self.p_race)
        self.p_lname     = ran_gen.rlname(self.p_race)
        self.p_name      = self.p_fname + " " + self.p_lname

        #financial
        self.p_net_worth = ran_gen.rwealth()
        self.p_wea_desc  = ran_gen.get_wealth_desc(self.p_net_worth)

        #stats
        self.str = stat_gen()
        self.dex = stat_gen()
        self.con = stat_gen()
        self.wis = stat_gen()
        self.int = stat_gen()
        self.cha = stat_gen()

    def logical_stereotype(self):
        """
            Helps normalize stereotypical alignment and class based
            on race according to the 5th edition PHB
        """

        pot_aligns = self.logical_dict[self.p_race]["pot_aligns"]           # potential alignment %s
        pot_alig_nums = self.logical_dict[self.p_race]["pot_alig_nums"]    # alig nums based off of pot_aligns
        class_nums = self.logical_dict[self.p_race]["class_nums"]           # class % per race
        pot_classes = self.logical_dict[self.p_race]["pot_classes"]         # potential classes

        ster_align = die.rolld(100)    # stereotypical alignment %
        ster_class = die.rolld(100)    # stereotypical class %

        for i in range(len(pot_aligns)):
            if ster_align <= pot_aligns[i]:
                self.p_alig_val[0] = pot_alig_nums[i][0]
                self.p_alig_val[1] = pot_alig_nums[i][1]

                for j in range(len(class_nums)):
                    if ster_class <= class_nums[j]:
                        self.p_class = pot_classes[j]
                        break
                break

        self.p_alignment = get_alig(self.p_alig_val)

    def smart_age(self):
        """
            Give character an appropriate age for given race
            Max age taken from 5th edition PHB, or D&D Beyond if not
            listed in PHB
        """

        r = die.rolld(100) # random percentage
        r_a_mod = random.randrange(86, 99) / 100 # age modifier

        # the following are ordered according to dnd_world
        maxa = [433, 845, 167, 98, 94, 522, 222, 80, 102]           # max ages
        aa = [17, 17, 17, 17, 15, 20, 17, 16, 17]                   # adulthood ages
        r_a_check = [.74, .88, .85, .85, .70, .82, .88, .79, .82]   # age check
        alter_chance = [89, 89, 89, 89, 85, 89, 89, 82, 89]         # age alter chance
        age = -1                                                    # initalize age

        for i in range(len(World.RACES.value)):
            if self.p_race == World.RACES.value[i]:
                age = die.rolld(maxa[i] - aa[i]) + aa[i]
                if age >= int(r_a_check[i] * maxa[i]) and r < alter_chance[i]:
                    age = int(age * r_a_mod)
                break

        return age

    def smart_wealth(self):
        'Make a somewhat logical attempt at calculating wealth'

        # these are arbitrary
        w_thresh = [100, 1150, 3700, 6800, 11000]
        w_brackets = [9.2, 50, 98.2, 99.6, 100]

        # ordered according to World
        w_mod = [1.08, 1.02, 1.01, 1.00, 1.02, 1.08, 1.02, .98, 1.03]

        p = round(random.uniform(0, 100), 2)
        rich_luck = random.uniform(0, 100)
        rl_mod = round(random.uniform(1.2, 2), 2)

        for i in range(len(w_brackets)):
            if p <= w_brackets[i]:
                if w_brackets[i] == w_brackets[0]:
                    self.p_net_worth = random.randint(1, w_thresh[i])
                    break
                else:
                    self.p_net_worth = random.randint(w_thresh[i-1], \
                        w_thresh[i])
                    if w_brackets[i] == w_brackets[-1] and rich_luck > 90:
                        self.p_net_worth = int(self.p_net_worth * rl_mod)
                    break

        for i in range(len(World.RACES.value)):
            if self.p_race == World.RACES.value[i]:
                self.p_net_worth = int(self.p_net_worth * w_mod[i])
                break

        # wealth descs not used for now
        self.p_wea_desc = ran_gen.get_wealth_desc(self.p_net_worth)

    def smart_stats(self):
        """
        Optimizes stats based on class based on 5th edition PHB
        """

        ph = [self.str, self.dex, self.con, self.wis, self.int, self.cha]
        ph.sort()
        ph.reverse()
        p = random.randint(1, 100)

        for decision_p, stats in self.smart_permutations[self.p_class].items():
            if p <= decision_p:
                for stat_name, stat_position in stats.items():
                    setattr(self, stat_name, ph[stat_position])
