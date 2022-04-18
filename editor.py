helper = """Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done"""
choices = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line",
           "ordered-list", "unordered-list", "!done", "!help"]
done = False

markdown = ""
def headings():
    global markdown
    if formatter == "header":
        level = int(input("Level: "))
        while level < 1 or level > 6:
            print("The level should be within the range of 1 to 6")
            level = int(input("Level: "))
        text = input("Text: ")
        text = "#" * level + " " + text + "\n"
        markdown += text
        print(markdown)

def PBII():
    global markdown
    if formatter == "bold":
        text = input("Text: ")
        text = "**" + text + "**"
        markdown += text
        print(markdown)
    if formatter == "italic":
        text = input("Text: ")
        text = "*" + text + "*"
        markdown += text
        print(markdown)
    if formatter == "plain":
        text = input("Text: ")
        text = text
        markdown += text
        print(markdown)
    if formatter == "inline-code":
        text = input("Text: ")
        text = "`" + text + "`"
        markdown += text
        print(markdown)

def linker():
    global markdown
    label = input("Label: ")
    hyperlink = input("URL: ")
    text = "[" + label + "]" + "(" + hyperlink + ")"
    markdown += text
    print(markdown)

def newline():
    global markdown
    newline = "\n"
    markdown += newline
    print(markdown)

def lister():
    global markdown
    rows = 0
    element = []
    while rows <= 0:
        rows = int(input("Number of rows: "))
        if rows <= 0:
            print("The number of rows should be greater than zero")
            continue
    for i in range(0,rows):
        element.append(input(f"Row #{i+1}: "))
    if formatter == "ordered-list":
        for id,i in enumerate(element):
            markdown += (f"{id+1}. {i}\n")
        print(markdown)
    if formatter == "unordered-list":
        for i in element:
            markdown += (f"* {i}\n")
        print(markdown)

while done == False:
    formatter = input("Choose a formatter: ")
    if formatter == "!help":
        print(helper)
    if formatter == "!done":
        file = open("output.md", "w")
        file.write(markdown)
        file.close()
        done = True
    if formatter not in choices:
        print("Unknown formatting type or command.")
        continue
    if formatter == "header":
        headings()
    if formatter == "plain" or formatter == "bold" or formatter == "italic" or formatter == "inline-code":
        PBII()
    if formatter == "link":
        linker()
    if formatter == "new-line":
        newline()
    if formatter == "ordered-list" or formatter == "unordered-list":
        lister()
