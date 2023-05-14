'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_PRICE = 60000
MAX_ITEM_QUANTITY = 50
MAX_ORDER_VALUE = 3e6

def validorder(order: Order):
    net = 0
    
    for item in order.items:
        if item.type == 'payment':
            payment_compliant = item.amount > -1 * MAX_ITEM_PRICE and item.amount < MAX_ITEM_PRICE
            if payment_compliant: 
                net += item.amount
            else:
                print(f"Attempting a payment higher than {MAX_ITEM_PRICE} is not allowed.")
        elif item.type == 'product':
            item_compliant = item.quantity > 0 and item.quantity <= MAX_ITEM_QUANTITY and item.amount > 0 and item.amount <= MAX_ITEM_PRICE
            if item_compliant:
                net -= item.amount * item.quantity
                if net > MAX_ORDER_VALUE or net < -1*MAX_ORDER_VALUE:
                    return("Total amount exceeded")
        else:
            return(f"Invalid item type: {item.type}")
    
    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
