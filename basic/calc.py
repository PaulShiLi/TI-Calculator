import decimal
import os
import math
import random
from scipy.stats import binom
from fractions import Fraction
import sympy as sym
import sys

# Decimal place limiter
displayDecLim = 10

# Set max recursion
maxRecursionLimit = 3000
sys.setrecursionlimit(maxRecursionLimit)


# Initialize Vars
def init(var: str):
    """
    Use this function to initialize a value
    var: String of the variable that will be included in future equations
    """
    return sym.var(var)


def clear():
    os.system("clear")


class Math:
    def toFrac(a: float):
        """
        Converts decimal to fraction.
        Float -> Str
        """
        if type(a) == float:
            return str(Fraction(a).limit_denominator())
        elif type(a) == int or type(a) == str:
            return a

    def toDec(a: str):
        """
        Converts fraction to decimal.
        Str -> Float
        """
        if type(a) == str and "/" in a:
            return eval(a)
        elif type(a) == int or type(a) == float:
            return a

    def nDeriv(exp, var, val):
        """
        exp: String or actual code of equation to take the derivative
        var: Variable to evaluate
        val: Can be a float or integer to evaluate the derivative of the expression
        """
        var = str(var)
        exp = sym.sympify(str(exp))
        var = sym.symbols(var)
        return sym.diff(exp).subs(var, val).evalf(displayDecLim)

    def fnInt(exp, var: str, lb, ub):
        """
        Finds the Definite Integral of a given function and boundaries
        exp: String or actual code of equation to take the derivative
        var: String of variable to evaluate
        lb: Can be a float or int as the lower bound of the integral
        ub: Can be a float or int as the upper bound of the integral
        """
        var = str(var)
        exp = sym.sympify(str(exp))
        var = sym.symbols(var)
        return sym.integrate(exp, (var, lb, ub)).evalf(displayDecLim)

    def fMin(exp, var: str, lb, ub):
        """
        Finds the minimum value of a given interval and function
        exp: String or actual code of equation to find the minimum value
        var: String of variable to evaluate
        lb: Can be a float or int as the lower bound of the minimum value
        ub: Can be a float or int as the upper bound of the minimum value
        """
        var = str(var)
        exp = sym.sympify(str(exp))
        var = sym.symbols(var)
        zeros = sym.solveset(exp, var, domain=sym.Interval(lb, ub))
        assert zeros.is_FiniteSet
        ans = sym.Min(exp.subs(var, lb), exp.subs(var, ub), *[exp.subs(var, i) for i in zeros])
        return ans.evalf(displayDecLim)

    def fMax(exp, var: str, lb, ub):
        """
        Finds the maximum value of a given interval and function
        exp: String or actual code of equation to find the maximum value
        var: String of variable to evaluate
        lb: Can be a float or int as the lower bound of the maximum value
        ub: Can be a float or int as the upper bound of the maximum value
        """
        var = str(var)
        exp = sym.sympify(str(exp))
        var = sym.symbols(var)
        zeros = sym.solveset(exp, var, domain=sym.Interval(lb, ub))
        assert zeros.is_FiniteSet
        ans = sym.Max(exp.subs(var, lb), exp.subs(var, ub), *[exp.subs(var, i) for i in zeros])
        return ans.evalf(displayDecLim)


class Num:
    def iPart(a):
        """
        Finds the integer part of a float
        a: float/int
        """
        if "-" in str(a):
            return math.ceil(a)
        else:
            return math.floor(a)

    def fPart(a):
        """
        Finds the decimal part of a float
        a: float/int
        """
        if "." in str(a):
            return float(f".{str(a).split('.')[-1]}")
        else:
            return 0

    def minimum(a, b=None):
        """
        Finds the minimum of either a list or float/int
        a: Can be a list/float/int
        b: (optional) Can be a list/float/int
        """
        if type(a) == list and b == None:
            return min(a)
        if type(a) == list and type(b) == list:
            return [min(a), min(b)]
        if (type(a) == float or type(a) == int) and (type(b) == float or type(b) == int):
            return min(a, b)
        if (type(a) == float or type(a) == int) and type(b) == list:
            return [(a if b[n] > a else (b[n])) for n in range(len(b))]
        if (type(b) == float or type(b) == int) and type(a) == list:
            return [(b if a[n] > b else (a[n])) for n in range(len(a))]

    def maximum(a, b=None):
        """
        Finds the maximum of either a list or float/int
        a: Can be a list/float/int
        b: (optional) Can be a list/float/int
        """
        if type(a) == list and b == None:
            return max(a)
        if type(a) == list and type(b) == list:
            return [max(a), max(b)]
        if (type(a) == float or type(a) == int) and (type(b) == float or type(b) == int):
            return max(a, b)
        if (type(a) == float or type(a) == int) and type(b) == list:
            return [(a if b[n] < a else (b[n])) for n in range(len(b))]
        if (type(b) == float or type(b) == int) and type(a) == list:
            return [(b if a[n] < b else (a[n])) for n in range(len(a))]

    def lcm(a: int, b: int):
        """
        Finds the least common multiple of two separate integers
        a: Int
        b: Int
        """
        return math.lcm(a, b)

    def gcd(a: int, b: int):
        """
        Finds the greatest common divisor of two separate integers
        a: int
        b: int
        """
        return math.gcd(a, b)


class Cpx:
    def conj(a):
        """
        Finds the conjugate of an complex function in the form of ai+b
        a: int/str
        """
        if type(a) == int or type(a) == float:
            return a
        if type(a) == str and "i" in a:
            a = a.replace(" ", "")
            if a[0] == "-" and "-" in a[1:len(a)]:
                temp = a[1:len(a)].split("-")
                if "i" in temp[0]:
                    return f"{temp[0]}-{temp[1]}"
                if "i" in temp[1]:
                    return f"-{temp[0]}+{temp[1]}"
            if a[0] == "-" and "+" in a[1:len(a)]:
                temp = a[1:len(a)].split("+")
                if "i" in temp[0]:
                    return f"{temp[0]}+{temp[1]}"
                if "i" in temp[1]:
                    return f"-{temp[0]}-{temp[1]}"
            else:
                if "-" in a:
                    temp = a.split("-")
                    if "i" in temp[0]:
                        return f"-{temp[0]}+{temp[1]}"
                    else:
                        return f"{temp[0]}+{temp[1]}"
                if "+" in a:
                    temp = a.split("+")
                    if "i" in temp[0]:
                        return f"-{temp[0]}+{temp[1]}"
                    else:
                        return f"{temp[0]}-{temp[1]}"

    def real(a):
        """
        Finds the real number in the complex function
        a: int/str
        """
        if type(a) == int or type(a) == float:
            return a
        if type(a) == str and "i" in a:
            a = a.replace(" ", "")
            if a[0] == "-" and "-" in a[1:len(a)]:
                temp = a[1:len(a)].split("-")
                if "i" in temp[0]:
                    return f"-{temp[1]}"
                if "i" in temp[1]:
                    return f"-{temp[0]}"
            if a[0] == "-" and "+" in a[1:len(a)]:
                temp = a[1:len(a)].split("+")
                if "i" in temp[0]:
                    return f"{temp[1]}"
                if "i" in temp[1]:
                    return f"-{temp[0]}"
            else:
                if "-" in a:
                    temp = a.split("-")
                    if "i" in temp[0]:
                        return f"{temp[1]}"
                    else:
                        return f"{temp[0]}"
                if "+" in a:
                    temp = a.split("+")
                    if "i" in temp[0]:
                        return f"{temp[1]}"
                    else:
                        return f"{temp[0]}"

    def imag(a):
        """
        Finds the coefficient of the imaginary number in the complex function
        a: int/str
        """
        if type(a) == int or type(a) == float:
            return 0
        if type(a) == str and "i" in a:
            a = a.replace(" ", "")
            if a[0] == "-" and "-" in a[1:len(a)]:
                temp = a[1:len(a)].split("-")
                if "i" in temp[0]:
                    if len(temp[0]) == 1:
                        return "-1"
                    return f"-{temp[0].replace('i', '')}"
                if "i" in temp[1]:
                    if len(temp[1]) == 1:
                        return "-1"
                    return f"-{temp[1].replace('i', '')}"
            if a[0] == "-" and "+" in a[1:len(a)]:
                temp = a[1:len(a)].split("+")
                if "i" in temp[0]:
                    if len(temp[0]) == 1:
                        return "-1"
                    return f"-{temp[0].replace('i', '')}"
                if "i" in temp[1]:
                    if len(temp[1]) == 1:
                        return "1"
                    return f"{temp[1].replace('i', '')}"
            else:
                if "-" in a:
                    temp = a.split("-")
                    if "i" in temp[0]:
                        if len(temp[0]) == 1:
                            return "1"
                        return f"{temp[0].replace('i', '')}"
                    else:
                        if len(temp[1]) == 1:
                            return "-1"
                        return f"-{temp[1].replace('i', '')}"
                if "+" in a:
                    temp = a.split("+")
                    if "i" in temp[0]:
                        if len(temp[0]) == 1:
                            return "1"
                        return f"{temp[0].replace('i', '')}"
                    else:
                        if len(temp[1]) == 1:
                            return "1"
                        return f"{temp[1].replace('i', '')}"


class Prb:
    def rand(n: int = None):
        """
        Gives a random decimal between the interval 0.1000000000 and 0.9999999999
        n: (optional) trials
        """
        if n == None:
            number = random.randint(1000000000, 9999999999)
            return float(f"0.{number}")
        if type(n) == int and 1000 > n > 0:
            return [float(f"0.{random.randint(1000000000, 9999999999)}") for a in range(n)]

    def npr(n: int, r: int):
        """
        Math nPr (permutation) formula
        n: int
        r: int
        """
        return math.factorial(n) // math.factorial(n - r)

    def ncr(n: int, r: int):
        """
        Math nCr (combination) formula
        n: int
        r: int
        """
        return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

    def fact(a: int):
        """
        Math factorial (!)
        a: int
        """
        return math.factorial(a)

    def randint(a, b, n: int = None):
        """
        Generates a random integer specified the bounds
        a: lower bound
        b: upper bound
        n: (optional) trials
        """
        if n == None:
            return random.randint(a, b)
        if type(n) == int and 1000 > n > 0:
            return [random.randint(a, b) for c in range(n)]

    def randnorm(µ, σ, n: int = None):
        if n == None:
            return random.gauss(µ, σ)
        if type(n) == int and 1000 > n > 0:
            return [random.gauss(µ, σ) for c in range(n)]

    def randbin(n, p, s: int = None):
        if s == None:
            return binom.rvs(n, p)
        if type(s) == int and 1000 > s > 0:
            return [binom.rvs(n, p) for c in range(s)]


class Angle:
    def DMS(degrees: float):
        """
        Degrees to Degree, minutes, seconds
        """
        raw_left = degrees - int(degrees)
        raw_minute = raw_left * 60
        minutes = int(raw_minute)
        raw_seconds = raw_minute - minutes
        seconds = raw_seconds * 3600
        return f"\n%i°, %i´, %i´´" % (int(degrees), minutes, seconds)


class Mfunc:
    def asin(θ, evaluate: bool = True):
        if evaluate:
            return sym.asin(θ).evalf(displayDecLim)
        else:
            return sym.asin(θ)

    def acos(θ, evaluate: bool = True):
        if evaluate:
            return sym.acos(θ).evalf(displayDecLim)
        else:
            return sym.acos(θ)

    def atan(θ, evaluate: bool = True):
        if evaluate:
            return sym.atan(θ).evalf(displayDecLim)
        else:
            return sym.atan(θ)

    def sin(θ, evaluate: bool = True):
        if evaluate:
            return sym.sin(θ).evalf(displayDecLim)
        else:
            return sym.sin(θ)

    def cos(θ, evaluate: bool = True):
        if evaluate:
            return sym.cos(θ).evalf(displayDecLim)
        else:
            return sym.cos(θ)

    def tan(θ, evaluate: bool = True):
        if evaluate:
            return sym.tan(θ).evalf(displayDecLim)
        else:
            return sym.tan(θ)

    def sqrt(x, evaluate: bool = True):
        if evaluate:
            return sym.sqrt(x).evalf(displayDecLim)
        else:
            return sym.sqrt(x)

    def log(x, evaluate: bool = True):
        if evaluate:
            return sym.log(x, 10).evalf(displayDecLim)
        else:
            return sym.log(x, 10)

    def ln(x, evaluate: bool = True):
        if evaluate:
            return sym.log(x, math.e).evalf(displayDecLim)
        else:
            return sym.log(x, math.e)

    def ep(x, evaluate: bool = True):
        if evaluate:
            return sym.exp(x).evalf(displayDecLim)
        else:
            return sym.exp(x)


# x = init("x")
# exp = Mfunc.ep(x ** 2) * Mfunc.cos(x) / (6 * Mfunc.ln(x))
# exp = x ** 2
# print(Math.fMax(exp, x, 0, 9), Math.fMin(exp, x, 0, 9))
