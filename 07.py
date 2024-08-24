#Question - 1
def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests: add a title, make the y-axis
    start at 0, label the y-axis. (And, if you're feeling ambitious, format the tick marks
    as dollar amounts using the "$" symbol.)
    """
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(bottom=0)
    graph.set_ylabel("Balance")
    ticks = graph.get_yticks()
    new_labels = ['${}'.format(int(amt)) for amt in ticks]
    graph.set_yticklabels(new_labels)

#Question - 3
def hand_total(hand):
    """Helper function to calculate the total points of a blackjack hand.
    """
    total = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            total += int(card)
    total += aces
    while total + 10 <= 21 and aces > 0:
        total += 10
        aces -= 1
    return total
def blackjack_hand_greater_than(hand_1, hand_2):
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)