import os


# აქ შეგიძლია შექმნა ახალი პაროლების კომბინაციები შენს მიერ შერჩეული სიტყვით

# ფუნქციონალი ასეთია
# giorgi Giorgi gIorgi giOrgi gioRgi giorGi giorgI GIORGI  #
# giorgi -> g!orgi giorg! g!org!                           #
# giorgi00->giorgi01   8-9-10 მდე რომ შეივსოს              # 
# 00giorgi->00giorgi   8-9-10 მდე რომ შეივსოს              #
# giorgi1923 giorgi1924                                    #
# 1923giorgi 1923giorgi                                    #
# giorgi0101 0101giorgi            თარიღები და სახელი     #

# phonenumber ებში საქართველოს თავსართებით გენერირდება 23 მილიონი სავარაუდო ნომერი
# შესაბამისად giorgi"phonenumber" ასეთი რაღაცის გაკეთება რესურსის მხრივ რთული იქნება 
# ასე შეიქმნება ძალიან ბევრი ვარიანტი და ამიტომაც კოდში ამ ფუნქციას არ დავამატებ


# დუბლიკატების მოშორება
def remove_duplicates(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    unique_lines = set()
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            if line not in unique_lines:
                outfile.write(line)
                unique_lines.add(line)

# დიდი და პატარა ასოებით დაწერა
def upper_and_lowercase(input_string, output_file):
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

# სიმბოლოებით შეცვლა
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

# 8 9 10 მდე შევსება რიცხვებით
def fill_with_numbers(input_file, output_file):
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            word = line.strip()  
            num_length = 8 - len(word)  
            num_length1 = 9 - len(word)
            num_length2 = 10 - len(word)
            # num_length3 = 11 - len(word) #თუ კიდევ გინდა მეტი სიგრძე დაამატო
            # ამოაკომენტარე ეს და კიდევ ქვემოთ

            # თავშიც ამატებს და ბოლოშიც
            if num_length>0:
                for i in range(10 ** num_length):  
                    combination = f"{word}{i:0{num_length}d}"
                    combination1 = f"{i:0{num_length}d}{word}"
                    output_f.write(combination + '\n')  
                    output_f.write(combination1 + '\n')  

            if num_length1>0:    
                for i in range(10 ** num_length1):  
                    combination = f"{word}{i:0{num_length1}d}"
                    combination1 = f"{i:0{num_length1}d}{word}"
                    output_f.write(combination + '\n')  
                    output_f.write(combination1 + '\n')  

            if num_length2>0:
                for i in range(10 ** num_length2):  
                    combination = f"{word}{i:0{num_length2}d}"
                    combination1 = f"{i:0{num_length2}d}{word}"
                    output_f.write(combination + '\n')  
                    output_f.write(combination1 + '\n')  
            
            # თუ გინდა კიდევ დამატო
            # if num_length3>0:
            #     for i in range(10 ** num_length3):  
            #         combination = f"{word}{i:0{num_length3}d}"
            #         combination1 = f"{i:0{num_length3}d}{word}"
            #         output_f.write(combination + '\n')  
            #         output_f.write(combination1 + '\n')  




# ამატებს წლებს თავში და ბოლოში
def append_years_to_words(input_file, output_file, start_year=1938, end_year=2024):
    with open(input_file, 'r', encoding='utf-8') as infile:
        words = infile.readlines()

    with open(output_file, 'a', encoding='utf-8') as outfile:
        for year in range(start_year, end_year + 1):
            for word in words:
                stripped_word = word.strip()
                if stripped_word:
                    # ამატებს ბოლოში
                    filled_word_back = f"{stripped_word}{year}"
                    outfile.write(filled_word_back + '\n')
                    filled_word_back = f"{stripped_word}{year}{year}"
                    outfile.write(filled_word_back + '\n')

                    # ამატებს თავში
                    filled_word_front = f"{year}{stripped_word}"
                    outfile.write(filled_word_front + '\n')
                    filled_word_front = f"{year}{year}{stripped_word}"
                    outfile.write(filled_word_front + '\n')

                    # თავშიც და ბოლოშიც
                    filled_word_front = f"{year}{stripped_word}{year}"
                    outfile.write(filled_word_front + '\n')

# ამატებს თვეების და დღეების კომბინაციებს ინპუტს
def append_date_variants_to_words(input_file, output_dates):
    # Step 1: Read the existing data from the file
    with open(input_file, 'r') as file:
        words = file.readlines()
    
    # Remove any trailing newline characters from the words
    words = [word.strip() for word in words]
    
    # Step 2: Generate the date variants and append them to each word
    updated_data = []
    for word in words:
        for month in range(1, 13):  # 1 to 12 months
            for day in range(1, 32):  # 1 to 31 days
                formatted_day = f"{day:02}"
                formatted_month = f"{month:02}"
                updated_data.append(f"{word}{formatted_month}{formatted_day}\n")
                updated_data.append(f"{word}{formatted_day}{formatted_month}\n")
                updated_data.append(f"{formatted_month}{formatted_day}{word}\n")
                updated_data.append(f"{formatted_day}{formatted_month}{word}\n")
                updated_data.append(f"{formatted_day}{word}{formatted_month}\n")
                updated_data.append(f"{formatted_month}{word}{formatted_day}\n")
    
    # Step 3: Write the updated data back to the file
    with open(output_dates, 'w') as file:
        file.writelines(updated_data)

# ამატებს პირველ ფაილს დანარჩენების კონტენტს
def append_files_data(file1, file2, file3, file4, output_file):
    with open(file1, 'r', encoding='utf-8') as f1:
        words1 = f1.readlines()

    words2=[]
    try:
        with open(file2, 'r', encoding='utf-8') as f2:
            words2 = f2.readlines()
    except FileNotFoundError:
        print(f"{file2} ფაილი არ არსებობს.(არაა სანერვიულო)")
    
    words3 = []
    try:
        with open(file3, 'r', encoding='utf-8') as f3:
            words3 = f3.readlines()
    except FileNotFoundError:
        print(f"{file3} ფაილი არ არსებობს.(არაა სანერვიულო)")

    words4 = []
    try:
        with open(file4, 'r', encoding='utf-8') as f4:
            words4 = f4.readlines()
    except FileNotFoundError:
        print(f"{file4} ფაილი არ არსებობს.(არაა სანერვიულო)")

    words1 = [word.strip() for word in words1 if word.strip()]
    words2 = [word.strip() for word in words2 if word.strip()]
    words3 = [word.strip() for word in words3 if word.strip()]
    words4 = [word.strip() for word in words4 if word.strip()]

    combined_words = words1 + words2 + words3 + words4

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for word in combined_words:
            outfile.write(word + '\n')

    try:
        os.remove(file1)
    except FileNotFoundError:
        print(f"{file1} არ არსებობს.(დაიკიდე)")
    except PermissionError:
        print(f"Permission denied: unable to remove {file1}.")
    except Exception as e:
        print(f"Error removing {file1}: {e}")
    
    try:
        os.remove(file2)
    except FileNotFoundError:
        print(f"{file2}  არ არსებობს.(დაიკიდე)")
    except PermissionError:
        print(f"Permission denied: unable to remove {file2}.")
    except Exception as e:
        print(f"Error removing {file2}: {e}")

    try:
        os.remove(file3)
    except FileNotFoundError:
        print(f"{file3}  არ არსებობს.(დაიკიდე)")
    except PermissionError:
        print(f"Permission denied: unable to remove {file3}.")
    except Exception as e:
        print(f"Error removing {file3}: {e}")

    try:
        os.remove(file4)
    except FileNotFoundError:
        print(f"{file4}  არ არსებობს.(დაიკიდე)")
    except PermissionError:
        print(f"Permission denied: unable to remove {file4}.")
    except Exception as e:
        print(f"Error removing {file4}: {e}")

# სიტვა რომელსაც მომხმარებელი შეიყვანს
saxeli = input("შეიყვანე სიტყვა რომლისგანაც გინდა შექმნა სიტყვების ჩამონათვალი: ")

# გამოსავალი ფაილი
input_file = r'pass.txt'
output_file = r'pass.txt' 

# საწყისი ფაილის შექმნა და სიტყვის ჩაწერა
with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(saxeli + '\n')

# დიდი და პატარა ასოების გაკეთება
upper_and_lowercase(saxeli, output_file)

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


output_dates = "pass3.txt"
append_date_variants_to_words(input_file, output_dates)


# 8-მდე შევსება
output_file = r'pass1.txt'  
fill_with_numbers(input_file, output_file)


output_file = r'pass2.txt'  
# ამატებს წლებს თავში და ბოლოში
append_years_to_words(input_file, output_file)

# ყველაფერს წერს ერთ ფაილში
file1="pass.txt"
file2="pass1.txt"
file3="pass2.txt"
file4="pass3.txt"
output="All_variants.txt"
append_files_data(file1,file2,file3,file4,output)