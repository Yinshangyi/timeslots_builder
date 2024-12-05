from datetime import datetime
from typing import List

import pytest

from timeslots import Timeslot, generate_timeslots_from_date_range

date = datetime(2024, 1, 1)


@pytest.mark.parametrize("start_date, end_date, expected_time_slots", [
    (
            date.replace(hour=9, minute=0),
            date.replace(hour=10, minute=0),
            [
                Timeslot(date.replace(hour=9, minute=0), date.replace(hour=9, minute=30)),
                Timeslot(date.replace(hour=9, minute=30), date.replace(hour=10, minute=0))
            ]
    ),
    (
            date.replace(hour=9, minute=0),
            date.replace(hour=12, minute=0),
            [
                Timeslot(date.replace(hour=9, minute=0), date.replace(hour=9, minute=30)),
                Timeslot(date.replace(hour=9, minute=30), date.replace(hour=10, minute=0)),
                Timeslot(date.replace(hour=10, minute=0), date.replace(hour=10, minute=30)),
                Timeslot(date.replace(hour=10, minute=30), date.replace(hour=11, minute=0)),
                Timeslot(date.replace(hour=11, minute=0), date.replace(hour=11, minute=30)),
                Timeslot(date.replace(hour=11, minute=30), date.replace(hour=12, minute=0))
            ]
    )
])
def test_should_break_the_time_range_into_30_mins_timeslots(start_date: datetime, end_date: datetime,
                                                            expected_time_slots: List[Timeslot]):
    time_slots = generate_timeslots_from_date_range(start_date, end_date)
    assert time_slots == expected_time_slots
