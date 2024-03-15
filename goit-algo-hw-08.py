def minimize_costs(cables):
    connections = [(i, j, cables[i] + cables[j]) for i in range(len(cables)) for j in range(i+1, len(cables))]
    connections.sort(key=lambda x: x[2])  # сортуємо за зростанням суми довжин

    total_cost = 0
    while len(connections) > 0:
        # беремо найменший з'єднувач
        i, j, cost = connections.pop(0)
        total_cost += cost

        # об'єднуємо кабелі та додаємо новий кабель до списку
        cables.append(cables[i] + cables[j])

    return total_cost

cables = [2, 3, 4, 6, 8]
min_cost = minimize_costs(cables)
print("Мінімальні витрати:", min_cost)
