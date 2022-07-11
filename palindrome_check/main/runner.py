"""
"""

from palindrome_check.corefunctions import Palindromecheck

def main() -> None:
    input_val = input("Please enter the string to check palindrome condition ")
    palindromecheck = Palindromecheck(input_val)
    palindromecheck.get_result()

if __name__ == "__main__":
    main()

