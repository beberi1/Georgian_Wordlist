# ქმნის ფაილს რომელშიც წლები წერია
# 19201920 -ასე
sawyisi_weli = 1920
saboloo_weli = 2030

with open('years.txt', 'w') as file:
    for weli in range(sawyisi_weli, saboloo_weli):
        file.write(str(weli) + str(weli) + '\n')
