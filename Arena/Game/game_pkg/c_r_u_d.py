'''CRUD
    --used by model to interact with data *list of dictionaries in this case
'''

from game_pkg import exceptions as mvc_exc

'''backend list'''

# global Martial Arts opponents list, for creating, updating, etc...
opponent_list = list()




# create char list


def create_chars(game_chars):
    global opponent_list
    opponent_list = game_chars

# create individual char


def create_char(name, ac, damage, hp, to_hit):
    global opponent_list
    results = list(filter(lambda x: x["name"] == name, opponent_list))
    if results:
        raise mvc_exc.CharAlreadyStored(f"{name} already stored!")
    else:
        opponent_list.append({"name": name,
                                "ac": ac,
                                "damage": damage, 
                                "hp": hp, 
                                "to_hit": to_hit})

# retrive and get char


def read_char(name):
    global opponent_list
    opponents = list(filter(lambda x: x['name'] == name, opponent_list))
    if opponents:
        return opponents[0]
    else:
        raise mvc_exc.CharNotStored(
            f"Can't read {name} because it's not stored"
        )

# read char list


def read_chars():
    global opponent_list
    return [list_item for list_item in opponent_list]

# update individual char


def update_char(name, ac, damage, hp, to_hit):
    global opponent_list
    # Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (index_x is a tuple, index_oppponent is a list of tuples)
    index_oppponent = list(
        filter(lambda index_x: index_x[1]["name"]
               == name, enumerate(opponent_list))
    )
    if index_oppponent:
        i, item_to_update = index_oppponent[0][0], index_oppponent[0][1]
        opponent_list[i] = {"name": name,
                            "ac": ac,
                            "damage": damage, 
                            "hp": hp, 
                            "to_hit": to_hit}
    else:
        raise mvc_exc.CharNotStored(
            f"Can't update {name} because it's not stored"
        )

# delete char


def delete_char(name):
    global opponent_list
    # From architect: Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    index_oppponent = list(
        filter(lambda index_x: index_x[1]["name"] == name, enumerate(opponent_list)))
    if index_oppponent:
        i, char_to_delete = index_oppponent[0][0], index_oppponent[0][1]
        del opponent_list[i]
    else:
        raise mvc_exc.CharNotStored(
            f"Can't delete {name} because it's not stored."
        )


'''
Local testing if necessary
'''
# def main():

#     # Main Data List of Dictionaries
#     opponent_list: list = [{"name": "Brute", "ac": 3, "damage": 75, "hp": 200, "to_hit": 15},
#                        {"name": "Inside", "ac": 8, "damage": 45, "hp": 100, "to_hit": 65},
#                        {"name": "Dodge", "ac": 15, "damage": 35, "hp": 75, "to_hit": 75},
#                        {"name": "Right_Hook", "ac": 7, "damage": 50, "hp": 100, "to_hit": 35},
#                        {"name": "Feet", "ac": 5, "damage": 60, "hp": 120, "to_hit": 25}]






# if __name__ == '__main__':
#     main()


