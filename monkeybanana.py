def monkey_banana_problem(monkey_pos, box_pos, banana_pos):
    steps = []

    if monkey_pos == "floor" and box_pos != banana_pos:
        steps.append("Monkey walks to box")
        steps.append("Monkey pushes box under bananas")
        steps.append("Monkey climbs box")
        steps.append("Monkey grabs bananas")
    elif monkey_pos == "floor" and box_pos == banana_pos:
        steps.append("Monkey climbs box")
        steps.append("Monkey grabs bananas")
    else:
        steps.append("Monkey can't reach bananas")

    return steps

#  Take input from user
monkey = input("Where is the monkey? (floor/table): ").lower()
box = input("Where is the box? (corner/under_bananas): ").lower()
banana = "ceiling"  # Always at ceiling

result = monkey_banana_problem(monkey, box, banana)

print("\nSteps:")
for step in result:
    print(step)
