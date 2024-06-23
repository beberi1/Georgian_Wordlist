# ქმნის ფაილს რომელშიც წლები წერია
# 19201920 -ასე
# ამის გარდა აკეთებს დღეების და თვეების დამატებას თავში და ბოლოში ასე:
# day month year
# month day year
# year day month
# year month day

sawyisi_weli = 1920
saboloo_weli = 2030

with open('dates.txt', 'w') as file:
    for year in range(sawyisi_weli, saboloo_weli):
        file.write(f"{year}" + f"{year}" + '\n')
        for month in range(1, 13):  # 1 დან 12 თვემდე
            for day in range(1, 32):  # 1 დან 31 დღემდე
                formatted_day = f"{day:02}"
                formatted_month = f"{month:02}"
                formatted_year = f"{year:04}"
                # კომბინაცია თუ როგორ ჩაიწერება
                file.write(formatted_day + formatted_month + formatted_year + '\n')
                file.write(formatted_month + formatted_day + formatted_year + '\n')
                file.write(formatted_year + formatted_day + formatted_month + '\n')
                file.write(formatted_year + formatted_month + formatted_day + '\n')
