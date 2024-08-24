#Question - 1
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False

#Question - 2
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise."""
    return [ele > thresh for ele in L]

#Question - 3
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

#Question - 4
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run."""
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    avg_payout = sum(payouts) / n_runs
    return avg_payout