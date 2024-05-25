import time

def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    chosen_items = []
    
    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            chosen_items.append(item)
    
    return total_calories, chosen_items

def dynamic_programming(items, budget):
    # Ініціалізація таблиці DP
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    item_list = list(items.items())
    
    for i in range(1, len(item_list) + 1):
        item_name, item_info = item_list[i - 1]
        cost = item_info['cost']
        calories = item_info['calories']
        
        for b in range(1, budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]
    
    total_calories = dp[len(item_list)][budget]
    chosen_items = []
    b = budget
    
    for i in range(len(item_list), 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item_name, item_info = item_list[i - 1]
            chosen_items.append(item_name)
            b -= item_info['cost']
    
    return total_calories, chosen_items

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Заданий бюджет
budget = 100

# Виконання жадібного алгоритму
start_time = time.time()
greedy_calories, greedy_items = greedy_algorithm(items, budget)
greedy_time = time.time() - start_time
print("Жадібний алгоритм:")
print(f"Загальна калорійність: {greedy_calories}")
print(f"Обрані страви: {greedy_items}")
print(f"Час виконання: {greedy_time:.6f} секунд")

# Виконання алгоритму динамічного програмування
start_time = time.time()
dp_calories, dp_items = dynamic_programming(items, budget)
dp_time = time.time() - start_time
print("\nАлгоритм динамічного програмування:")
print(f"Загальна калорійність: {dp_calories}")
print(f"Обрані страви: {dp_items}")
print(f"Час виконання: {dp_time:.6f} секунд")

# Висновки
print("\nВисновки:")
if greedy_calories > dp_calories:
    print("Жадібний алгоритм дав кращий результат.")
elif greedy_calories < dp_calories:
    print("Алгоритм динамічного програмування дав кращий результат.")
else:
    print("Обидва алгоритми дали однаковий результат.")

print("\nПорівняння часу виконання:")
print(f"Час виконання жадібного алгоритму: {greedy_time:.6f} секунд")
print(f"Час виконання алгоритму динамічного програмування: {dp_time:.6f} секунд")
if greedy_time < dp_time:
    print("Жадібний алгоритм виконується швидше.")
else:
    print("Алгоритм динамічного програмування виконується швидше.")
