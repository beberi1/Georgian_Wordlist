# დუბლიკატების მოშორება / Remove duplicats
def remove_duplicates(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    unique_lines = set()
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            if line not in unique_lines:
                outfile.write(line)
                unique_lines.add(line)

# ფაილების არჩევა / File addresses
input_file = r'Surnames\Surnames.txt'
output_file = r'Surnames\Unique_Surnames.txt'
remove_duplicates(input_file, output_file)

input_file = r'Names\Names.txt'
output_file = r'Names\Unique_Names.txt'
remove_duplicates(input_file, output_file)



# დაფორმატება
# პატარა_ასოებით
# დიდი_ასოებით
# პირველიდიდი_ასო
# სახელის_პირველი_ასო.გვარი
def process_text(input_file, output_file):
    # ინპუტის წაკითხვაი / Read input
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    # აქ შეგიძლია დაამატო სხვადასხვა ვარიანტი / you can add variants
    lowercase_lines = [line.lower() for line in lines]
    first_letter_uppercase_lines = [line.capitalize() for line in lines]
    uppercase_lines = [line.upper() for line in lines]
    
    # output ში ჩაწერა / write in output
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(lowercase_lines)
        outfile.writelines(first_letter_uppercase_lines)
        outfile.writelines(uppercase_lines)

# მისამართები / Addresses
input_file = r'Surnames\Unique_Surnames.txt'
output_file = r'Surnames\Unique_Surnames.txt'
process_text(input_file, output_file)

input_file = r'Names\Unique_Names.txt'
output_file = r'Names\Unique_Names.txt'
process_text(input_file, output_file)



# შერევა სახელისა და გვარის / Shuffle name and surname
def generate_name_surname_combinations(first, second, output_file):
    # სახელების წაკითხვა / Read Names
    with open(first, 'r', encoding='utf-8') as infile:
        names = [line.strip() for line in infile]
    
    # გვარების წაკითხვა / Read Surnames
    with open(second, 'r', encoding='utf-8') as infile:
        surnames = [line.strip() for line in infile]
    
    # კომბინაციები / Combinations
    combination1 = [f"{name}{surname}" for name in names for surname in surnames]
    combination2 = [f"{name}_{surname}" for name in names for surname in surnames]
    combination3 = [f"{name}-{surname}" for name in names for surname in surnames]
    combination4 = [f"{name}.{surname}" for name in names for surname in surnames]
    combination5 = [f"{name}/{surname}" for name in names for surname in surnames]
    combination6 = [f"{name}\{surname}" for name in names for surname in surnames]
    combination7 = [f"{name[0]}.{surname}" for name in names for surname in surnames]
    combination8 = [f"{name[0]}_{surname}" for name in names for surname in surnames]
    combination9 = [f"{name[0]}-{surname}" for name in names for surname in surnames]
    combination10 = [f"{name[0]}/{surname}" for name in names for surname in surnames]
    combination11 = [f"{name[0]}\{surname}" for name in names for surname in surnames]
    combination12 = [f"{name[0]}_{surname}" for name in names for surname in surnames]
    combination13 = [f"{name[0]}{surname}" for name in names for surname in surnames]
    
    # Write the combinations to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("\n".join(combination1) + "\n")
        outfile.write("\n".join(combination2) + "\n")
        outfile.write("\n".join(combination3) + "\n")
        outfile.write("\n".join(combination4) + "\n")
        outfile.write("\n".join(combination5) + "\n")
        outfile.write("\n".join(combination6) + "\n")
        outfile.write("\n".join(combination7) + "\n")
        outfile.write("\n".join(combination8) + "\n")
        outfile.write("\n".join(combination9) + "\n")
        outfile.write("\n".join(combination10) + "\n")
        outfile.write("\n".join(combination11) + "\n")
        outfile.write("\n".join(combination12) + "\n")
        outfile.write("\n".join(combination13) + "\n")

# NameSurname
first = r'Names\Unique_Names.txt'
second = r'Surnames\Unique_Surnames.txt'
output_file = r'combinations.txt'
generate_name_surname_combinations(first, second, output_file)

# SurnameName
first = r'Surnames\Unique_Surnames.txt'
second = r'Names\Unique_Names.txt'
output_file = r'combinations1.txt'
generate_name_surname_combinations(first, second, output_file)




# შლის 8 ზე ნაკლებ ასოიან სიტყვებს / removes words with less than 8 letters
def filter_short_words(input_file, output_file, min_length=8):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    filtered_lines = [line for line in lines if len(line.strip()) >= min_length]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(filtered_lines)

input_file = r'combinations.txt'
output_file = r'filtered_combinations.txt'
filter_short_words(input_file, output_file)

input_file = r'combinations1.txt'
output_file = r'filtered_combinations1.txt'
filter_short_words(input_file, output_file)



# ამატებს პირველი კობინაციების ფაილს მეორე კომბინაციების ფაილს / append combinations1 to combinations
def append_file_data(file1, file2, output_file):
    # Read the contents of the first file
    with open(file1, 'r', encoding='utf-8') as infile1:
        lines1 = infile1.readlines()
    
    # Read the contents of the second file
    with open(file2, 'r', encoding='utf-8') as infile2:
        lines2 = infile2.readlines()
    
    # Combine the contents with each word on a new line
    combined_lines = lines1 + lines2
    
    # Write the combined contents to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(combined_lines)

# Example usage
file1 = r'filtered_combinations.txt'
file2 = r'filtered_combinations1.txt'
output_file = r'FullWordlist.txt'
append_file_data(file1, file2, output_file)
