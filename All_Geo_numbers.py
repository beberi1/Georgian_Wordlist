def generate_numbers(prefixes, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for prefix in prefixes:
            num_digits = 9 - len(str(prefix))
            
            for number in range(10**num_digits):
                outfile.write(f"{prefix}{number:0{num_digits}d}\n")

# აქიდან აიღებს თავსართებს
prefixes = [
    501, 504, 505, 510, 511, 522, 533, 500,
    544, 550, 555, 568, 569, 571, 574, 575,
    579, 585, 591, 592, 595, 596, 597, 598, 599
]

# ჩაწერს numbers.txt ში
output_file = r'numbers.txt'
generate_numbers(prefixes, output_file)
