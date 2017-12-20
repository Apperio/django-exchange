try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from django.test import TestCase

from exchange.models import Currency, ExchangeRate
from exchange.adapters.openexchangerates import OpenExchangeRatesAdapter


class OpenExchangeRatesAdapterTest(TestCase):
    @patch('exchange.adapters.openexchangerates.OXRClient')
    def test_update(self, client):
        currency_dict = {
            'AED': 'United Arab Emirates Dirham',
            'AFN': 'Afghan Afghani', 'USD': 'USA'
        }

        latest_dict = {
            'disclaimer': "<Disclaimer data>",
            'license': "<License data>",
            'timestamp': 1358150409,
            'base': "USD",
            'rates': {
                'AED': 3.66,
                'AFN': 51.22,
                'USD': 1.0,
            }
        }

        client.get_currencies.return_value = currency_dict
        client.get_latest.return_value = latest_dict

        adapter = OpenExchangeRatesAdapter()

        adapter.update()

        self.assertEqual(Currency.objects.count(), len(currency_dict))
        self.assertEqual(
            list(Currency.objects.order_by('code').values_list('code', flat=True)),
            sorted(currency_dict.keys())
        )

        for k, v in latest_dict['rates'].items():
            rate = ExchangeRate.objects.get(
                source__code='USD',
                target__code=k,
            )
            self.assertEqual('%.2f' % rate.rate, '%.2f' % v)
