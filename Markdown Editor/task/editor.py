help_menu = ["plain", "bold", "italic", "header", "link",
             "inline-code", "new-line", "ordered-list", "unordered-list"]
special = ["!help", "!done"]

formatted_text = ""
text_list = []


def plain():
    text = input("Text: ")
    return text


def bold():
    text = input("Text: ")
    return f"**{text}**"


def italic():
    text = input("Text: ")
    return f"*{text}*"


def header():
    level = int(input("Level: "))
    while level not in range(1, 6):
        print("The level should be within the range of 1 to 6")
        level = int(input("Level: "))
    text = input("Text: ")
    return level * "#" + f" {text}" + "\n"


def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def inline_code():
    text = input("Text: ")
    return f"`{text}`"


def new_line():
    return "\n"


def mark_list(order=True):
    row = 0
    text = list()
    rows = int(input("Number of rows: "))
    while rows <= 0:
        print("The number of rows should be greater than zero")
        rows = int(input("Number of rows: "))
    while row < rows:
        row += 1
        element = input(f"Row #{row}: ")
        if order:
            text.append(f"{row}. {element}\n")
        else:
            text.append(f"* {element}\n")
    return "".join(text)


while True:
    formatter = input("Choose a formatter: ")
    if formatter not in help_menu and formatter not in special:
        print("Unknown formatting type or command")
        continue
    if formatter == "!help":
        print(" ".join(help_menu))
        print("Special commands: ", " ".join(special))
        continue
    if formatter == "!done":
        print(formatted_text)
        with open("output.md", "w") as text_file:
            for line in text_list:
                text_file.write(line)
        text_file.close()
        break
    else:
        if formatter == "plain":
            formatted_text = plain()
        elif formatter == "bold":
            formatted_text = bold()
        elif formatter == "italic":
            formatted_text = italic()
        elif formatter == "header":
            formatted_text = header()
        elif formatter == "link":
            formatted_text = link()
        elif formatter == "inline-code":
            formatted_text = inline_code()
        elif formatter == "new-line":
            formatted_text = new_line()
        elif formatter == "ordered-list":
            formatted_text = mark_list()
        elif formatter == "unordered-list":
            formatted_text = mark_list(order=False)
        text_list.append(formatted_text)
        print("".join(text_list))
        continue
