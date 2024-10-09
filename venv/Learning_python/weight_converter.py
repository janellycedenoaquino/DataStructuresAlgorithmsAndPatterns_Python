import math


def weightConverter():
    w = input("weight: ")
    unit = input(f"(K)g or (L)bs:").lower()
    if unit == "l":
        # convert to pounds
        weight_converted = math.floor(int(w) / 2.20462)
        unit = "k"
    else:
        # convert to kg
        weight_converted = math.floor(int(w) * 2.20462)

    print(f"weight in {unit}: {weight_converted}")


def makeStar(amount):
    amount_of_stars = "*"
    space_filler = ""
    final_value = ""
    for star in range(amount):
        for space in range(math.ceil(amount/2 - len(amount_of_stars)+1)):
              space_filler += " "
        final_value += space_filler + amount_of_stars + space_filler + "\n"
        amount_of_stars += "*"
        space_filler = ""
    return final_value


print(makeStar(7))