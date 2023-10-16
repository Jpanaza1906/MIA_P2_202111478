Consola = []

def printConsole(text): 
    global Consola
    print("\033[36m{}\033[00m" .format(text))
    Consola.append(text)

def printError(error): 
    global Consola
    print("\033[91m{}\033[00m" .format(error))
    Consola.append(error)

def printSuccess(success): 
    global Consola
    print("\033[1;32m{}\033[00m" .format(success))
    Consola.append(success)

def printWarning(warning): 
    global Consola
    print("\033[93m{}\033[00m" .format(warning))
    Consola.append(warning)

def printTitle(title):
    global Consola 
    print("\033[1;33m{}\033[00m" .format(title))
    Consola.append(title)

def printSubtitle(subtitle): 
    global Consola
    print("\033[1;34m{}\033[00m" .format(subtitle))
    Consola.append(subtitle)

def printComment(comment): 
    global Consola
    print("\033[1;35m{}\033[00m" .format(comment))
    Consola.append(comment)

def printInfo(info): 
    global Consola
    print("\033[1;36m{}\033[00m" .format(info))
    Consola.append(info)

def printHelp(help): 
    global Consola
    print("\033[1;37m{}\033[00m" .format(help))
    Consola.append(help)

def printText(text): 
    global Consola
    print("\033[1;38m{}\033[00m" .format(text))
    Consola.append(text)

#inputs con color
def inputConsole(text): return input("\033[1;34m{}\033[00m" .format(text))

def inputWarning(text): return input("\033[93m{}\033[00m" .format(text))
