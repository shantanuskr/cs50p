food_items ={ 
            "apple"       : 130,
            "avocado"       : 50 ,
            "banana"        : 110,
            "cantaloupe"    : 50 ,
            "grapefruit"    : 60 ,
            "grapes"        : 90,
            "kiwifruit"     : 90 ,
            "lemon"         : 15 ,
            "lime"          : 20 ,
            "orange"        : 80 ,
            "peach"         : 60 ,
            "pear"          : 100,
            "pineapple"     : 50 ,
            "plums"         : 70,
            "strawberries"  : 50,
            "sweet cherries": 100,
            "tangerine"     : 50,
            "watearmelon"   : 80  }


item = input("Item: ").lower()


if item in food_items:
    print(f"Calories: {food_items[item]}")
