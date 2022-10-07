class Syntax(Exception):
    """
    Base class for syntax errors
    """
    base = f"Invalid Syntax: "
    pass


class nmp(Syntax):
    def __init__(self, lineNum: int, line: str):
        self.message = self.base + f"Mismatched Parentheses in line {lineNum}\n-- {line} --"
        super().__init__(self.message)


class syntax(Syntax):
    def __init__(self, lineNum: int, line: str):
        self.message = self.base + f"Syntax error in line {lineNum}\n-- {line} --"
        super().__init__(self.message)
