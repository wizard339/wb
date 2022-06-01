import requests, time
import pandas as pd
import numpy as np

# добавить api-ключ после знака равенства
API_V1 = '&key='

date = input('Введите дату в формате "2021-12-18" без кавычек: ')
flag = input('Введите "1", если необходимо получить данные за указанную дату, или "0", если необходимо получить данные с указанной даты по настоящий момент: ')
time_ = '03:00:00'

if flag == '0':
    time_ = input('Введите время, с которого начнется отчет, в формате "21:00:00" без кавычек: ')

dateFrom = date + 'T' + time_ + 'Z'
response_sales = requests.get('https://suppliers-stats.wildberries.ru/api/v1/supplier/sales?dateFrom=' + dateFrom + '&flag=' + flag + api_v1)

if response_sales.status_code == 200:
    print('sales have been successfully uploaded!')
elif response_sales.status_code == 404:
    print('Error 404: sales not found!')

response_orders = requests.get('https://suppliers-stats.wildberries.ru/api/v1/supplier/orders?dateFrom=' + dateFrom + '&flag=' + flag + api_v1)

if response_orders.status_code == 200:
    print('orders have been successfully uploaded!')
elif response_orders.status_code == 404:
    print('Error 404: orders not found!')

# получим текущее время
cur_time = time.ctime()
cur_time = cur_time[-13:-5]
cur_time = cur_time[:2] + '-' + cur_time[3:5] + '-' + cur_time[6:]

# сохраним заказы и продажи в DataFrame для дальнейшей обработки и в файл
data_sales = pd.DataFrame(response_sales.json())
data_sales.to_excel('sales_' + date + '_' + cur_time + '.xlsx')
data_orders = pd.DataFrame(response_orders.json())
data_orders.to_excel('orders_' + date + '_' + cur_time + '.xlsx')

# получим список всех артикулов, по которым были заказы/продажи/возвраты
art_list = np.array(list(set(data_orders['supplierArticle']).union(set(data_sales['supplierArticle']))))
# сформируем np.array массивы с заказами, продажами и возвратами
sum_orders = np.array([np.sum(data_orders['quantity'][data_orders['supplierArticle'] == art]) for art in art_list])
sum_sales = np.array([np.sum(data_sales['quantity'][(data_sales['supplierArticle'] == art) & (data_sales['quantity'] > 0)]) for art in art_list])
sum_refunds = np.array([np.abs(np.sum(data_sales['quantity'][(data_sales['supplierArticle'] == art) & (data_sales['quantity'] < 0)])) for art in art_list])
# формируем DataFrame
result_table = pd.DataFrame({'Артикул': art_list,
                             'Заказано, шт': sum_orders,
                             'Продано, шт': sum_sales,
                             'Возвратов, шт': sum_refunds})
# сохраняем DataFrame в файл
result_table.to_excel('текущие продажи ' + date + ' ' + cur_time + '.xlsx')
