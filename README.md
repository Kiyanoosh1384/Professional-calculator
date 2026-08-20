                    ULTIMATE MATHEMATICAL CALCULATOR
                    Professional Python Calculator


                        Developed by: Kiyanoosh Shafiei
                        Version: 3.0
                        License: MIT


                        PROJECT DESCRIPTION


This is a comprehensive and professional mathematical calculator developed in 
Python. It covers all major branches of mathematics including:

• Basic Arithmetic & Advanced Operations
• Algebra & Equations (Linear, Quadratic, Cubic)
• Number Theory (Prime Numbers, GCD, LCM, Fibonacci, etc.)
• Statistics (Mean, Median, Mode, Variance, Quartiles, etc.)
• Linear Algebra (Matrix Operations, Determinant, Inverse, Transpose)
• Geometry (2D & 3D Shapes: Area, Perimeter, Volume, Surface Area)
• Number Systems (Binary, Hexadecimal, Octal Conversions)
• Probability (Binomial, Poisson, Permutations, Combinations)

This calculator is designed for students, teachers, engineers, researchers, 
and anyone who needs a reliable and complete mathematical tool.


                        SYSTEM REQUIREMENTS


• Python 3.6 or higher installed on your system
• No external libraries required (all built-in modules used)
• Operating System: Windows, Linux, or macOS


                        INSTALLATION GUIDE


STEP 1: Install Python
------------------------
If you don't have Python installed:

Windows:
1. Go to https://www.python.org/downloads/
2. Download Python 3.6 or higher
3. During installation, CHECK "Add Python to PATH"
4. Complete the installation

Linux (Ubuntu/Debian):
sudo apt update
sudo apt install python3 python3-pip

macOS:
brew install python3

STEP 2: Download the Project
------------------------------
Option A - Using Git (Recommended):
git clone https://github.com/yourusername/mathematical-calculator.git
cd mathematical-calculator

Option B - Manual Download:
1. Download the ZIP file from GitHub
2. Extract the ZIP file to your desired location
3. Open terminal/command prompt in that folder

STEP 3: Verify Installation
-----------------------------
Open terminal/command prompt and run:
python --version
or
python3 --version

You should see: Python 3.6 or higher


                        HOW TO RUN THE CALCULATOR


METHOD 1: Using Terminal/Command Prompt (Recommended)
------------------------------------------------------
Windows:
1. Open Command Prompt (cmd) or PowerShell
2. Navigate to the project folder:
   cd C:\path\to\calculator-folder
3. Run the calculator:
   python calculator.py

Linux/macOS:
1. Open Terminal
2. Navigate to the project folder:
   cd /path/to/calculator-folder
3. Run the calculator:
   python3 calculator.py

METHOD 2: Using VS Code
------------------------
1. Install Visual Studio Code
2. Open the project folder in VS Code
3. Press Ctrl+` (backtick) to open terminal
4. Type: python calculator.py
5. Press Enter

METHOD 3: Using IDLE (Python's Built-in IDE)
---------------------------------------------
1. Open IDLE
2. Click File → Open
3. Select calculator.py
4. Press F5 to run


                        QUICK START GUIDE


1. Run the calculator (see instructions above)
2. Main Menu will appear with 8 options:
   (1) Basic Calculator
   (2) Algebra & Equations
   (3) Number Theory
   (4) Statistics
   (5) Linear Algebra
   (6) Geometry
   (7) Number Systems
   (8) Probability

3. Type the number of your desired section and press Enter

4. Follow the prompts for each operation

5. Type 'q' to go back or exit

6. Type 'help' anytime for complete guide


                        BASIC CALCULATOR EXAMPLES


After selecting option 1 (Basic Calculator), try these:

calc> 2 + 3 * 4
Result: 14

calc> sqrt(144)
Result: 12.0

calc> 5!
Result: 120

calc> sin(30)
Result: 0.5

calc> ln(e)
Result: 1.0

calc> log(1024, 2)
Result: 10.0

calc> pi * 5^2
Result: 78.53981633974483

calc> abs(-15)
Result: 15

calc> comb(10, 3)
Result: 120

calc> perm(10, 3)
Result: 720

calc> sec(60)
Result: 2.0

calc> sinh(1)
Result: 1.1752011936438014

calc> q
(Returns to main menu)


                        KEYBOARD SHORTCUTS


q        : Quit current menu / Exit program
help     : Display complete reference guide
1-8      : Select menu options
space    : Separate numbers (e.g., 1 2 3 4)
^        : Power operation (e.g., 2^3 = 8)


                        IMPORTANT NOTES


1. All trigonometric functions work in DEGREES by default
   Example: sin(30) = 0.5 (not radians)

2. Use '.' for decimal points (e.g., 3.14, not 3,14)

3. For matrices, use the format: [[a,b],[c,d]]

4. For logarithm with custom base: log(x, base)
   Example: log(1024, 2) = 10.0

5. For natural logarithm: ln(x)
   Example: ln(e) = 1.0

6. For nth root: root(n, x)
   Example: root(3, 27) = 3.0

7. For factorial: number!
   Example: 5! = 120

8. For percentage: number%
   Example: 50% = 0.5


                        TROUBLESHOOTING


PROBLEM: "python is not recognized"
SOLUTION: Python is not installed or not in PATH
→ Reinstall Python and CHECK "Add Python to PATH"

PROBLEM: "ModuleNotFoundError: No module named 'xyz'"
SOLUTION: This calculator uses only built-in modules
→ Your Python installation might be corrupted
→ Reinstall Python

PROBLEM: Syntax errors in calculations
SOLUTION:
→ Check for missing parentheses: sqrt(144 → sqrt(144)
→ Check for missing operators: 2 3 → 2*3 or 2+3
→ Use correct function names: sqt(144) → sqrt(144)

PROBLEM: Wrong answers in trigonometry
SOLUTION: All trig functions use DEGREES, not radians
→ sin(30) = 0.5 (correct)
→ sin(0.5236) ≠ 0.5 (this is radians)

PROBLEM: Matrix operations not working
SOLUTION:
→ Use correct format: [[a,b],[c,d]]
→ Make sure dimensions match for multiplication


                        FOLDER STRUCTURE



mathematical-calculator/
├── calculator.py          # Main program file
├── README.md              # This documentation
└── LICENSE                # MIT License


                        SUPPORT & CONTACT


Developer: Kiyanoosh Shafiei

For support, questions, or feedback:
• Open an issue on GitHub
• Star the repository if you find it useful!


                        LICENSE


This project is licensed under the MIT License - see the LICENSE file for details.


                        SPECIAL NOTES FOR BEGINNERS


"I've never used Python before!"
1. Install Python from https://python.org
2. Make sure to check "Add Python to PATH"
3. Open Command Prompt/Terminal
4. Navigate to the folder with calculator.py
5. Type: python calculator.py
6. Press Enter

"I don't understand the menu options!"
• Type help at any time to see the complete guide
• Each section has clear prompts explaining what to do
• If you're stuck, type q to go back

"I got an error message!"
• Read the error message carefully
• Check if you typed the expression correctly
• Make sure all parentheses are closed
• For matrices, use the correct format


Made with ❤️ by Kiyanoosh Shafiei

