def convert(hour, minute, period):
    # Adjust hour for PM times
    if period == "pm" and hour != 12:
        hour += 12
    else:
        # Adjust hour for AM times at 12:00 AM
        if period == "am" and hour == 12:
            hour = 0
    
    # Format the time in 24-hour format
    hour_str = f"{hour:02}"
    minute_str = f"{minute:02}"
    
    print  (hour_str + minute_str)
convert(4,30,"pm")