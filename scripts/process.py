import re


def reversestr(string: str):
    return "".join([a for a in [string[n] for n in range(len(string))].__reversed__()])


def countStartSpace(line):
    for char in range(len(line)):
        if line[char] != " ":
            return char


def findall(line: str, search: str):
    try:
        return [n.span() for n in re.finditer(search, line)]
    except:
        for charIndex in range(len(search)):
            char = search[charIndex]
            try:
                re.finditer(char, line)
            except:
                search = search[:charIndex] + f"\{char}" + search[charIndex + 1:]
        return [n.span() for n in re.finditer(search, line)]


def parentMatch(line: str):
    """
    ( = left Parenthesis
    ) = right Parenthesis
    returns list with tuples
    """
    # Check
    cache = line
    for entry in re.findall("'([^']*)'", line):
        cache = cache.replace(entry, "")
    if len(re.findall("\(", cache)) != len(re.findall("\)", cache)):
        return None
    lParent = []
    sCond = False
    lpCount = 0
    Parent = []
    for index in range(len(line)):
        if line[index] == "'":
            sCond = not sCond
        if sCond == True:
            continue
        elif sCond == False:
            if line[index] == "(":
                lpCount += 1
                lParent.append(index)
            if line[index] == ")":
                lpCount -= 1
                Parent.append((lParent[-1], index))
                lParent.pop(-1)
    return sorted(Parent, key=lambda x: x[0])


def ifMatcher(lines: list):
    # (space:int, classify:str, spaceLine:int)
    lines = [(line.replace("elif", "if") if "elif" in line else (line)) for line in lines]
    ifProcess = [cache for cache in [((countStartSpace(lines[lineNum]), "if", lineNum) if "if" in lines[lineNum].replace(countStartSpace(lines[lineNum]) * " ", "")[:3] else ((countStartSpace(lines[lineNum]), "else", lineNum) if "else" in lines[lineNum].replace(countStartSpace(lines[lineNum]) * " ", "")[:5] else None)) for lineNum in range(len(lines))] if cache != None]
    adjust = 0
    for currentindex in range(len(ifProcess) - 1, -1, -1):
        space, classify, line = ifProcess[currentindex - adjust]
        if classify == "else":
            # Finds the matching pair for else
            for indexCache in range(currentindex - 1, -1, -1):
                if space == ifProcess[indexCache][0] and ifProcess[indexCache][1] == "if":
                    ifProcess.pop(indexCache)
                    adjust += 1
                    break
    return ifProcess

def eocFinder(info: tuple, lines: list):
    """
    End of Chunk Finder
    info: (space: int, classify: str, line: int)
    """
    space, classify, lineNum = info
    for lineIndex in range(lineNum + 1, len(lines)):
        line = lines[lineIndex]
        lineSpace = countStartSpace(line)
        if lineSpace <= space:
            return lineIndex
        elif lineIndex + 1 == len(lines):
            return len(lines)

def appendPrep(insertList: list, lines: list):
    """
    insertList: [(space: int, classify: str, line: int)...]
    """
    reference = {
        "if": "End",
        "else": "End",
        "for": "End"
    }
    keys = [key for key in reference.keys()]
    prepList = [index for index in [(eocFinder(insert, lines), reference[insert[1]] if insert[1] in keys else None) for insert in insertList] if index != None]
    return sorted(prepList, key=lambda tup: tup[0])

def excessSpaceRemove(line):
    options = ["+", "-", "(", ")", "[", "]", "<=", ">=", "<", ">", "="]
    for n in options:
        line = line.replace(f" {n}", n)
        line = line.replace(f" {n} ", n)
        line = line.replace(f"{n} ", n)
    return line

class line:
    def str(line):
        if "str(" in line:
            indexCount = len(findall(line, "str("))
            for n in range(indexCount):
                indexes = findall(line, "str(")
                parents = parentMatch(line)
                index, cache = indexes[0]
                index += 3
                for entry in range(len(parents)):
                    a, b = parents[entry]
                    if a == index or b == index:
                        indexStart, indexEnd = a, b
                        break
                line = line[0:indexStart - 3] + line[indexStart + 1:indexEnd] + line[indexEnd + 1:]
        return line

    def int(line):
        if "int(" in line and (line.find("print(") + 2 != line.find("int(")):
            indexCount = len(findall(line, "int("))
            for n in range(indexCount):
                indexes = findall(line, "int(")
                parents = parentMatch(line)
                index, cache = indexes[0]
                index += 3
                for entry in range(len(parents)):
                    a, b = parents[entry]
                    if a == index or b == index:
                        indexStart, indexEnd = a, b
                        break
                line = line[0:indexStart - 3] + line[indexStart + 1:indexEnd] + line[indexEnd + 1:]
        return line

    def print(line):
        if "print(" in line:
            index = line.find("print(") + 5
            parents = parentMatch(line)
            indexStart = None
            indexEnd = None
            for entry in range(len(parents)):
                a, b = parents[entry]
                if a == index or b == index:
                    indexStart, indexEnd = a, b
                    break
            line = line[0:indexStart] + line[indexStart + 1:indexEnd] + line[indexEnd + 1:]
            index = line.find("print")
            line = line[:index] + "Disp " + line[index + 5:]
            addIndex = findall(line, "+")
            if len(addIndex) != 0:
                indexStart, cache = addIndex[0]
                tempLine = [line[:indexStart], line[indexStart + 1:]]
                cache = tempLine[1].replace("(", "")
                if tempLine[0][-1] == " ":
                    tempLine[0] = tempLine[0][:-1]
                if cache[0] == " ":
                    cache = cache[1:]
                line = f"{tempLine[0]},{cache}"
            addIndex = findall(line, ",")
            if len(addIndex) != 0:
                indexStart, cache = addIndex[0]
                tempLine = [line[:indexStart], line[indexStart + 1:]]
                cache = tempLine[1].replace("(", "")
                if tempLine[0][-1] == " ":
                    tempLine[0] = tempLine[0][:-1]
                if cache[0] == " ":
                    cache = cache[1:]
                line = f"{tempLine[0]},{cache}"
        return line

    def input(line):
        if "input(" in line:
            if "=" in line:
                cache = line.split("=")
                var = cache[0].replace(" ", "")
                if cache[1][0] == " ":
                    cache[1] = cache[1][1:]
                line = f'{cache[1]},{var}'.replace("input(", "Input(")
            else:
                line = line.replace("input(", "Input(")
            parents = parentMatch(line)
            #   print(parents)
            indexStart = None
            indexEnd = None
            index = line.find("(")
            for entry in range(len(parents)):
                a, b = parents[entry]
                if a == index or b == index:
                    indexStart, indexEnd = a, b
                    break
            line = line[0:indexStart] + " " + line[indexStart + 1:indexEnd] + line[indexEnd + 1:]
        return line

    def equal(line):
        if "=" in line and "==" not in line and "if" not in line:
            cache = line.split("=")
            var = cache[0].replace(" ", "")
            if cache[1][0] == " ":
                cache[1] = cache[1][1:]
            line = f'{cache[1]}→{var}'
        return line

    def For(line):
        if "for" in line.replace(countStartSpace(line) * " ", "")[:4]:
            if "len(" not in line:
                cache = line.split("in")
                cacheVar = cache[0].split("for")
                var = cacheVar[1].replace(" ", "").replace("\t", "")
                cache[1] = cache[1].replace(" ", "").replace("range(", "").replace(")", "").replace(":", "")
                if "," in cache[1]:
                    bounds = cache[1].split(",")
                    lb = f"{bounds[0]}"
                    ub = bounds[1]
                else:
                    lb = 0
                    ub = cache[1]
                line = f"For({var},{lb},{ub}-1)"
            if "len(" in line:
                line = line.replace("len(", "dim(")
                lPFor = findall(line, "range(")[0][1]-1
                parentheses = parentMatch(line)
                for lp, rp in parentheses:
                    if lp == lPFor:
                        line = line[:lPFor] + line[lPFor+1:rp-1] + line[rp:]
                        print(line[:lPFor], lPFor)
                        break
                cache = line.split("range")
                cache[1] = cache[1].replace(" ", "").replace("\t", "")
                var = cache[0].replace("for", "").replace("in", "").replace(" ", "").replace("\t", "")
                if "," in cache[1]:
                    bounds = cache[1].split(",")
                    lb = f"{bounds[0]}"
                    ub = bounds[1]
                else:
                    lb = 1
                    ub = cache[1]
                line = f"For({var},{lb},{ub})"
        return line


    def operators(line):
        if "+=" in line:
            cache = line.replace(countStartSpace(line) * " ", "").split("+=")
            var = cache[0]
            cache.pop(0)
            cache = "".join(cache)
            line = f"{var}={var}+{cache}"
        if "-=" in line:
            cache = line.replace(countStartSpace(line) * " ", "").split("-=")
            var = cache[0]
            cache.pop(0)
            cache = "".join(cache)
            line = f"{var}={var}-{cache}"
        if "*=" in line:
            cache = line.replace(countStartSpace(line) * " ", "").split("*=")
            var = cache[0]
            cache.pop(0)
            cache = "".join(cache)
            line = f"{var}={var}*{cache}"
        if "/=" in line:
            cache = line.replace(countStartSpace(line) * " ", "").split("/=")
            var = cache[0]
            cache.pop(0)
            cache = "".join(cache)
            line = f"{var}={var}/{cache}"
        return line