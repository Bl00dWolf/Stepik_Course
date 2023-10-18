from enum import Flag, auto


class OrderStatus(Flag):
    ORDER_PLACED, PAYMENT_RECEIVED, SHIPPING_COMPLETE = (auto() for el in range(3))

