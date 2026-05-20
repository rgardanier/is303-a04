'''
Ryan Gardanier
IS 303
Number Analyzer

Inputs:
- user inputs a a bunch of numbers that finishes when a user presses the enter key
- use the try / except block to catch any errors that may occur

Processes:
- get_input() function to get the user's numbers and store them in a list
- analyze_numbers(numbers) function that analyzes the numbers and returns the results
- find_mean(numbers) function that calculates the mean of the numbers
- find_median(numbers) function that calculates the median of the numbers
- find_mode(numbers) function that calculates the mode of the numbers
- main() function that calls the other functions and runs the program
- print(results) function that prints the results of the analysis

Outputs:
- print the results of the analysis in a formatted string
'''
import statistics
import math


def get_input():
    numbers = []
    while True:
        try:
            number = input("Enter a number (or press Enter to finish): ")
            if number == '':
                break
            number = float(number)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers


def find_mean(numbers):
    mean = math.fsum(numbers) / len(numbers)
    return mean


def find_median(numbers):
    median = statistics.median(numbers)
    return median


def find_mode(numbers):
    try:
        mode = statistics.mode(numbers)
        return mode
    except statistics.StatisticsError:
        return "No unique mode; multiple values have the same frequency."


def get_printed_format(mean, median, mode):
    printed_format = f"Mean: {mean:.2f}\nMedian: {median}\nMode: {mode}"
    return printed_format


def main():
    list_of_numbers = get_input()
    if not list_of_numbers:
        print("No numbers were entered. Exiting the program.")
        return
    mean = find_mean(list_of_numbers)
    median = find_median(list_of_numbers)
    mode = find_mode(list_of_numbers)
    printed_format = get_printed_format(mean, median, mode)
    print("--- Here are the results of your analysis ---")
    print(printed_format)
    print("--- Thank you for using the Number Analyzer! ---")
    

if __name__ == "__main__":
    main()