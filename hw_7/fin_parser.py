"""Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта: <br>
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:
* Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта [центробанка РФ](http://www.cbr.ru/development/sxml/))
* Код компании (справа от названия компании на странице компании)
* P/E компании (информация находится справа от графика на странице компании)
* Годовой рост/падение компании в процентах (основная таблица)
* Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и
проданы на уровне 52 Week High (справа от графика на странице компании)

Сохранить итоговую информацию в 4 JSON файла:
1. Топ 10 компаний с самими дорогими акциями в рублях.
2. Топ 10 компаний с самым низким показателем P/E.
3. Топ 10 компаний, которые показали самый высокий рост за последний год
4. Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.
"""


import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json

base_url = 'https://markets.businessinsider.com'


"""
get_currency_rate() function is responsible for getting the current US dollar to ruble exchange rate from the website 
of the Central Bank of Russia in JSON format.
"""


async def get_currency_rate():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.cbr-xml-daily.ru/daily_json.js') as resp:
            data = await resp.json(content_type='application/javascript')
            return data['Valute']['USD']['Value']


"""
get_companies_list() отвечает за получение списка компаний из индекса S&P 500 на сайте businessinsider.com.
Для этого она отправляет GET-запрос на страницу с индексом, получает HTML-код страницы, парсит его с помощью
библиотеки BeautifulSoup и извлекает из таблицы список компаний с их кодами.
"""


async def get_companies_list():
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url + '/index/components/s&p_500') as resp:
            html = await resp.text()
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find('table', {'class': 'table table-small no-margin'})
            rows = table.find_all('tr')
            companies = []
            for row in rows[1:]:
                cols = row.find_all('td')
                name = cols[1].text.strip()
                code = cols[2].text.strip()
                companies.append({'name': name, 'code': code})
            return companies


"""
get_company_info(code) function is responsible for getting information about the company with the given code.
To do this,it sends a GET request to the company page on businessinsider.com (http://businessinsider.com/) 
,gets the HTML code of
the page, parses it using the BeautifulSoup library, and extracts information about the stock price, P / E ratio
,growth and profit of the company from it.
"""


async def get_company_info(code):
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url + f'/stocks/{code.lower()}-stock') as resp:
            html = await resp.text()
            soup = BeautifulSoup(html, 'html.parser')
            price = soup.find('span', {'class': 'price-section__current-value'}).text.strip()
            pe = soup.find('div', {'class': 'snapshot__data-item snapshot__data-item--large'}).text.strip()
            growth = soup.find('td', {'class': 'table__td snapshot__td snapshot__td--big'}).text.strip()
            profit = soup.find_all('div', {'class': 'snapshot__data-item'})[-1].text.strip()
            return {'code': code, 'price': price, 'pe': pe, 'growth': growth, 'profit': profit}


"""
get_top_companies(sort_key, top_n) function is responsible for getting the list of companies with the highest value of
the given parameter (price, P/E ratio, growth or earnings). To do this, it calls the get_companies_list() function to
get a list of companies, creates a list of tasks to get information about each company using get_company_info() function
,runs these tasks in parallel using asyncio.gather() function, and sorts the results by the given parameter.
It then saves the resulting list in JSON format to a file with a name that matches the given parameter
"""


async def get_top_companies(sort_key, top_n):
    companies = await get_companies_list()
    tasks = [get_company_info(company['code']) for company in companies]
    results = await asyncio.gather(*tasks)
    results = sorted(results, key=lambda x: x[sort_key], reverse=True)[:top_n]
    with open(f'{sort_key}.json', 'w') as f:
        json.dump(results, f, indent=4)


"""
The main() function is the main function of the script. It calls get_currency_rate() to get the current USD/RUB exchange
rate and then calls get_top_companies() to get a list of companies with the highest price,
P/E ratio, growth, and earnings.
"""


async def main():
    currency_rate = await get_currency_rate()
    await get_top_companies('price', 10)
    await get_top_companies('pe', 10)
    await get_top_companies('growth', 10)
    await get_top_companies('profit', 10)


"""
The code in the if __name__ == '__main__': runs the main main() function using asyncio.run() function.
"""


if __name__ == '__main__':
    asyncio.run(main())