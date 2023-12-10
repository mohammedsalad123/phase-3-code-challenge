# phase-3-code-challenge
# Project Title
code challenge
## Author

- [Mohammed salad ali]


## License

This project is licensed under the [MTC].

<!-- challenge 1 -->
Function: convert
This function converts a time from 12-hour format to 24-hour format.

<!-- Inputs: -->
hour: An integer representing the hour in the range of 1 to 12, inclusive.
minute: An integer representing the minute in the range of 0 to 59, inclusive.
period: A string indicating the period, either "am" or "pm".

<!-- Output: -->
A four-digit string representing the time in 24-hour format (HH:MM).
Functionality:
Adjusts the hour for PM times by adding 12 to the hour if it's not already 12 PM.
Adjusts the hour for AM times at 12:00 AM by setting the hour to 0.
Formats the time in 24-hour notation with two digits for hour and minute.
Returns the time in 24-hour format as a concatenated four-digit string.

<!-- challenge 2 -->
Function: check number
This function checks if exactly two out of three integers are positive.

<!-- Inputs: -->
a, b, c: Integers to be evaluated.
<!-- Output: -->
Returns True if exactly two out of the three integers are positive; otherwise, returns False.
Functionality:
Counts the number of positive integers among the three given integers (a, b, c).
Returns True if exactly two out of the three integers are positive.
Returns False if any other number of positive integers are found (0, 1, or 3).

<!-- challenge 3 -->
Function: highest_value_consonant_substring
This function calculates the highest value of consonant substrings within a given string.

<!-- Inputs: -->
s: A lowercase string containing alphabetic characters only (no spaces).

<!-- Output: -->
Returns the highest value of consonant substrings found within the given string.
Functionality:
Iterates through the string s character by character.
Identifies consonant substrings (sequences of consecutive consonants).
Calculates the value of each consonant substring based on the position of its characters in the alphabet (a = 1, b = 2, ..., z = 26).
Tracks the highest value found among these consonant substrings.
Returns the highest value of consonant substrings.
