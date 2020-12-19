def normalize(mins):
    ### Преобразует входные минуты во время, отбрасывая сутки, если необходимо
    if mins > 1440:
        mins -= 1440
    return(str(mins//60) + ":" + str(mins%60))

def asleep(hours, minutes):
    ### Returns the wake-up time after specified several sleep cycles.
    # tim -- Time in Minutes
    tim = hours * 60 + minutes
    b = []
    b.append(normalize(tim + 90 * 3))
    b.append(normalize(tim + 90 * 4))
    b.append(normalize(tim + 90 * 5))
    b.append(normalize(tim + 90 * 6))
    return(b)


def wakeup(hours, minutes):
    ### Returns the wake-up time after specified several sleep cycles.
    # tim -- Time in Minutes
    tim = hours * 60 + minutes
    b = []
    b.append(normalize(tim - 90 * 3))
    b.append(normalize(tim - 90 * 4))
    b.append(normalize(tim - 90 * 5))
    b.append(normalize(tim - 90 * 6))
    return(b)

