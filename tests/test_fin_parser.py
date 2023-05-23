import pytest
from unittest.mock import MagicMock, patch
from fin_parser import get_currency_rate, get_companies_list, get_company_info, get_top_companies


@pytest.mark.asyncio
async def test_get_currency_rate():
    with patch('aiohttp.ClientSession.get') as mock_get:
        mock_resp = MagicMock()
        mock_resp.json = MagicMock(return_value={'Valute': {'USD': {'Value': 70.0}}})
        mock_get.return_value.__aenter__.return_value = mock_resp
        rate = await get_currency_rate()
        assert rate == 70.0


@pytest.mark.asyncio
async def test_get_companies_list():
    with patch('aiohttp.ClientSession.get') as mock_get:
        mock_resp = MagicMock()
        mock_resp.text = MagicMock(return_value='<table><tr><td>1</td><td>Apple Inc.</td><td>AAPL</td></tr></table>')
        mock_get.return_value.__aenter__.return_value = mock_resp
        companies = await get_companies_list()
        assert companies == [{'name': 'Apple Inc.', 'code': 'AAPL'}]


@pytest.mark.asyncio
async def test_get_company_info():
    with patch('aiohttp.ClientSession.get') as mock_get:
        mock_resp = MagicMock()
        mock_resp.text = MagicMock(return_value='<span class="price-section__current-value">100.0</span><div' 
                                                'class="snapshot__data-item' 
                                                'snapshot__data-item--large">20.0</div><td class="table__td' 
                                                'snapshot__td snapshot__td--big">10.0%</td><div' 
                                                'class="snapshot__data-item">30.0</div>'
                                   )
        mock_get.return_value.__aenter__.return_value = mock_resp
        company_info = await get_company_info('AAPL')
        assert company_info == {'code': 'AAPL', 'price': '100.0', 'pe': '20.0', 'growth': '10.0%', 'profit': '30.0'}


@pytest.mark.asyncio
async def test_get_top_companies():
    with patch('main.get_companies_list') as mock_get_companies_list:
        mock_get_companies_list.return_value = [{'name': 'Apple Inc.', 'code': 'AAPL'}, {'name': 'Microsoft Corporation', 'code': 'MSFT'}]
        with patch('main.get_company_info') as mock_get_company_info:
            mock_get_company_info.side_effect = [{'code': 'AAPL', 'price': '100.0', 'pe': '20.0', 'growth': '10.0%', 'profit': '30.0'}, {'code': 'MSFT', 'price': '200.0', 'pe': '30.0', 'growth': '20.0%', 'profit': '40.0'}]
            with patch('builtins.open', create=True) as mock_open:
                await get_top_companies('price', 1)
                mock_open.assert_called_once_with('price.json', 'w')
                mock_open.return_value.__enter__.return_value.write.assert_called_once_with('[n    {n        '
                                                                                            '"code": "MSFT",n'
                                                                                            '"price": "200.0",n'
                                                                                            '"pe": "30.0",n'
                                                                                            '"growth": "20.0%",n'
                                                                                            '"profit": "40.0"n    }n]'
                                                                                            )