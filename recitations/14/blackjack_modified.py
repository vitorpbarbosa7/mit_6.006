

# could create a more complete memoization here
x = {}
cards = [2,3,8,3,6,7,7,1,3,10,8,9,6,7,8,5,4,3,9,3,6,2,8,6]
def black(i):
    print('\nStack frame creaated')
    print(f'cards: {cards[i:]}')

    # Base case
    # no more cards to be run:
    if len(cards[i:]) < 4:
        return 0
    
    # subproblems
    dealer = cards[i] + cards[i+1]
    player_no_hit = cards[i+2] + cards[i+3]
    if len(cards[i:])>4:
        player_hit = cards[i+2] + cards[i+3] + cards[i+4]
    else:
        player_hit = 0

    # relation

    x[i] = max(
        get_winner(dealer, player_no_hit) + black(i+4),
        get_winner(dealer, player_hit) + black(i+5)
    )

    return x[i]
    
def get_winner(d, p):
    if p > d or (p > d and p <= 21):
        return 1
    else:
        return 0
    

result = black(0)
print(result)
print(x)
print(max(x))