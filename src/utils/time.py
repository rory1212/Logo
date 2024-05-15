from datetime import datetime
from tzlocal import get_localzone


def get_current_timestamp() -> str:
    local_timezone = get_localzone()
    current_time = datetime.now(local_timezone)
    return current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
