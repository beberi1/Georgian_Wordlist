def generate_numbers(prefixes, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for prefix in prefixes:
            # Calculate the number of digits left for the number part
            num_digits = 9 - len(str(prefix))
            
            for number in range(10**num_digits):  # From 0 to 10^num_digits - 1
                outfile.write(f"{prefix}{number:0{num_digits}d}\n")

# List of prefixes
prefixes = [
    501, 504, 505, 510, 511, 522, 533, 500,
    544, 550, 555, 568, 569, 571, 574, 575,
    579, 585, 591, 592, 595, 596, 597, 598, 599
]

# Example usage
output_file = r'numbers.txt'
generate_numbers(prefixes, output_file)
