budget = float(input())
price_for_1_kg_flour = float(input())

budget_remaining = budget
price_1pack_of_eggs = price_for_1_kg_flour * 0.75
price_1kg_milk = (price_for_1_kg_flour * 0.25) + price_for_1_kg_flour
price_for_250ml_milk = price_1kg_milk / 4
bred_count = 0
colored_eggs_count = 0
while budget_remaining >= 0:
    bred_count += 1
    budget_remaining -= price_for_1_kg_flour + price_1pack_of_eggs + price_for_250ml_milk
    colored_eggs_count += 3
    if bred_count % 3 == 0 and budget_remaining >= 0:
        colored_eggs_count -= (bred_count - 2)
else:
    bred_count -= 1
    budget_remaining += price_for_1_kg_flour + price_1pack_of_eggs + price_for_250ml_milk
    colored_eggs_count -= 3


print(f"You made {bred_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget_remaining:.2f}BGN left.")

