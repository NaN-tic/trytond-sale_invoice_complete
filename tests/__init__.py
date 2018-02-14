# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
try:
    from trytond.modules.sale_invoice_complete.tests.test_sale_invoice_complete import suite
except ImportError:
    from .test_sale_invoice_complete import suite

__all__ = ['suite']
