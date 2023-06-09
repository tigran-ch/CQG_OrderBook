# CQG_OrderBook

Необходимо реализовать простейший биржевой стакан (OrderBook) и максимально покрыть его
тестами.
OrderBook представляет собой таблицу, в которую отдельно собираются Заявки (Orders) на
Продажу (Ask) и Покупку (Bid) товара, например акций.
Заявка на продажу/покупку содержит следующие поля:
• id: целое число, номер заявки
• type: строка «bid» или «ask»
• price: целое число
• volume: целое число, количество лотов, которое готов продать или купить трейдер
Класс OrderBook должен предоставлять следующие возможности:
• добавлять одну или сразу несколько заявок
• удалять заявку по ее id
• получать информацию о заявке (type, price, volume) по id
• изменять параметры заявки (только price или volume) по id
• получать текущее состояние стакана (snapshot) в следующем виде:
{
'Asks': [
{
'price': value,
'volume': value
},
...
]
'Bids': [
{
'price': value,
'volume': value
},
...
]
}
Для каждой цены необходимо отображать суммарное количество лотов на покупку или продажу.
При выводе заявки в snapshot группируются по уровням цены и сортируются в порядке убывания
(Покупка) и в порядке возрастания (Продажа)
Условия реализации:
• код реализации ордербука должен быть написан без использования сторонних
библиотек/БД (можно использовать itertools, collections и другие стандартные библиотеки)
• тесты должны быть написаны с использованием фреймворка pytest, использование
сторонних библиотек – без ограничений
• в коде должны использоваться doc-strings и комментарии там, где необходимо
• проверки должны содержать сообщения об ошибках
• при желании можно самостоятельно поизучать детали работы биржевой торговли в
интернете в целях лучшего понимания предметной области, в которой предстоит работать