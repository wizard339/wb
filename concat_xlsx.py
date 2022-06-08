import os
import pandas as pd

# указать полный файл к разархивированным файлам с детализацией
path = '\\WB\\detalization\\unzip'
os.chdir(path)

list_files = os.listdir()

result_file = pd.read_excel(list_files[0])

if len(list_files) > 1:
    for f in list_files[1:]:
        new_file_to_concat = pd.read_excel(f)
        result_file = pd.concat([result_file, new_file_to_concat], ignore_index=True)

result_file.to_excel('concat_detail.xlsx')
