class Item:

    def __init__(self, data, item_name):
        self.data = data
        self.name = item_name

    def get_sales_sum(self):
        """
        Возвращает для продаж сумму столбца "Вайлдберриз реализовал Товар (Пр)"
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        frame = frame.loc[frame['Тип документа'] == 'Продажа']
        value = frame['Вайлдберриз реализовал Товар (Пр)'].sum()
        return value

    def get_refunds_sum(self):
        """
        Возвращает для продаж сумму столбца "Вайлдберриз реализовал Товар (Пр)"
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        frame = frame.loc[frame['Тип документа'] == 'Возврат']
        value = frame['Вайлдберриз реализовал Товар (Пр)'].sum()
        return value

    def get_revenue_sum(self):
        """
        Возвращает итоговую сумму "Вайлдберриз реализовал Товар (Пр)" для данного
        предмета
        """
        value = self.get_sales_sum() - self.get_refunds_sum()
        return value

    def get_cost_agent_sum(self):
        """
        Возвращает сумму столбца "Возмещение Расходов услуг поверенного"
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        sales = frame.loc[frame['Тип документа'] == 'Продажа']
        refunds = frame.loc[frame['Тип документа'] == 'Возврат']
        value = sales['Возмещение Расходов услуг поверенного'].sum() - refunds[
            'Возмещение Расходов услуг поверенного'].sum()
        return value

    def get_wb_award_without_tax_sum(self):
        """
        Возвращает сумму столбца "Вознаграждение Вайлдберриз (ВВ), без НДС"
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        sales = frame.loc[frame['Тип документа'] == 'Продажа']
        refunds = frame.loc[frame['Тип документа'] == 'Возврат']
        value = sales['Вознаграждение Вайлдберриз (ВВ), без НДС'].sum() - refunds[
            'Вознаграждение Вайлдберриз (ВВ), без НДС'].sum()
        return value

    def get_wa_award_tax_sum(self):
        """
        Возвращает сумму столбца "НДС с Вознаграждения Вайлдберриз"
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        sales = frame.loc[frame['Тип документа'] == 'Продажа']
        refunds = frame.loc[frame['Тип документа'] == 'Возврат']
        value = sales['НДС с Вознаграждения Вайлдберриз'].sum() - refunds[
            'НДС с Вознаграждения Вайлдберриз'].sum()
        return value

    def get_sales_to_transfer_sum(self):
        """
        Возвращает сумму для продаж столбца
        "К перечислению Продавцу за реализованный Товар"
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        frame = frame.loc[frame['Тип документа'] == 'Продажа']
        value = frame['К перечислению Продавцу за реализованный Товар'].sum()
        return value

    def get_refunds_to_transfer_sum(self):
        """
        Возвращает сумму для возвратов столбца
        "К перечислению Продавцу за реализованный Товар"
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        frame = frame.loc[frame['Тип документа'] == 'Возврат']
        value = frame['К перечислению Продавцу за реализованный Товар'].sum()
        return value

    def get_to_transfer_sum(self):
        """
        Возвращает итоговую сумму "К перечислению Продавцу за реализованный Товар"
        для данного предмета
        """
        value = self.get_sales_to_transfer_sum() - self.get_refunds_to_transfer_sum()
        return value

    def get_spp_proportion(self):
        """
        Возвращает долю продаж с СПП относительного общего числа продаж
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        num_sales = frame.loc[frame['Обоснование для оплаты'] == 'Продажа'].shape[0]
        if num_sales != 0:
            # затем отбираем только те строки, где СПП != 0
            frame = frame.loc[frame['Скидка постоянного Покупателя (СПП)'] != 0]
            value = (frame.shape[0] / num_sales) * 100
        else:
            value = 0
        return value

    def get_spp_mean(self):
        """
        Возвращает среднюю СПП
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        # затем отбираем только те строки, где СПП != 0
        frame = frame.loc[frame['Скидка постоянного Покупателя (СПП)'] != 0]
        if frame.shape[0] != 0:
            value = frame['Скидка постоянного Покупателя (СПП)'].mean()
        else:
            value = 0
        return value

    def get_kvv_mean(self):
        """
        Возвращает средний размер кВВ без учета СПП
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        frame = frame.loc[frame['Обоснование для оплаты'] == 'Продажа']
        if frame.shape[0] != 0:
            value = frame['Размер кВВ, %'].mean()
        else:
            value = 0
        return value

    def get_kvv_with_spp_mean(self):
        """
        Возвращает средний размер итогового кВВ после вычета СПП и без учета НДС
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        frame = frame.loc[frame['Обоснование для оплаты'] == 'Продажа']
        if frame.shape[0] != 0:
            value = frame['Итоговый кВВ без НДС, %'].mean()
        else:
            value = 0
        return value

    def get_number_sales(self):
        """
        Возвращает количество продаж по данному предмету
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        frame = frame.loc[frame['Тип документа'] == 'Продажа']
        value = frame['Кол-во'].sum()
        return value

    def get_number_refunds(self):
        """
        Возвращает количество возвратов по данному предмету
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        frame = frame.loc[frame['Тип документа'] == 'Возврат']
        value = frame['Кол-во'].sum()
        return value

    def get_number_ref_shipments(self):
        """
        Возвращает количество возвратной логистики
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        frame = frame.loc[frame['Обоснование для оплаты'] == 'Логистика']
        value = frame['Количество возврата'].sum()
        return value

    def get_number_shipments(self):
        """
        Возврашает общее количество логистик
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        frame = frame.loc[frame['Обоснование для оплаты'] == 'Логистика']
        value = frame['Количество доставок'].sum()
        return value

    def get_charge_mp_sum(self):
        """
        Возвращает сумму Штрафов МП
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        frame = frame.loc[frame['Обоснование для оплаты'] == 'Штраф МП']
        value = frame['Услуги по доставке товара покупателю'].sum()
        return value

    def get_shipments_sum(self):
        """
        Возвращает сумму столбца "Услуги по доставке товара покупателю"
        за вычетом Штрафов МП
        """
        frame = self.data.loc[self.data['Предмет'] == self.name]
        value = frame['Услуги по доставке товара покупателю'].sum() - self.get_charge_mp_sum()
        return value
