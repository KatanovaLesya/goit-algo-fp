import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(num_simulations):
    sum_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_simulations):
        dice_sum = roll_dice() + roll_dice()
        sum_counts[dice_sum] += 1
    
    probabilities = {s: count / num_simulations for s, count in sum_counts.items()}
    
    return probabilities

def plot_probabilities(mc_probabilities, analytical_probabilities):
    sums = list(mc_probabilities.keys())
    mc_probs = list(mc_probabilities.values())
    analytical_probs = [analytical_probabilities[s] for s in sums]
    
    width = 0.35  # Ширина стовпців
    fig, ax = plt.subplots(figsize=(10, 6))
    mc_bar = ax.bar([s - width/2 for s in sums], mc_probs, width, label='Монте-Карло', color='skyblue')
    analytical_bar = ax.bar([s + width/2 for s in sums], analytical_probs, width, label='Аналітичні', color='orange')
    
    ax.set_xlabel('Сума')
    ax.set_ylabel('Ймовірність')
    ax.set_title('Ймовірності сум при киданні двох кубиків')
    ax.set_xticks(sums)
    ax.legend()
    
    plt.show()

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Параметри симуляції
num_simulations = 1000000

# Проведення симуляції
mc_probabilities = monte_carlo_simulation(num_simulations)

# Виведення результатів
print("Ймовірності сум при киданні двох кубиків (Метод Монте-Карло):")
for s in sorted(mc_probabilities):
    print(f"Сума: {s}, Ймовірність: {mc_probabilities[s] * 100:.2f}%")

print("\nАналітичні ймовірності сум при киданні двох кубиків:")
for s in sorted(analytical_probabilities):
    print(f"Сума: {s}, Ймовірність: {analytical_probabilities[s] * 100:.2f}%")

# Побудова графіка
plot_probabilities(mc_probabilities, analytical_probabilities)
