items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    items_ratio = [(item, info['calories'] / info['cost']) for item, info in items.items()]
    items_ratio.sort(key=lambda x: x[1], reverse=True)

    total_calories = 0
    selected_items = {}

    for item, ratio in items_ratio:
        cost = items[item]['cost']
        calories = items[item]['calories']
        if budget >= cost:
            budget -= cost
            total_calories += calories
            selected_items[item] = {"cost": cost, "calories": calories}

    return selected_items, total_calories


budget = 100
selected_items, total_calories = greedy_algorithm(items, budget)
print(f"Вибрані страви: {selected_items}")
print(f"Загальна калорійність: {total_calories}")


def dynamic_programming(items, budget):
    n = len(items)
    items_list = list(items.items())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    selected_items = [[[] for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, info = items_list[i - 1]
        cost = info['cost']
        calories = info['calories']
        for w in range(budget + 1):
            if cost <= w:
                if dp[i - 1][w] < dp[i - 1][w - cost] + calories:
                    dp[i][w] = dp[i - 1][w - cost] + calories
                    selected_items[i][w] = selected_items[i - 1][w - cost] + [item]
                else:
                    dp[i][w] = dp[i - 1][w]
                    selected_items[i][w] = selected_items[i - 1][w]
            else:
                dp[i][w] = dp[i - 1][w]
                selected_items[i][w] = selected_items[i - 1][w]

    total_calories = dp[n][budget]
    selected_items_names = selected_items[n][budget]
    result_items = {item: items[item] for item in selected_items_names}

    return result_items, total_calories


budget = 100
selected_items, total_calories = dynamic_programming(items, budget)
print(f"Вибрані страви: {selected_items}")
print(f"Загальна калорійність: {total_calories}")
