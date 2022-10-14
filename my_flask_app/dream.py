def normalize(mins):
    """Convert input minutes to time. Minus one day, if needed"""
    if mins > 1440:
        mins -= 1440
    if mins <= 0:
        mins += 1440
    return((str(mins//60) if len(str(mins//60)) == 2 else "0" + str(mins//60)) + ":" + (str(mins%60) if len(str(mins%60)) == 2 else "0" + str(mins%60)))

def asleep(hours, minutes):
    """Returns the wake-up time after specified several sleep cycles."""
    # tim -- Time in Minutes
    tim = hours * 60 + minutes
    b = []
    for i in range(3, 7):
        b.append(normalize(tim + 90 * i))

    return(b)


def wakeup(hours, minutes):
    """Returns the wake-up time after specified several sleep cycles."""
    # tim -- Time in Minutes
    tim = hours * 60 + minutes
    b = []
    b.append(normalize(tim - 90 * 3))
    b.append(normalize(tim - 90 * 4))
    b.append(normalize(tim - 90 * 5))
    b.append(normalize(tim - 90 * 6))
    return(b)

