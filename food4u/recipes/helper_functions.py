import inflect


def get_base_ingredient(ingredient):
    p = inflect.engine()

    list_of_words = ingredient.split()
    relevant_word = list_of_words[-1]

    if p.singular_noun(relevant_word):
        list_of_words[-1] = p.singular_noun(relevant_word)

    return " ".join(list_of_words)



def get_ingredient_string(quantity, measurement, ingredient):

    if measurement:
        ingredient_string = quantity + " " + measurement + " " + ingredient + ";"
    else:

        if quantity:
            ingredient_string = quantity + " " + ingredient + ";"
        else:
            ingredient_string = ingredient + ";"

    return ingredient_string

