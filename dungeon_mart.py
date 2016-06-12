dungeon_mart = ['drake heart', 'wyvern tooth', 'lizard tail']

stock = {
    "drake heart": 6,
    "wyvern tooth": 0,
    "lizard tail": 32,
    "komodo snout": 15
}
    
prices = {
    "drake heart": 4,
    "wyvern tooth": 2,
    "lizard tail": 1.5,
    "komodo snout": 3
}

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total + prices[item]
            stock[item] -= 1
    return total