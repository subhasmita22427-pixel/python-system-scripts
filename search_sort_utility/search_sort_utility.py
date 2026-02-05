# Search and Sort Utility
# A menu-driven program to perform operations on a list of numbers
# Includes search, sorting, filtering, and custom logic.

def get_number_list():
    """
    Takes input from user and converts it into a list of integers.
    Ensures only numbers are entered.
    """
    user_input = input("Enter numbers separated by space: ").strip()

    if not user_input:
        print("Input cannot be empty.")
        return None

    numbers = user_input.split()
    number_list = []

    for item in numbers:
        if item.lstrip("-").isdigit():
            number_list.append(int(item))
        else:
            print("Invalid input detected. Please enter numbers only.")
            return None

    return number_list


def search_number(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1


def sort_numbers(data, order):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if order == "asc" and data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
            elif order == "desc" and data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
    return data


def get_even_numbers(data):
    return [num for num in data if num % 2 == 0]


def get_odd_numbers(data):
    return [num for num in data if num % 2 != 0]


def get_multiples(data, value):
    return [num for num in data if num % value == 0]


def main():
    numbers = None

    while numbers is None:
        numbers = get_number_list()

    while True:
        print("\nChoose an operation:")
        print("1. Search a number")
        print("2. Sort numbers (Ascending)")
        print("3. Sort numbers (Descending)")
        print("4. Show even numbers")
        print("5. Show odd numbers")
        print("6. Show multiples of a number")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            target = input("Enter number to search: ")
            if target.lstrip("-").isdigit():
                result = search_number(numbers, int(target))
                if result != -1:
                    print(f"Number found at position {result}")
                else:
                    print("Number not found.")
            else:
                print("Invalid input. Please enter a number.")

        elif choice == "2":
            print("Sorted list (Ascending):", sort_numbers(numbers.copy(), "asc"))

        elif choice == "3":
            print("Sorted list (Descending):", sort_numbers(numbers.copy(), "desc"))

        elif choice == "4":
            print("Even numbers:", get_even_numbers(numbers))

        elif choice == "5":
            print("Odd numbers:", get_odd_numbers(numbers))

        elif choice == "6":
            value = input("Enter a number to find its multiples: ")
            if value.lstrip("-").isdigit() and int(value) != 0:
                print(
                    f"Multiples of {value}:",
                    get_multiples(numbers, int(value))
                )
            else:
                print("Please enter a valid non-zero number.")

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select between 1 and 7.")


if __name__ == "__main__":
    main()
