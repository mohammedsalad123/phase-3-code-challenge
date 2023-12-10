def highest_value_consonant_substring(s):
    vowels = 'aeiou'
    max_value = 0
    current_value = 0
    
    for char in s:
        if char not in vowels:
            # Calculate the value of consonants using their position in the alphabet
            current_value += ord(char) - ord('a') + 1
        else:
            # Update max_value if the current substring's value is higher
            max_value = max(max_value, current_value)
            current_value = 0  # Reset current_value for the next substring
    
    # Update max_value in case the last substring is the highest value
    max_value = max(max_value, current_value)
    
    print( max_value)
highest_value_consonant_substring("strength")