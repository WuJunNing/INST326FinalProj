import re
def store():
    with open("storestock.txt", "r", encoding = "utf-8") as f:
        inventory = {}
        for line in f:
            expr = (r"""(?mx)
                ^
                (?:(?P<item>[a-z]+)*\s)
                (?P<price>\d*)""")
            match = re.search(expr,line)
            if match:
                itemname = match.group("item")
                itemprice = match.group("price")
                inventory[itemname] = itemprice
    return inventory
print(store())