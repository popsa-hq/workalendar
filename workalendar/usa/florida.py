# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import FRI
from .core import UnitedStates


class Florida(UnitedStates):
    """Florida"""
    def get_variable_days(self, year):
        days = super(Florida, self).get_variable_days(year)
        days.append(
            (Florida.get_nth_weekday_in_month(year, 11, FRI, 4),
             "Friday after Thanksgiving")
        )
        return days
