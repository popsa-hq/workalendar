# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from workalendar.core import FRI
from .core import UnitedStates


class Nevada(UnitedStates):
    """Nevada"""
    include_thanksgiving_friday = True

    def get_variable_days(self, year):
        days = super(Nevada, self).get_variable_days(year)
        days.extend([
            (self.get_last_weekday_in_month(year, 10, FRI), "Nevada Day")
        ])
        return days
