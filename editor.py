# write your code here
# !help to check for the commands you can use
# !done to save the content to a file and exit the program


data_list = []


def only_plain():
    plain_text = input("Text: ")
    data_list.append(plain_text)
    for i in data_list:
        print(i)


def only_bold():
    bold_text = input("Text: ")
    data_list.append('**' + bold_text + '**')
    for i in data_list:
        print(i, end='')
    print('')


def only_italic():
    italic_text = input("Text: ")
    data_list.append('*' + italic_text + '*')
    for i in data_list:
        print(i, end='')
    print()


def only_header():
    s = ''
    heading_level = int(input("Level: "))
    if 1 <= heading_level <= 6:
        header_text = input("Text: ")
        for i in range(heading_level):
            s = s + '#'
        data_list.append(s + " " + header_text + '\n')
        for lst in data_list:
            print(lst, end='')
        print()
    else:
        print("The level should be within the range of 1 to 6")
        only_header()


def only_link():
    label = input("Label: ")
    url = input("URL: ")
    data_list.append(f"[{label}]({url})")
    for i in data_list:
        print(i)


def only_inline():
    inline_text = input("Text: ")
    data_list.append("`" + inline_text + "`")
    for i in data_list:
        print(i, end='')
    print()


def only_new_line():
    for i in data_list:
        print(i)
    print()
    data_list.append('\n')


def only_lists(formatter):
    if formatter == "ordered-list":
        rows = int(input("Number of rows: "))
        if rows > 0:
            for i in range(1, rows + 1):
                row_data = input(f"Row #{i}: ")
                data_list.append(f'{i}. ' + row_data + '\n')
            [print(data, end='') for data in data_list]
            print()
        else:
            print("The number of rows should be greater than zero")
            only_lists(formatter)
    if formatter == "unordered-list":
        rows = int(input("Number of rows: "))
        if rows > 0:
            for i in range(1, rows + 1):
                row_data = input(f"Row #{i}: ")
                data_list.append('* ' + row_data + '\n')
            [print(data, end='') for data in data_list]
            print()
        else:
            print("The number of rows should be greater than zero")
            only_lists(formatter)


# program starts from here
available_formatters = ["plain", "bold", "italic", "header",
                        "link", "inline-code", "new-line", "ordered-list", "unordered-list"]
special_commands = ["!help", "!done"]

while True:
    choose_a_formatter = input("Choose a formatter:")
    if choose_a_formatter == special_commands[0]:
        print(' '.join(available_formatters))
        print(' '.join(special_commands))
    elif choose_a_formatter in available_formatters:
        if choose_a_formatter == 'plain':
            only_plain()
        elif choose_a_formatter == 'bold':
            only_bold()
        elif choose_a_formatter == 'italic':
            only_italic()
        elif choose_a_formatter == 'header':
            only_header()
        elif choose_a_formatter == 'link':
            only_link()
        elif choose_a_formatter == 'inline-code':
            only_inline()
        elif choose_a_formatter == 'new-line':
            only_new_line()
        elif choose_a_formatter == 'ordered-list' or choose_a_formatter == 'unordered-list':
            only_lists(choose_a_formatter)
    elif choose_a_formatter == special_commands[1]:
        file = open('output.md', 'w')
        for get in data_list:
            file.write(get)
        file.close()
        exit()
    else:
        print("Unknown formatting type or command")
