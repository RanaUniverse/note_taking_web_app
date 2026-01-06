"""
HEre i will keep some needy important things
"""

import datetime

from uuid import uuid4


def generate_uuid() -> str:
    return str(uuid4().hex)



GMT_TIMEZONE = datetime.timezone(datetime.timedelta(hours=0, minutes=0))
IST_TIMEZONE = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
