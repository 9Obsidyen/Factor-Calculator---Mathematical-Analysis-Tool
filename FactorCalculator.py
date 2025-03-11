"""
Factor Calculator - Mathematical Analysis Tool

This program:
- Lists all divisors of two positive integers provided by the user
- Finds common divisors
- Finds and lists prime factors
- Displays results in a visually appealing and structured format
"""

from typing import List, Set


def get_valid_positive_integer(prompt: str) -> int:
    """Prompts the user to enter a valid positive integer (greater than 2)."""
    while True:
        try:
            number = int(input(prompt))
            if number > 2:
                return number
            print("[❌ ERROR] Please enter an integer greater than 2.")
        except ValueError:
            print("[❌ ERROR] Invalid input. Please enter an integer.")


def calculate_divisors(number: int) -> List[int]:
    """Calculates all positive divisors of a given number."""
    return [i for i in range(2, number + 1) if number % i == 0]


def find_prime_factors(number: int) -> List[int]:
    """Finds the prime factors of a given number."""
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return sorted(set(factors))


def format_number_list(numbers: List[int], items_per_line: int = 8) -> str:
    """Formats a list of numbers into a structured text output."""
    if not numbers:
        return "[None]"
    return "\n".join(
        " ".join(f"{num:4}" for num in numbers[i : i + items_per_line])
        for i in range(0, len(numbers), items_per_line)
    )


def find_common_elements(set1: Set[int], set2: Set[int]) -> List[int]:
    """Finds common elements in two sets and returns them as a sorted list."""
    return sorted(set1.intersection(set2))


def print_section_header(title: str, width: int = 50, border_char: str = "═") -> None:
    """Prints a visually formatted section header."""
    print(f"\n{border_char * width}\n{title.center(width)}\n{border_char * width}")


def main() -> None:
    """Main execution flow of the program."""
    print_section_header(" FACTOR ANALYSIS TOOL ")

    number_y = get_valid_positive_integer("\nEnter the first number (Y): ")
    number_g = get_valid_positive_integer("Enter the second number (G): ")

    y_divisors = calculate_divisors(number_y)
    g_divisors = calculate_divisors(number_g)
    common_divisors = find_common_elements(set(y_divisors), set(g_divisors))
    y_prime_factors = find_prime_factors(number_y)
    g_prime_factors = find_prime_factors(number_g)

    print_section_header(f" Y ({number_y}) DIVISORS ", border_char="─")
    print(format_number_list(y_divisors))

    print_section_header(f" G ({number_g}) DIVISORS ", border_char="─")
    print(format_number_list(g_divisors))

    print_section_header(f" COMMON DIVISORS ({number_y} & {number_g}) ")
    print(format_number_list(common_divisors))

    print_section_header(f" Y ({number_y}) PRIME FACTORS ", border_char="─")
    print(format_number_list(y_prime_factors))

    print_section_header(f" G ({number_g}) PRIME FACTORS ", border_char="─")
    print(format_number_list(g_prime_factors))


if __name__ == "__main__":
    main()
