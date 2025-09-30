from datetime import datetime

import pytz

def get_current_time(zone):
    """Get the current time in a specific time zone."""
    timezone = pytz.timezone(zone)
    current_time = datetime.now(timezone)
    return current_time

def convert_time_zone(from_zone, to_zone, time):
    """Convert a time from one time zone to another."""
    from_timezone = pytz.timezone(from_zone)
    to_timezone = pytz.timezone(to_zone)
    time = from_timezone.localize(time)
    converted_time = time.astimezone(to_timezone)
    return converted_time

def main():
     
    # Get the current time in different time zones
    print("Current time in New York:", get_current_time('America/New_York'))
    print("Current time in London:", get_current_time('Europe/London'))
    print("Current time in Tokyo:", get_current_time('Asia/Tokyo'))

    # Convert a time from one time zone to another
    from_zone = 'America/New_York'
    to_zone = 'Europe/London'
    time = datetime(2024, 12, 21, 14, 30, 0)
    converted_time = convert_time_zone(from_zone, to_zone, time)
    print(f"Converted time from {from_zone} to {to_zone}: {converted_time}")

if __name__ == "__main__":
    main()
