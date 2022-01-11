def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    inventory = {}

    for item in items:
        if item not in inventory:
            inventory[item] = 0

        inventory[item] += 1

    return inventory


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    for item in items:
        if item not in inventory:
            inventory[item] = 0

        inventory[item] += 1
    
    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for item in items:
        if inventory[item] > 0:
            inventory[item] -= 1
    
    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    if item in inventory:
        inventory.pop(item)
    
    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    tuples = []

    for key in inventory:
        if inventory[key] > 0:
            tuples.append(tuple([key, inventory[key]]))

    return tuples
