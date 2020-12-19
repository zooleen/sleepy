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

