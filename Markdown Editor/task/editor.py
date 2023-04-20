class Formatter:
    def __init__(self):
        self.user_input = ""
        self.content = []
        self.commands = ["!done", "!help"]
        self.formatters = {"plain": self.plain, "bold": self.bold, "italic": self.italic,
                           "header": self.header, "link": self.link, "inline-code": self.inline_code,
                           "ordered-list": self.ordered_list, "unordered-list": self.unordered_list,
                           "new-line": self.new_line}
    def plain(self):
        self.content.append(input("Text: "))

    def bold(self):
        last_item = self.content.pop()
        user_input = input("Text: ")
        self.content.append(last_item + "**" + user_input + "**")

    def italic(self):
        user_input = input("Text:")
        self.content.append(f"*{user_input}*")
    def header(self):
        while True:
            level = int(input("level: "))
            if level not in range(1, 6):
                print("The level should be within the range of 1 to 6")
            else:
                break
        user_input = input("Text: ")
        self.content.append(level * "#" + " " + user_input + "\n")
    def link(self):
        label = input("Label: ")
        user_input = input("URL: ")
        self.content.append(f"[{label}]({user_input})")
    def inline_code(self):
        user_input = input("Text:")
        last_item = self.content.pop()
        self.content.append(last_item + f"`{user_input}`")
    def ordered_list(self):
        while True:
            user_input = int(input("Number of rows: "))
            if user_input <= 0:
                print("The number of rows should be greater than zero")
            else:
                break
        temp = ""
        for i in range(1, user_input + 1):
            user_input = input(f"Row #{i}: ")
            temp += f"{i}. {user_input}\n"
        self.content.append(temp)
    def unordered_list(self):
        while True:
            user_input = int(input("Number of rows: "))
            if user_input <= 0:
                print("The number of rows should be greater than zero")
            else:
                break
        temp = ""
        for i in range(1, user_input + 1):
            user_input = input(f"Row #{i}: ")
            temp += f"* {user_input}\n"
        self.content.append(temp)
    def new_line(self):
        last_item = self.content.pop()
        self.content.append(last_item + "\n")
    def save_file(self):
        with open("output.md", "w", encoding="utf-8") as file:
            for i in self.content:
                file.write(f"{i}")
    def start(self):
        while True:
            user_input = input("Choose a formatter: ")
            if user_input == "!done":
                self.save_file()
                break
            elif user_input == "!help":
                print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
                print("Special commands: !help !done")
            elif user_input in self.formatters.keys():
                formatter_function = self.formatters[user_input]
                formatted_text = formatter_function()
                if formatted_text is not None:
                    self.content.append(formatted_text)
            for item in self.content:
                print(item)
def main():
    f = Formatter()
    f.start()

if __name__ == "__main__":
    main()

