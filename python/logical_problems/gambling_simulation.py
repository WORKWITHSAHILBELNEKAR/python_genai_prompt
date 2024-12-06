import random

def gambler_simulation(stake, goal, num_trials):
    wins = 0
    bets = 0

    for _ in range(num_trials):
        cash = stake
        while cash > 0 and cash < goal:
            bets += 1
            cash += 1 if random.random() < 0.5 else -1
        if cash == goal:
            wins += 1

    win_percentage = (wins / num_trials) * 100
    print(f"Wins: {wins}, Bets: {bets}, Win Percentage: {win_percentage:.2f}%")
    return wins, win_percentage


gambler_simulation(10, 20, 100)
