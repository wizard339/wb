import pandas as pd
from article import Article
from brand import Brand
from item import Item


class Detail:

    def __init__(self, data):
        self.data = data

    def get_unique_article(self):
        """
        Возвращает список артикулов, заказанных/проданных/возвращенных
        в течение недели, в виде списка
        input: pd.DataFrame
        output: list
        """
        return list(set(self.data['Артикул поставщика']))

    def get_unique_brands(self):
        """
        Возвращает список брендов, заказанных/проданных/возвращенных
        в течение недели, в виде списка
        input: pd.DataFrame
        output: list
        """
        return list(set(self.data['Бренд']))

    def get_unique_items(self):
        """
        Возвращает список предметов, заказанных/проданных/возвращенных
        в течение недели, в виде списка
        input: pd.DataFrame
        output: list
        """
        return list(set(self.data['Предмет']))

    def get_unique_nomenclature(self):
        """
        Возвращает список номенклатуры, заказанных/проданных/возвращенных
        в течение недели, в виде списка
        input: pd.DataFrame
        output: list
        """
        return list(set(self.data['Код номенклатуры']))

    def make_table_by_article(self, save=False):
        table = pd.DataFrame(columns=[
            'Бренд',
            'Предмет',
            'Артикул поставщика',
            'Номенклатура (код 1С)',
            'Продажи, шт',
            'Продажи (ВБ реализовал товар), руб',
            'Продажи (к перечислению за реализованный товар), руб',
            'Возвраты, шт',
            'Возвраты (ВБ реализовал товар), руб',
            'Возвраты (к перечислению за реализованный товар), руб',
            'Общее количество логистик',
            'Количество возвратной логистики',
            'Общая стоимость логистики',
            'Сумма штрафов МП',
            'кВВ факт, %',
            'СПП факт',
            'Доля продаж с СПП',
            'ВБ реализовал товар, руб',
            'К перечислению за реализованный товар, руб',
            'Возмещение Расходов услуг поверенного, руб',
            'Вознаграждение Вайлдберриз (ВВ), без НДС',
            'НДС с Вознаграждения Вайлдберриз'
        ])
        for art in self.get_unique_article():
            article = Article(self.data, art)
            new_row = {
                'Бренд': article.get_brand_name(),
                'Предмет': article.get_item(),
                'Артикул поставщика': art,
                'Номенклатура (код 1С)': article.get_nomenclature(),
                'Продажи, шт': article.get_number_sales(),
                'Продажи (ВБ реализовал товар), руб': article.get_sales_sum(),
                'Продажи (к перечислению за реализованный товар), руб': article.get_sales_to_transfer_sum(),
                'Возвраты, шт': article.get_number_refunds(),
                'Возвраты (ВБ реализовал товар), руб': article.get_refunds_sum(),
                'Возвраты (к перечислению за реализованный товар), руб': article.get_refunds_to_transfer_sum(),
                'Общее количество логистик': article.get_number_shipments(),
                'Количество возвратной логистики': article.get_number_ref_shipments(),
                'Общая стоимость логистики': article.get_shipments_sum(),
                'Сумма штрафов МП': article.get_charge_mp_sum(),
                'кВВ факт, %': article.get_kvv_mean(),
                'СПП факт': article.get_spp_mean(),
                'Доля продаж с СПП': article.get_spp_proportion(),
                'ВБ реализовал товар, руб': article.get_revenue_sum(),
                'К перечислению за реализованный товар, руб': article.get_to_transfer_sum(),
                'Возмещение Расходов услуг поверенного, руб': article.get_cost_agent_sum(),
                'Вознаграждение Вайлдберриз (ВВ), без НДС': article.get_wb_award_without_tax_sum(),
                'НДС с Вознаграждения Вайлдберриз': article.get_wa_award_tax_sum()
            }
            table = table.append(new_row, ignore_index=True)
        if save is True:
            table.to_excel('detail_by_article.xlsx')
        return table

    def make_table_by_brand(self, save=False):
        table = pd.DataFrame(columns=[
            'Бренд',
            'Продажи, шт',
            'Продажи (ВБ реализовал товар), руб',
            'Продажи (к перечислению за реализованный товар), руб',
            'Возвраты, шт',
            'Возвраты (ВБ реализовал товар), руб',
            'Возвраты (к перечислению за реализованный товар), руб',
            'Общее количество логистик',
            'Количество возвратной логистики',
            'Общая стоимость логистики',
            'Сумма штрафов МП',
            'кВВ факт, %',
            'СПП факт',
            'Доля продаж с СПП',
            'ВБ реализовал товар, руб',
            'К перечислению за реализованный товар, руб',
            'Возмещение Расходов услуг поверенного, руб',
            'Вознаграждение Вайлдберриз (ВВ), без НДС',
            'НДС с Вознаграждения Вайлдберриз'
        ])
        for br in self.get_unique_brands():
            brand = Brand(self.data, br)
            new_row = {
                'Бренд': br,
                'Продажи, шт': brand.get_number_sales(),
                'Продажи (ВБ реализовал товар), руб': brand.get_sales_sum(),
                'Продажи (к перечислению за реализованный товар), руб': brand.get_sales_to_transfer_sum(),
                'Возвраты, шт': brand.get_number_refunds(),
                'Возвраты (ВБ реализовал товар), руб': brand.get_refunds_sum(),
                'Возвраты (к перечислению за реализованный товар), руб': brand.get_refunds_to_transfer_sum(),
                'Общее количество логистик': brand.get_number_shipments(),
                'Количество возвратной логистики': brand.get_number_ref_shipments(),
                'Общая стоимость логистики': brand.get_shipments_sum(),
                'Сумма штрафов МП': brand.get_charge_mp_sum(),
                'кВВ факт, %': brand.get_kvv_mean(),
                'СПП факт': brand.get_spp_mean(),
                'Доля продаж с СПП': brand.get_spp_proportion(),
                'ВБ реализовал товар, руб': brand.get_revenue_sum(),
                'К перечислению за реализованный товар, руб': brand.get_to_transfer_sum(),
                'Возмещение Расходов услуг поверенного, руб': brand.get_cost_agent_sum(),
                'Вознаграждение Вайлдберриз (ВВ), без НДС': brand.get_wb_award_without_tax_sum(),
                'НДС с Вознаграждения Вайлдберриз': brand.get_wa_award_tax_sum()
            }
            table = table.append(new_row, ignore_index=True)
        if save is True:
            table.to_excel('detail_by_brand.xlsx')
        return table

    def make_table_by_item(self, save=False):
        table = pd.DataFrame(columns=[
            'Предмет',
            'Продажи, шт',
            'Продажи (ВБ реализовал товар), руб',
            'Продажи (к перечислению за реализованный товар), руб',
            'Возвраты, шт',
            'Возвраты (ВБ реализовал товар), руб',
            'Возвраты (к перечислению за реализованный товар), руб',
            'Общее количество логистик',
            'Количество возвратной логистики',
            'Общая стоимость логистики',
            'Сумма штрафов МП',
            'кВВ факт, %',
            'СПП факт',
            'Доля продаж с СПП',
            'ВБ реализовал товар, руб',
            'К перечислению за реализованный товар, руб',
            'Возмещение Расходов услуг поверенного, руб',
            'Вознаграждение Вайлдберриз (ВВ), без НДС',
            'НДС с Вознаграждения Вайлдберриз'
        ])
        for it in self.get_unique_items():
            item = Item(self.data, it)
            new_row = {
                'Предмет': it,
                'Продажи, шт': item.get_number_sales(),
                'Продажи (ВБ реализовал товар), руб': item.get_sales_sum(),
                'Продажи (к перечислению за реализованный товар), руб': item.get_sales_to_transfer_sum(),
                'Возвраты, шт': item.get_number_refunds(),
                'Возвраты (ВБ реализовал товар), руб': item.get_refunds_sum(),
                'Возвраты (к перечислению за реализованный товар), руб': item.get_refunds_to_transfer_sum(),
                'Общее количество логистик': item.get_number_shipments(),
                'Количество возвратной логистики': item.get_number_ref_shipments(),
                'Общая стоимость логистики': item.get_shipments_sum(),
                'Сумма штрафов МП': item.get_charge_mp_sum(),
                'кВВ факт, %': item.get_kvv_mean(),
                'СПП факт': item.get_spp_mean(),
                'Доля продаж с СПП': item.get_spp_proportion(),
                'ВБ реализовал товар, руб': item.get_revenue_sum(),
                'К перечислению за реализованный товар, руб': item.get_to_transfer_sum(),
                'Возмещение Расходов услуг поверенного, руб': item.get_cost_agent_sum(),
                'Вознаграждение Вайлдберриз (ВВ), без НДС': item.get_wb_award_without_tax_sum(),
                'НДС с Вознаграждения Вайлдберриз': item.get_wa_award_tax_sum()
            }
            table = table.append(new_row, ignore_index=True)
        if save is True:
            table.to_excel('detail_by_item.xlsx')
        return table
