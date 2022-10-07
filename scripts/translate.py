# Python code to TI Token Translator
from scripts import process

class compiler:
    moduleName = "calc"
    replace = dict([
        ("nDeriv", "nDeriv"),
        ("fnInt", "fnInt"),
        ("iPart", "iPart"),
        ("fPart", "fPart"),
        ("minimum", "min"),
        ("maximum", "max"),
        ("lcm", "lcm"),
        ("gcd", "gcd"),
        ("conj", "conj"),
        ("real", "real"),
        ("imag", "imag"),
        ("rand", "rand"),
        ("npr", "nPr"),
        ("ncr", "nCr"),
        ("randint", "randInt"),
        ("randnorm", "randNorm"),
        ("randbin", "randBin"),
        ("asin", "sin^-1"),
        ("acos", "cos^-1"),
        ("atan", "tan^-1"),
        ("sin", "sin"),
        ("cos", "cos"),
        ("tan", "tan"),
        ("sqrt", "sqrt"),
        ("log", "log"),
        ("ln", "ln"),
        ("ep", "e^")
    ])
    # Relocate input to the left
    relocate = dict([
        ("toFrac", ">Frac"),
        ("toDec", ">Dec"),
        ("fact", "!"),
        ("dms", ">DMS")
    ])
    # No Parentheses
    nonparent = dict([
        ("print", "Disp"),
        ("input", "Input"),
        ("prompt", "Prompt")
    ])

    def replacer(code: list):
        moduleName = compiler.moduleName
        for lineNum in range(len(code)):
            for key in compiler.replace.keys():
                #print(code[lineNum])
                code[lineNum] = code[lineNum].replace(key, compiler.replace[key])
            code[lineNum] = code[lineNum].replace(f"{moduleName}.", "")
        return code

    def relocater(code: list):
        # for lineNum in range(len(code)):
        a = 0

    def read(filePath: str):
        with open(filePath, "r") as f:
            lineCache = f.readlines()
        lines = [cache for cache in lineCache]
        insertList = []
        xpList = []
        skipAdjust = 0
        initCondition = False
        for lineNum in range(len(lines)):
            adjust = 0
            line = lines[lineNum]
            if line == "" or line == "\n":
                skipAdjust += 1
            line = line.replace("\t", "    ").replace("\n", "").replace("'", '"')
            space = process.countStartSpace(line)
            if space == None:
                continue
            if "#" in line:
                skipAdjust += 1
                continue
            if "calc" in line and "import" in line and " as " in line:
                compiler.moduleName = line.split("as")[-1].replace(" ", "")
            elif "import" in line and "as" not in line and "calc" in line:
                compiler.moduleName = line.replace(" ", "").replace("import", "")
            if "import" in line:
                skipAdjust += 1
                continue
            if f"init(" in line:
                continue
            if "for" in line.replace(space * " ", "")[:4]:
                if process.countStartSpace(lines[lineNum + 1]) != 0:
                    insertList.append((process.countStartSpace(lines[lineNum]), "for", lineNum))
            if "elif" in line:
                line = line.replace("elif", "if")
                lines[lineNum] = line
            lists = "123456"
            for listchar in lists:
                if f"L{listchar}=[]" in line.replace(process.countStartSpace(line) * " ", "").replace(" ", ""):
                    line = f"ClrList L{listchar}"
            line = process.line.operators(line)
            line = process.line.For(line)
            line = process.line.int(line)
            line = process.line.equal(line)
            line = process.line.input(line)
            line = process.line.str(line)
            line = process.line.print(line)
            line = process.excessSpaceRemove(line)
            if "==" in line:
                line = line.replace("==", "=")
            replaceList = [("!=", "≠"), ("<=", "≤"), (">=", "≥")]
            for prev, after in replaceList:
                line = line.replace(prev, after)
            if "Input" in line.replace(process.countStartSpace(line)*" ", "")[:6] and "→" in line:
                line = line.replace("→", ",")
            if "if" in line.replace(process.countStartSpace(line)*" ", "")[:3] and ":" in line:
                line = line.replace(":", ":Then")
                line = line.replace("if", "If")
            if "else" in line.replace(process.countStartSpace(line)*" ", "")[:5]:
                line = line.replace("else", "Else")
            if "while" in line.replace(process.countStartSpace(line)*" ", "")[:5]:
                line = line.replace("while", "While")
            prepList = [("L1", "L₁"), ("L2", "L₂"), ("L3", "L₃"), ("L4", "L₄"), ("L5", "L₅"), ("L6", "L₆"), ("len(", "dim("), ("[", "("), ("]", "+1)")]
            for prep, prepafter in prepList:
                line = line.replace(prep, prepafter)
            if ".append(" in line:
                cache = line.replace(process.countStartSpace(line)*" ", "").replace(")", "")
                cache = cache.split(".append(")
                L = cache[0]
                var = cache[1]
                line = f"{var}→{L}(1+dim({L}))"
            if "break" in line.replace(process.countStartSpace(line)*" ", ""):
                line = line.replace("break", "Stop")
            if len(process.findall(line, "%")) != 0:
                parents = process.parentMatch(line)
                for start, end in parents:
                    selected = line[start+1:end]
                    if "%" in selected:
                        selected = selected.split("%")
                        var1 = selected[0].replace(" ", "")
                        var2 = selected[1].replace(" ", "")
                        selected = f" ({var1}-({var2}*iPart(({var1})/({var2}))))"
                    line = line.replace(line[start:end+1], selected)
            line = line.replace(process.countStartSpace(line)*" ", "")
            xpList.append(line)
        insertList += process.ifMatcher(lines)
        insertList = process.appendPrep(insertList, lines)
        adjust = 0
        for n in range(len(insertList)):
            xpList.insert(insertList[n][0] + adjust - skipAdjust, insertList[n][1])
            adjust += 1
        xpList = compiler.replacer(xpList)
        xpList = [xpList[lineNum] for lineNum in range(len(xpList)) if len(xpList[lineNum]) != 0]
        code = "\n".join(xpList)
        print(code)
