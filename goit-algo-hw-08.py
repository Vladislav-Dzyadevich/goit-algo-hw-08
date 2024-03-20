import heapq

def minimize_costs(cables):
    heapq.heapify(cables)  # перетворюємо список кабелів у min-кучу

    total_cost = 0
    while len(cables) > 1:
        # вибираємо два найменших кабелі та їх вартість
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)
        cost = shortest1 + shortest2
        total_cost += cost

        # додаємо новий кабель до min-кучі
        heapq.heappush(cables, cost)

    return total_cost

cables = [1,1,1]
min_cost = minimize_costs(cables)
print("Мінімальні витрати:", min_cost)
