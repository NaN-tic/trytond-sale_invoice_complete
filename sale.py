# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Sale']


class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'

    invoice_complete = fields.Boolean('Invoice complete', help='If marked '
        'invoices will be created only if the sale is complete', states={
            'readonly': (Eval('state') != 'draft'),
            'invisible': (Eval('invoice_method') != 'shipment'),
            }, depends=['state'])

    def create_invoice(self):
        if self.invoice_complete and not self.is_sale_complete():
            return
        return super(Sale, self).create_invoice()

    def is_sale_complete(self):
        ' Returns true if the sale is considered complete, false otherwise '
        if self.invoice_method == 'shipment':
            return all(l.move_done for l in self.lines)
        return True
