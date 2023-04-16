from calendar import calendar
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, EasterMonday, Easter
from pandas.tseries.offsets import Day, CustomBusinessDay, CustomBusinessHour


class PLHolidayCalendar(AbstractHolidayCalendar):
    """
    Custom Holiday calendar for Poland based on
    https://en.wikipedia.org/wiki/Public_holidays_in_Poland
    """
    rules = [
        Holiday('New Years Day', month=1, day=1),
        Holiday('Epiphany', month=1, day=6),
        Holiday('Easter', month=1, day=1, offset=[Easter()]),
        EasterMonday,
        Holiday('May Day', month=5, day=1),
        Holiday('Constitution Day', month=5, day=3),
        Holiday('Pentecost Sunday', month=1, day=1, offset=[Easter(), Day(49)]),
        Holiday('Corpus Christi', month=1, day=1, offset=[Easter(), Day(60)]),
        Holiday('Assumption of the Blessed Virgin Mary', month=8, day=15),
        Holiday('All Saints Day', month=11, day=1),
        Holiday('Independence Day', month=11, day=11),
        Holiday('Christmas Day', month=12, day=25),
        Holiday('Second Day of Christmastide', month=12, day=26),
    ]

pl_bd = CustomBusinessDay(calendar=PLHolidayCalendar())
