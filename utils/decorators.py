from colorama import Fore, Style

class IconicDecorator:
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ # ]" + Style.RESET_ALL
        self.CMDL = Style.BRIGHT + Fore.BLUE + "[ → ]" + Style.RESET_ALL
        self.STDS = "     "

class MessageDecorator:
    def __init__(self):
        ICON = IconicDecorator()
        self.PASS = ICON.PASS
        self.FAIL = ICON.FAIL
        self.WARN = ICON.WARN
        self.HEAD = ICON.HEAD
        self.CMDL = ICON.CMDL
        self.STDS = ICON.STDS

    def SuccessMessage(self, RequestMessage):
        print(self.PASS + " " + Style.RESET_ALL + RequestMessage)

    def FailureMessage(self, RequestMessage):
        print(self.FAIL + " " + Style.RESET_ALL + RequestMessage)

    def WarningMessage(self, RequestMessage):
        print(self.WARN + " " + Style.RESET_ALL + RequestMessage)

    def SectionMessage(self, RequestMessage):
        print(self.HEAD + " " + Fore.CYAN + Style.BRIGHT
              + RequestMessage + Style.RESET_ALL)

    def CommandMessage(self, RequestMessage):
        return self.CMDL + " " + Style.RESET_ALL + RequestMessage

    def GeneralMessage(self, RequestMessage):
        print(self.STDS + " " + Style.RESET_ALL + RequestMessage)

