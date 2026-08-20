import math
import re
import random
import cmath
import statistics
from fractions import Fraction
from decimal import Decimal, getcontext

# ======================================
#         PRECISION SETTINGS
# ======================================
getcontext().prec = 50

# ======================================
#             TITLE
# ======================================
def pretty_title():
    print("=" * 80)
    print("               ULTIMATE MATHEMATICAL CALCULATOR")
    print("=" * 80)
    print("    Complete Mathematics: Algebra, Geometry, Statistics, Probability")
    print("    Type 'q' to quit, 'help' for guide\n")

# ======================================
#          COMPLETE GUIDE
# ======================================
def show_guide():
    print("\n" + "=" * 80)
    print("                    COMPLETE REFERENCE GUIDE")
    print("=" * 80)
    
    print("\n📐 BASIC ARITHMETIC:")
    print("  +, -, *, /, //, %, **, ^")
    
    print("\n📊 ALGEBRA & EQUATIONS:")
    print("  solve_linear(a,b) - solve ax + b = 0")
    print("  solve_quadratic(a,b,c) - solve ax² + bx + c = 0")
    print("  solve_cubic(a,b,c,d) - solve ax³ + bx² + cx + d = 0")
    
    print("\n🔢 NUMBER THEORY:")
    print("  gcd(a,b), lcm(a,b), is_prime(n)")
    print("  factors(n), fibonacci(n), factorial(n)")
    print("  divisors(n), phi(n) - Euler's totient")
    
    print("\n📈 LOGARITHMS & EXPONENTIALS:")
    print("  ln(x), log(x), log10(x), log2(x), log(x, base)")
    print("  exp(x), sqrt(x), cbrt(x), root(n,x)")
    
    print("\n📐 TRIGONOMETRY (DEGREES):")
    print("  sin(x), cos(x), tan(x), cot(x), sec(x), csc(x)")
    print("  asin(x), acos(x), atan(x)")
    
    print("\n🌀 HYPERBOLIC FUNCTIONS:")
    print("  sinh(x), cosh(x), tanh(x), coth(x), sech(x), csch(x)")
    
    print("\n📊 STATISTICS:")
    print("  mean(x1,x2,...), median(x1,x2,...), mode(x1,x2,...)")
    print("  variance(x1,x2,...), stdev(x1,x2,...)")
    
    print("\n🧮 LINEAR ALGEBRA (Section 5):")
    print("  det, inv, transpose, multiply, add, subtract, scalar")
    
    print("\n📐 GEOMETRY (Section 6):")
    print("  2D: square, rectangle, circle, triangle, etc.")
    print("  3D: cube, sphere, cylinder, cone, etc.")
    
    print("\n🔢 NUMBER SYSTEMS (Section 7):")
    print("  bin_to_dec, dec_to_bin, hex_to_dec, dec_to_hex")
    
    print("\n🎲 PROBABILITY (Section 8):")
    print("  binomial_prob, poisson_prob, permutations, combinations")
    
    print("\n" + "=" * 80 + "\n")

# ======================================
#         ALGEBRA FUNCTIONS
# ======================================
def solve_linear(a, b):
    if a == 0:
        return "No solution" if b != 0 else "Infinite solutions"
    return -b / a

def solve_quadratic(a, b, c):
    if a == 0:
        return solve_linear(b, c)
    d = b**2 - 4*a*c
    if d < 0:
        return [complex(-b, math.sqrt(-d))/(2*a), complex(-b, -math.sqrt(-d))/(2*a)]
    elif d == 0:
        return [-b/(2*a)]
    else:
        return [(-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a)]

def solve_cubic(a, b, c, d):
    if a == 0:
        return solve_quadratic(b, c, d)
    a1 = b/a
    b1 = c/a
    c1 = d/a
    p = b1 - a1**2/3
    q = 2*a1**3/27 - a1*b1/3 + c1
    disc = (q/2)**2 + (p/3)**3
    if disc >= 0:
        u = (-q/2 + math.sqrt(disc))**(1/3)
        v = (-q/2 - math.sqrt(disc))**(1/3)
        return [u + v - a1/3]
    else:
        r = math.sqrt((-p/3)**3)
        theta = math.acos(-q/(2*r))
        roots = []
        for k in range(3):
            root = 2 * r**(1/3) * math.cos((theta + 2*math.pi*k)/3) - a1/3
            roots.append(root)
        return roots

# ======================================
#         NUMBER THEORY FUNCTIONS
# ======================================
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def divisors(n):
    divs = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
    return sorted(divs)

def sum_divisors(n):
    return sum(divisors(n))

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def is_perfect(n):
    return sum_divisors(n) == 2*n

def is_abundant(n):
    return sum_divisors(n) > 2*n

def is_deficient(n):
    return sum_divisors(n) < 2*n

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a * b // math.gcd(a, b)

def fibonacci(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def factorial(n):
    return math.factorial(n)

def binomial(n, k):
    return math.comb(n, k)

def permutations(n, k):
    return math.perm(n, k)

# ======================================
#         STATISTICS FUNCTIONS
# ======================================
def quartiles(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    q1 = statistics.median(sorted_data[:n//2])
    q2 = statistics.median(sorted_data)
    q3 = statistics.median(sorted_data[(n+1)//2:])
    return {"Q1": q1, "Q2": q2, "Q3": q3}

def iqr(data):
    q = quartiles(data)
    return q["Q3"] - q["Q1"]

# ======================================
#         MATRIX OPERATIONS
# ======================================
def det_2x2(M):
    return M[0][0]*M[1][1] - M[0][1]*M[1][0]

def det_3x3(M):
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

def inv_2x2(M):
    det = det_2x2(M)
    if det == 0:
        return "Matrix is singular"
    return [[M[1][1]/det, -M[0][1]/det],
            [-M[1][0]/det, M[0][0]/det]]

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        return "Cannot multiply: dimensions don't match"
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_add(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Cannot add: dimensions don't match"
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_subtract(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Cannot subtract: dimensions don't match"
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scalar_multiply(s, M):
    return [[s * M[i][j] for j in range(len(M[0]))] for i in range(len(M))]

# ======================================
#         GEOMETRY SHAPE CALCULATOR
# ======================================
shape_list = [
    "square", "rectangle", "parallelogram", "rhombus", "triangle",
    "equilateral", "isosceles", "right_triangle", "trapezoid",
    "pentagon", "hexagon", "octagon", "circle", "ellipse",
    "cube", "cuboid", "sphere", "cylinder", "pyramid", "cone"
]

shape_params = {
    "square": ["side"],
    "rectangle": ["length", "width"],
    "parallelogram": ["base", "height", "side"],
    "rhombus": ["side", "major_diagonal", "minor_diagonal"],
    "triangle": ["base", "height", "side2", "side3"],
    "equilateral": ["side"],
    "isosceles": ["base", "height", "side"],
    "right_triangle": ["base", "height", "hypotenuse"],
    "trapezoid": ["base1", "base2", "height", "side1", "side2"],
    "pentagon": ["side"],
    "hexagon": ["side"],
    "octagon": ["side"],
    "circle": ["radius"],
    "ellipse": ["major_axis", "minor_axis"],
    "cube": ["side"],
    "cuboid": ["length", "width", "height"],
    "sphere": ["radius"],
    "cylinder": ["radius", "height"],
    "pyramid": ["base_side", "height"],
    "cone": ["radius", "height"]
}

def print_shapes_menu():
    print("\n" + "=" * 60)
    print("                    GEOMETRY SHAPES")
    print("=" * 60)
    print("2D SHAPES (Area & Perimeter):")
    print("-" * 40)
    two_d = ["square", "rectangle", "parallelogram", "rhombus", "triangle",
             "equilateral", "isosceles", "right_triangle", "trapezoid",
             "pentagon", "hexagon", "octagon", "circle", "ellipse"]
    for i, s in enumerate(two_d, 1):
        print(f"{i:2}) {s.capitalize().replace('_', ' ')}")
    
    print("\n3D SHAPES (Volume & Surface Area):")
    print("-" * 40)
    three_d = ["cube", "cuboid", "sphere", "cylinder", "pyramid", "cone"]
    for i, s in enumerate(three_d, len(two_d)+1):
        print(f"{i:2}) {s.capitalize().replace('_', ' ')}")
    print("=" * 60)

def shape_calculator():
    while True:
        print_shapes_menu()
        choice = input("\nEnter shape name or number (or 'q' to go back): ").strip().lower()
        
        if choice == 'q':
            return
        
        selected_shape = None
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(shape_list):
                selected_shape = shape_list[idx]
        else:
            for shape in shape_list:
                if choice in shape:
                    selected_shape = shape
                    break
        
        if not selected_shape:
            print("Invalid shape. Please try again.")
            continue
        
        params = shape_params[selected_shape]
        values = {}
        print(f"\n{'='*40}")
        print(f"  {selected_shape.upper().replace('_', ' ')}")
        print('='*40)
        
        for p in params:
            display_name = p.replace('_', ' ').capitalize()
            values[p] = float(input(f"Enter {display_name}: "))
        
        print("\n" + "-" * 40)
        print("RESULTS:")
        print("-" * 40)
        
        if selected_shape == "square":
            a = values["side"]
            print(f"Perimeter (4×side) = {4*a}")
            print(f"Area (side²) = {a*a}")
        
        elif selected_shape == "rectangle":
            l, w = values["length"], values["width"]
            print(f"Perimeter (2(L+W)) = {2*(l+w)}")
            print(f"Area (L×W) = {l*w}")
        
        elif selected_shape == "parallelogram":
            b, h, s = values["base"], values["height"], values["side"]
            print(f"Area (base×height) = {b*h}")
            print(f"Perimeter (2(base+side)) = {2*(b+s)}")
        
        elif selected_shape == "rhombus":
            side, D, d = values["side"], values["major_diagonal"], values["minor_diagonal"]
            print(f"Area (D×d/2) = {D*d/2}")
            print(f"Perimeter (4×side) = {4*side}")
        
        elif selected_shape == "triangle":
            b, h, s2, s3 = values["base"], values["height"], values["side2"], values["side3"]
            print(f"Area (base×height/2) = {b*h/2}")
            print(f"Perimeter (base+s2+s3) = {b+s2+s3}")
        
        elif selected_shape == "equilateral":
            s = values["side"]
            print(f"Area (s²√3/4) = {s*s*math.sqrt(3)/4}")
            print(f"Perimeter (3s) = {3*s}")
        
        elif selected_shape == "isosceles":
            b, h, s = values["base"], values["height"], values["side"]
            print(f"Area (b×h/2) = {b*h/2}")
            print(f"Perimeter (b+2s) = {b+2*s}")
        
        elif selected_shape == "right_triangle":
            b, h, c = values["base"], values["height"], values["hypotenuse"]
            if abs(b*b + h*h - c*c) > 0.0001:
                print("Error: Not a right triangle.")
            else:
                print(f"Area (b×h/2) = {b*h/2}")
                print(f"Perimeter = {b+h+c}")
        
        elif selected_shape == "trapezoid":
            B1, B2, h, s1, s2 = values["base1"], values["base2"], values["height"], values["side1"], values["side2"]
            print(f"Area ((B1+B2)/2×h) = {(B1+B2)/2*h}")
            print(f"Perimeter = {B1+B2+s1+s2}")
        
        elif selected_shape == "pentagon":
            s = values["side"]
            area = (5*s*s) / (4*math.tan(math.pi/5))
            print(f"Area = {area}")
            print(f"Perimeter = {5*s}")
        
        elif selected_shape == "hexagon":
            s = values["side"]
            print(f"Area = {3*math.sqrt(3)/2*s*s}")
            print(f"Perimeter = {6*s}")
        
        elif selected_shape == "octagon":
            s = values["side"]
            print(f"Area = {2*(1+math.sqrt(2))*s*s}")
            print(f"Perimeter = {8*s}")
        
        elif selected_shape == "circle":
            r = values["radius"]
            print(f"Circumference (2πr) = {2*math.pi*r}")
            print(f"Area (πr²) = {math.pi*r*r}")
        
        elif selected_shape == "ellipse":
            a, b = values["major_axis"] / 2, values["minor_axis"] / 2
            print(f"Area (πab) = {math.pi*a*b}")
        
        elif selected_shape == "cube":
            s = values["side"]
            print(f"Volume (s³) = {s**3}")
            print(f"Surface Area (6s²) = {6*s*s}")
        
        elif selected_shape == "cuboid":
            l, w, h = values["length"], values["width"], values["height"]
            print(f"Volume (l×w×h) = {l*w*h}")
            print(f"Surface Area 2(lw+lh+wh) = {2*(l*w + l*h + w*h)}")
        
        elif selected_shape == "sphere":
            r = values["radius"]
            print(f"Volume (4/3πr³) = {4/3*math.pi*r**3}")
            print(f"Surface Area (4πr²) = {4*math.pi*r*r}")
        
        elif selected_shape == "cylinder":
            r, h = values["radius"], values["height"]
            print(f"Volume (πr²h) = {math.pi*r*r*h}")
            print(f"Lateral Surface (2πrh) = {2*math.pi*r*h}")
            print(f"Total Surface (2πr(r+h)) = {2*math.pi*r*(r+h)}")
        
        elif selected_shape == "pyramid":
            s, h = values["base_side"], values["height"]
            print(f"Volume (s²h/3) = {s*s*h/3}")
        
        elif selected_shape == "cone":
            r, h = values["radius"], values["height"]
            print(f"Volume (πr²h/3) = {math.pi*r*r*h/3}")
        
        print("=" * 40 + "\n")

# ======================================
#         NUMBER SYSTEMS
# ======================================
def bin_to_dec(bin_str):
    return int(bin_str, 2)

def dec_to_bin(n):
    return bin(n)[2:]

def hex_to_dec(hex_str):
    return int(hex_str, 16)

def dec_to_hex(n):
    return hex(n)[2:].upper()

def oct_to_dec(oct_str):
    return int(oct_str, 8)

def dec_to_oct(n):
    return oct(n)[2:]

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

# ======================================
#         PROBABILITY FUNCTIONS
# ======================================
def binomial_prob(n, k, p):
    return math.comb(n, k) * (p**k) * ((1-p)**(n-k))

def poisson_prob(k, lam):
    return (lam**k * math.exp(-lam)) / math.factorial(k)

# ======================================
#         SAFE EVALUATION ENGINE
# ======================================
def safe_eval(expr):
    if not expr.strip():
        return "GUIDE_REQUESTED"
    
    # Remove spaces and convert ^ to **
    expr = expr.replace(" ", "")
    expr = expr.replace("^", "**")
    expr = expr.replace("π", "pi")
    
    # Build a safe environment with all needed functions
    safe_env = {
        # Built-in functions
        "abs": abs,
        "sum": sum,
        "max": max,
        "min": min,
        "len": len,
        "pow": pow,
        "round": round,
        "int": int,
        "float": float,
        "complex": complex,
        "str": str,
        "bool": bool,
        "list": list,
        "tuple": tuple,
        "range": range,
        "print": print,
        "type": type,
        
        # Constants
        "pi": math.pi,
        "e": math.e,
        "tau": 2 * math.pi,
        "phi": (1 + math.sqrt(5)) / 2,
        
        # Math functions - DIRECT, not through math module
        "sqrt": math.sqrt,
        "log": math.log,
        "log10": math.log10,
        "log2": math.log2,
        "exp": math.exp,
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "cot": lambda x: 1/math.tan(math.radians(x)) if math.tan(math.radians(x)) != 0 else "Undefined",
        "sec": lambda x: 1/math.cos(math.radians(x)) if math.cos(math.radians(x)) != 0 else "Undefined",
        "csc": lambda x: 1/math.sin(math.radians(x)) if math.sin(math.radians(x)) != 0 else "Undefined",
        "sinh": math.sinh,
        "cosh": math.cosh,
        "tanh": math.tanh,
        "factorial": math.factorial,
        "comb": math.comb,
        "perm": math.perm,
        "degrees": math.degrees,
        "radians": math.radians,
        "gcd": math.gcd,
        
        # Statistics
        "statistics": statistics,
        "mean": statistics.mean,
        "median": statistics.median,
        "mode": statistics.mode,
        "variance": statistics.variance,
        "stdev": statistics.stdev,
        
        # Custom functions
        "gcd": gcd,
        "lcm": lcm,
        "fibonacci": fibonacci,
        "factorial": factorial,
        "is_prime": is_prime,
        "solve_linear": solve_linear,
        "solve_quadratic": solve_quadratic,
        "solve_cubic": solve_cubic,
        "binomial": binomial,
        "permutations": permutations,
        "binomial_prob": binomial_prob,
        "poisson_prob": poisson_prob,
        
        # Random
        "random": random,
        "rand": random.random,
        "randint": random.randint,
    }
    
    # Handle factorial: 5! -> factorial(5)
    expr = re.sub(r"(\d+)!", r"factorial(\1)", expr)
    
    # Handle percentage: 50% -> 0.5
    expr = re.sub(r"(\d+)%", r"(\1/100)", expr)
    
    # Handle square root: sqrt(x) -> sqrt(x)
    expr = re.sub(r"sqrt\(([^)]*)\)", r"sqrt(\1)", expr)
    expr = re.sub(r"sqr\(([^)]*)\)", r"sqrt(\1)", expr)
    
    # Handle cube root: cbrt(x) -> x**(1/3)
    expr = re.sub(r"cbrt\(([^)]*)\)", r"(\1**(1/3))", expr)
    
    # Handle nth root: root(n,x) -> x**(1/n)
    expr = re.sub(r"root\(([^,]*),([^)]*)\)", r"(\2**(1/\1))", expr)
    
    # Handle log with base - use a marker
    expr = re.sub(r"ln\(([^)]*)\)", r"log(\1)", expr)
    expr = re.sub(r"log\(([^,]+),([^)]+)\)", r"__LOGBASE__(\1,\2)", expr)
    expr = re.sub(r"log10\(([^)]*)\)", r"log10(\1)", expr)
    expr = re.sub(r"log2\(([^)]*)\)", r"log2(\1)", expr)
    expr = re.sub(r"log\(([^)]*)\)", r"log10(\1)", expr)
    expr = re.sub(r"__LOGBASE__\(([^,]+),([^)]+)\)", r"log(\1,\2)", expr)
    
    # Handle exponential: exp(x) -> exp(x)
    expr = re.sub(r"exp\(([^)]*)\)", r"exp(\1)", expr)
    
    # Handle trig functions
    expr = re.sub(r"sin\(([^)]*)\)", r"sin(\1)", expr)
    expr = re.sub(r"cos\(([^)]*)\)", r"cos(\1)", expr)
    expr = re.sub(r"tan\(([^)]*)\)", r"tan(\1)", expr)
    expr = re.sub(r"cot\(([^)]*)\)", r"cot(\1)", expr)
    expr = re.sub(r"sec\(([^)]*)\)", r"sec(\1)", expr)
    expr = re.sub(r"csc\(([^)]*)\)", r"csc(\1)", expr)
    
    # Handle hyperbolic
    expr = re.sub(r"sinh\(([^)]*)\)", r"sinh(\1)", expr)
    expr = re.sub(r"cosh\(([^)]*)\)", r"cosh(\1)", expr)
    expr = re.sub(r"tanh\(([^)]*)\)", r"tanh(\1)", expr)
    expr = re.sub(r"coth\(([^)]*)\)", r"coth(\1)", expr)
    expr = re.sub(r"sech\(([^)]*)\)", r"sech(\1)", expr)
    expr = re.sub(r"csch\(([^)]*)\)", r"csch(\1)", expr)
    
    # Handle comb and perm
    expr = re.sub(r"comb\(([^,]*),([^)]*)\)", r"comb(\1,\2)", expr)
    expr = re.sub(r"perm\(([^,]*),([^)]*)\)", r"perm(\1,\2)", expr)
    
    # Handle inverse trig functions
    expr = re.sub(r"asin\(([^)]*)\)", r"degrees(asin(\1))", expr)
    expr = re.sub(r"acos\(([^)]*)\)", r"degrees(acos(\1))", expr)
    expr = re.sub(r"atan\(([^)]*)\)", r"degrees(atan(\1))", expr)
    
    try:
        # Evaluate in a safe environment
        result = eval(expr, {"__builtins__": None}, safe_env)
        
        if isinstance(result, complex):
            return f"Complex: {result.real} + {result.imag}i"
        return result
        
    except NameError as e:
        return f"Unknown function: {e}"
    except ValueError as e:
        return f"Invalid value: {e}"
    except ZeroDivisionError:
        return "Division by zero"
    except SyntaxError as e:
        return f"Syntax error: {e}"
    except Exception as e:
        return f"Error: {e}"

# ======================================
#         SUB-MENU FUNCTIONS
# ======================================
def algebra_menu():
    while True:
        print("\nALGEBRA & EQUATIONS")
        print("1) Solve Linear (ax + b = 0)")
        print("2) Solve Quadratic (ax² + bx + c = 0)")
        print("3) Solve Cubic (ax³ + bx² + cx + d = 0)")
        print("q) Back to main menu")
        
        sub = input("Choose: ").strip()
        
        if sub == 'q':
            return
        
        if sub == "1":
            a, b = map(float, input("Enter a b: ").split())
            print(f"Solution: x = {solve_linear(a,b)}")
        elif sub == "2":
            a, b, c = map(float, input("Enter a b c: ").split())
            roots = solve_quadratic(a,b,c)
            print(f"Roots: {roots}")
        elif sub == "3":
            a, b, c, d = map(float, input("Enter a b c d: ").split())
            roots = solve_cubic(a,b,c,d)
            print(f"Roots: {roots}")
        else:
            print("Invalid choice. Please try again.")

def number_theory_menu():
    while True:
        print("\nNUMBER THEORY")
        print("1) Prime Check")
        print("2) Prime Factors")
        print("3) Divisors")
        print("4) GCD")
        print("5) LCM")
        print("6) Fibonacci")
        print("7) Factorial")
        print("8) Perfect/Abundant/Deficient")
        print("9) Next Prime")
        print("q) Back to main menu")
        
        sub = input("Choose: ").strip()
        
        if sub == 'q':
            return
        
        if sub == "1":
            n = int(input("Number: "))
            print(f"Is prime: {is_prime(n)}")
        elif sub == "2":
            n = int(input("Number: "))
            print(f"Prime factors: {prime_factors(n)}")
        elif sub == "3":
            n = int(input("Number: "))
            print(f"Divisors: {divisors(n)}")
            print(f"Sum of divisors: {sum_divisors(n)}")
            print(f"Euler's totient: {phi(n)}")
        elif sub == "4":
            a,b = map(int, input("Two numbers: ").split())
            print(f"GCD: {gcd(a,b)}")
        elif sub == "5":
            a,b = map(int, input("Two numbers: ").split())
            print(f"LCM: {lcm(a,b)}")
        elif sub == "6":
            n = int(input("n: "))
            print(f"Fibonacci({n}): {fibonacci(n)}")
        elif sub == "7":
            n = int(input("n: "))
            print(f"{n}! = {factorial(n)}")
        elif sub == "8":
            n = int(input("Number: "))
            print(f"Perfect: {is_perfect(n)}")
            print(f"Abundant: {is_abundant(n)}")
            print(f"Deficient: {is_deficient(n)}")
        elif sub == "9":
            n = int(input("Number: "))
            print(f"Next prime: {next_prime(n)}")
        else:
            print("Invalid choice. Please try again.")

def statistics_menu():
    while True:
        print("\nSTATISTICS")
        print("Enter numbers separated by space (or 'q' to go back):")
        data_input = input("data> ").strip()
        
        if data_input == 'q':
            return
        
        data = list(map(float, data_input.split()))
        if len(data) < 2:
            print("Need at least 2 numbers")
            continue
        
        print(f"Count: {len(data)}")
        print(f"Sum: {sum(data)}")
        print(f"Mean: {statistics.mean(data)}")
        print(f"Median: {statistics.median(data)}")
        print(f"Mode: {statistics.mode(data)}")
        print(f"Variance: {statistics.variance(data)}")
        print(f"Std Dev: {statistics.stdev(data)}")
        print(f"Min: {min(data)}")
        print(f"Max: {max(data)}")
        print(f"Range: {max(data)-min(data)}")
        q = quartiles(data)
        print(f"Quartiles: Q1={q['Q1']}, Q2={q['Q2']}, Q3={q['Q3']}")
        print(f"IQR: {iqr(data)}")

def linear_algebra_menu():
    while True:
        print("\nLINEAR ALGEBRA")
        print("1) 2x2 Determinant")
        print("2) 3x3 Determinant")
        print("3) 2x2 Inverse")
        print("4) Transpose")
        print("5) Matrix Multiplication")
        print("6) Matrix Addition")
        print("7) Matrix Subtraction")
        print("8) Scalar Multiplication")
        print("q) Back to main menu")
        
        sub = input("Choose: ").strip()
        
        if sub == 'q':
            return
        
        if sub == "1":
            M = eval(input("Enter 2x2 matrix [[a,b],[c,d]]: "))
            print(f"Determinant: {det_2x2(M)}")
        elif sub == "2":
            M = eval(input("Enter 3x3 matrix [[a,b,c],[d,e,f],[g,h,i]]: "))
            print(f"Determinant: {det_3x3(M)}")
        elif sub == "3":
            M = eval(input("Enter 2x2 matrix [[a,b],[c,d]]: "))
            print(f"Inverse: {inv_2x2(M)}")
        elif sub == "4":
            M = eval(input("Enter matrix: "))
            print(f"Transpose: {transpose(M)}")
        elif sub == "5":
            A = eval(input("Enter matrix A: "))
            B = eval(input("Enter matrix B: "))
            print(f"A×B: {matrix_multiply(A,B)}")
        elif sub == "6":
            A = eval(input("Enter matrix A: "))
            B = eval(input("Enter matrix B: "))
            print(f"A+B: {matrix_add(A,B)}")
        elif sub == "7":
            A = eval(input("Enter matrix A: "))
            B = eval(input("Enter matrix B: "))
            print(f"A-B: {matrix_subtract(A,B)}")
        elif sub == "8":
            s = float(input("Enter scalar: "))
            M = eval(input("Enter matrix: "))
            print(f"{s}×M: {scalar_multiply(s,M)}")
        else:
            print("Invalid choice. Please try again.")

def number_systems_menu():
    while True:
        print("\nNUMBER SYSTEMS")
        print("1) Binary to Decimal")
        print("2) Decimal to Binary")
        print("3) Hexadecimal to Decimal")
        print("4) Decimal to Hexadecimal")
        print("5) Octal to Decimal")
        print("6) Decimal to Octal")
        print("q) Back to main menu")
        
        sub = input("Choose: ").strip()
        
        if sub == 'q':
            return
        
        if sub == "1":
            s = input("Binary: ")
            print(f"Decimal: {bin_to_dec(s)}")
        elif sub == "2":
            n = int(input("Decimal: "))
            print(f"Binary: {dec_to_bin(n)}")
        elif sub == "3":
            s = input("Hex: ")
            print(f"Decimal: {hex_to_dec(s)}")
        elif sub == "4":
            n = int(input("Decimal: "))
            print(f"Hex: {dec_to_hex(n)}")
        elif sub == "5":
            s = input("Octal: ")
            print(f"Decimal: {oct_to_dec(s)}")
        elif sub == "6":
            n = int(input("Decimal: "))
            print(f"Octal: {dec_to_oct(n)}")
        else:
            print("Invalid choice. Please try again.")

def probability_menu():
    while True:
        print("\nPROBABILITY")
        print("1) Binomial Probability")
        print("2) Poisson Probability")
        print("3) Permutations")
        print("4) Combinations")
        print("q) Back to main menu")
        
        sub = input("Choose: ").strip()
        
        if sub == 'q':
            return
        
        if sub == "1":
            n,k = map(int, input("n k: ").split())
            p = float(input("Probability p: "))
            print(f"P(X={k}) = {binomial_prob(n,k,p)}")
        elif sub == "2":
            k = int(input("k: "))
            lam = float(input("λ: "))
            print(f"P(X={k}) = {poisson_prob(k,lam)}")
        elif sub == "3":
            n,k = map(int, input("n k: ").split())
            print(f"P({n},{k}) = {permutations(n,k)}")
        elif sub == "4":
            n,k = map(int, input("n k: ").split())
            print(f"C({n},{k}) = {binomial(n,k)}")
        else:
            print("Invalid choice. Please try again.")

# ======================================
#         MAIN PROGRAM
# ======================================
def main():
    pretty_title()
    guide_shown = False

    while True:
        print("\n" + "=" * 40)
        print("MAIN MENU")
        print("=" * 40)
        print("1) Basic Calculator")
        print("2) Algebra & Equations")
        print("3) Number Theory")
        print("4) Statistics")
        print("5) Linear Algebra")
        print("6) Geometry")
        print("7) Number Systems")
        print("8) Probability")
        print("q) Quit")
        print("help) Complete Guide")
        
        choice = input("\nEnter option: ").strip()
        
        if choice.lower() == 'q':
            print("\nThank you for using the Ultimate Mathematical Calculator!")
            break
        
        if choice.lower() == 'help':
            show_guide()
            guide_shown = True
            continue
        
        if choice == "1":
            if not guide_shown:
                show_guide()
                guide_shown = True
            
            print("\nEnter expression (or 'q' to return):")
            while True:
                expr = input("calc> ")
                if expr.lower() == 'q':
                    break
                result = safe_eval(expr)
                if result == "GUIDE_REQUESTED":
                    show_guide()
                else:
                    print(f"Result: {result}")
        
        elif choice == "2":
            algebra_menu()
        
        elif choice == "3":
            number_theory_menu()
        
        elif choice == "4":
            statistics_menu()
        
        elif choice == "5":
            linear_algebra_menu()
        
        elif choice == "6":
            shape_calculator()
        
        elif choice == "7":
            number_systems_menu()
        
        elif choice == "8":
            probability_menu()
        
        else:
            print("Invalid option. Choose 1-8, 'q', or 'help'.")

if __name__ == "__main__":
    main()

print("\n" + "=" * 80)
print("                    CALCULATOR CLOSED")
print("=" * 80)