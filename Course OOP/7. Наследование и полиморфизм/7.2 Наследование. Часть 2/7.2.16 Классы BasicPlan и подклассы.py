class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = "8.99$"


class SilverPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = "12.99$"


class GoldPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = "15.99$"
