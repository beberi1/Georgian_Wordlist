# არ აის დასრულებული

# აქ შეგიძლია შექმნა ახალი პაროლების კომბინაციები
# giorgi Giorgi gIorgi giOrgi gioRgi giorGi giorgI GIORGI  #
# giorgi -> g!orgi giorg! g!org!                           #
# giorgi12   8-9-10 მდე რომ შეივსოს                        # 
# 12giorgi   8-9-10 მდე რომ შეივსოს                        #
# giorgi1923 giorgi1924                                    
# giorgi"phonenumber"                                      



def remove_duplicates(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    unique_lines = set()
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            if line not in unique_lines:
                outfile.write(line)
                unique_lines.add(line)


def process_text(input_string, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(input_string + '\n')
    
    with open(output_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    # ყველა lowercase & uppercase
    lowercase_lines = [line.lower() for line in lines]
    uppercase_lines = [line.upper() for line in lines]
    alternating_capitalization_lines = [generate_alternating_capitalizations(line.strip()) for line in lines]
    
    # ჩაწერა ფაილში
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(lowercase_lines)
        outfile.writelines(uppercase_lines)
        for alt_lines in alternating_capitalization_lines:
            for alt_line in alt_lines:
                outfile.write(alt_line + '\n')

def generate_alternating_capitalizations(input_string):
    # დიდი ასოების გენერაცია
    capitalizations = []
    for i in range(len(input_string)):
        capitalized = input_string[:i] + input_string[i].upper() + input_string[i+1:]
        capitalizations.append(capitalized)
    return capitalizations


def replace_first_occurrence(word, letter, symbol):
    return word.replace(letter, symbol, 1)

def replace_second_occurrence(word, letter, symbol):
    parts = word.split(letter, 2)
    if len(parts) == 3:
        return letter.join(parts[:2]) + symbol + parts[2]
    return word

def replace_all_occurrences(word, letter, symbol):
    return word.replace(letter, symbol)

def process_words(input_file, output_file, letter, symbol):
    with open(input_file, 'r', encoding='utf-8') as infile:
        words = [line.strip() for line in infile]
    
    with open(output_file, 'a', encoding='utf-8') as outfile:
        for word in words:
            first_replacement = replace_first_occurrence(word, letter, symbol)
            outfile.write(first_replacement + '\n')

            second_replacement = replace_second_occurrence(word, letter, symbol)
            outfile.write(second_replacement + '\n')

            all_replacement = replace_all_occurrences(word, letter, symbol)
            outfile.write(all_replacement + '\n')

# 8 მდე შევსება
def process_and_fill_words(input_file, output_file):
    # 9, 10, 11 character lengths for words
    target_lengths = [9, 10, 11]

    def fill_word(word, target_length, append_at_end=False):
        if len(word.strip()) >= target_length:
            return word.strip()[:target_length]  # Return the first `target_length` characters if the word is already long enough
        else:
            # Fill the word with numbers to make it `target_length` characters long
            num_to_add = target_length - len(word.strip())
            if append_at_end:
                numbers = ''.join([str(i) for i in range(num_to_add, 0, -1)])
                filled_word = word.strip() + numbers
            else:
                numbers = ''.join([str(i) for i in range(1, num_to_add + 1)])
                filled_word = numbers + word.strip()
            return filled_word

    with open(input_file, 'r', encoding='utf-8') as infile:
        words = infile.readlines()
    
    with open(output_file, 'a', encoding='utf-8') as outfile:
        # First write words with numbers appended from the front
        for word in words:
            for target_length in target_lengths:
                filled_word = fill_word(word, target_length, append_at_end=False)
                outfile.write(filled_word + '\n')
        
        # Then write words with numbers appended from the back
        for word in words:
            for target_length in target_lengths:
                filled_word = fill_word(word, target_length, append_at_end=True)
                outfile.write(filled_word + '\n')





# რა გინდა ერქვას ახალ ფაილს?

# სიტვა რომელსაც მომხმარებელი შეიყვანს
saxeli = input("შეიყვანე სიტყვა: ")

# გამოსავალი ფაილი
input_file = r'pass.txt'
output_file = r'pass.txt'  


# დიდი და პატარა ასოების გაკეთება
process_text(saxeli, output_file)

# ასოების სიმბოლოებით შეცვლა
# აქ შეგიძლია დაამატო კიდევ რა ასოები გინდა რომ შეიცვალოს სხვადასხვა სიმბოლოთი
# პირველად წერ ასოს რომელიც გინდა შეიცვალოს და მეორედ სიმბოლოს რომლითაც გინდა რომ შეიცვალოს
process_words(input_file, output_file, 'i', '!')
process_words(input_file, output_file, 'e', '3')
process_words(input_file, output_file, 'o', '0')
process_words(input_file, output_file, 'a', '@')
process_words(input_file, output_file, 'b', '6')

# დუპლიკატების წაშლა
remove_duplicates(input_file, output_file)

# 8-მდე შევსება
process_and_fill_words(input_file, output_file)


