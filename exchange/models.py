from __future__ import unicode_literals

from django.db import models
from django.utils.six import python_2_unicode_compatible

from exchange.managers import ExchangeRateManager
from exchange.iso_4217 import code_list


@python_2_unicode_compatible
class Currency(models.Model):
    """Model holds a currency information for a nationality"""
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'currencies'

    def __str__(self):
        return self.code

    def get_numeric_code(self):
        return code_list[self.code]  # Let it raise an exception


@python_2_unicode_compatible
class ExchangeRate(models.Model):
    """Model to persist exchange rates between currencies"""
    source = models.ForeignKey('exchange.Currency', related_name='rates')
    target = models.ForeignKey('exchange.Currency')
    rate = models.DecimalField(max_digits=17, decimal_places=8)

    objects = ExchangeRateManager()

    def __str__(self):
        return '%s / %s = %s' % (self.source, self.target, self.rate)
