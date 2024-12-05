from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List


@dataclass
class Timeslot:
    start_time: datetime
    end_time: datetime


def generate_timeslots_from_date_range(start_time: datetime, end_time: datetime, interval_time: int = 30) -> List[Timeslot]:
    interval = timedelta(minutes=interval_time)
    time_slots: List[Timeslot] = []
    current_time = start_time
    while current_time < end_time:
        time_slots.append(Timeslot(current_time, current_time + interval))
        current_time += interval
    return time_slots
