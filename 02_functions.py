# Question - 1
def round_to_two_places(num):
    """Return the given number rounded to two decimal places."""
    return round(num,2)

#Question - 2 : basic cell run

# Question - 3
def to_smash(total_candies, friends = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends."""
    return total_candies % friends