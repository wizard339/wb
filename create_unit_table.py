import os
import pandas as pd
import detail

# указать полный путь к папке, в которой размещен файл concat_detail.xlsx
path = '\\WB\\detalization\\unzip'
os.chdir(path)

data = pd.read_excel('concat_detail.xlsx')
# указать полный путь, куда будет помещен результат данного скрипта
path = '\\WB\\detalization\\result'
os.chdir(path)

unit_table = detail.Detail(data)
unit_table.make_table_by_article(save=True)
unit_table.make_table_by_brand(save=True)
unit_table.make_table_by_item(save=True)
