import random
import matplotlib.pyplot as plt


def roll_dice(num_rolls):
    sums = [0] * 13

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sums[roll_sum] += 1

    return sums


def calculate_probabilities(sums, num_rolls):
    probabilities = [count / num_rolls for count in sums]
    return probabilities


def plot_probabilities(probabilities):
    sums = range(2, 13)
    plt.bar(sums, probabilities[2:13], color='#1296F0', alpha=0.7)
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум чисел (Метод Монте-Карло)')
    plt.xticks(sums)
    plt.show()


num_rolls = 100000
sums = roll_dice(num_rolls)
probabilities = calculate_probabilities(sums, num_rolls)
plot_probabilities(probabilities)
