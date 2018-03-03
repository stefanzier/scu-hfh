menu_options = ["Prepare", "Oh, no. Need help now..."]


def generate_menu():
    index = 1
    menu = "Welcome to APP_NAME!\n"
    for option in menu_options:
        menu += "  {} - {}\n".format(index, option) + ""
        index += 1

    return menu
