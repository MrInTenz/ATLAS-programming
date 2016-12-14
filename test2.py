# split word into letters
# create dashes
# ask input
# if yes, enter and rewrite dashes
# if no, print NO

word = "kofie"

letters = list(word)


def create_space(word):
    return list(range(1, len(word)+1))


def ask():
    return input()


def starting_message():
    print("Welcome to your doom!")


def ending_message():
    pass


def has_won(list):
    for item in list:
        if item.isalpha():
            return True


def has_lost():
    pass


def draw_space(list, n):
    print(list[0:n])

draw_space(create_space(word), len(word))


def set_space_value(space, index, value):
    space[index] = value


def enter_letter(space, text, list, n):
    guess = input("Choose a letter!")
    if guess in text:
        num = text.index(guess)
        set_space_value(space, num, guess)
        draw_space(list,n)
    else:
        print("NO!")


def game(space, text, list, n):
    while not has_won() and not has_lost():
        draw_space(create_space(word), len(word))
        enter_letter(space, text, list, n)
    if has_won():
        print("hurray")
    if has_lost():
        print("haha sucker")
