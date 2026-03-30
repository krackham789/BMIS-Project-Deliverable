import random

# ---------------------------
# Recipe Database
# ---------------------------
def load_recipes():
    recipes = [
        {"name": "Grilled Chicken Bowl", "protein": 35, "fiber": 5, "calories": 450, "type": "lunch"},
        {"name": "Oatmeal with Berries", "protein": 10, "fiber": 8, "calories": 300, "type": "breakfast"},
        {"name": "Egg Scramble", "protein": 20, "fiber": 2, "calories": 250, "type": "breakfast"},
        {"name": "Turkey Sandwich", "protein": 25, "fiber": 4, "calories": 400, "type": "lunch"},
        {"name": "Salmon with Rice", "protein": 30, "fiber": 3, "calories": 500, "type": "dinner"},
        {"name": "Chicken Stir Fry", "protein": 28, "fiber": 6, "calories": 480, "type": "dinner"},
        {"name": "Greek Yogurt Bowl", "protein": 18, "fiber": 2, "calories": 200, "type": "breakfast"},
        {"name": "Veggie Wrap", "protein": 12, "fiber": 7, "calories": 350, "type": "lunch"},
        {"name": "Steak and Potatoes", "protein": 40, "fiber": 4, "calories": 600, "type": "dinner"},
        {"name": "Protein Smoothie", "protein": 22, "fiber": 3, "calories": 280, "type": "breakfast"},
    ]
    return recipes


# ---------------------------
# Display Menu
# ---------------------------
def display_menu():
    print("\n=== SmartMeal Planner ===")
    print("1. Enter Nutrition Goals")
    print("2. Generate Weekly Meal Plan")
    print("3. View Meal Plan")
    print("4. Quit")


# ---------------------------
# Get User Goals
# ---------------------------
def get_user_goals():
    protein = int(input("Enter daily protein goal (grams): "))
    fiber = int(input("Enter daily fiber goal (grams): "))
    calories = int(input("Enter daily calorie goal: "))
    return protein, fiber, calories


# ---------------------------
# Filter Recipes by Type
# ---------------------------
def get_recipes_by_type(recipes, meal_type):
    return [r for r in recipes if r["type"] == meal_type]


# ---------------------------
# Generate Meal Plan
# ---------------------------
def generate_meal_plan(recipes, protein_goal, fiber_goal, calorie_goal):
    meal_plan = []

    breakfasts = get_recipes_by_type(recipes, "breakfast")
    lunches = get_recipes_by_type(recipes, "lunch")
    dinners = get_recipes_by_type(recipes, "dinner")

    for day in range(7):
        day_plan = {
            "breakfast": random.choice(breakfasts),
            "lunch": random.choice(lunches),
            "dinner": random.choice(dinners),
        }
        meal_plan.append(day_plan)

    return meal_plan


# ---------------------------
# Calculate Daily Totals
# ---------------------------
def calculate_totals(day_plan):
    total_protein = 0
    total_fiber = 0
    total_calories = 0

    for meal in day_plan.values():
        total_protein += meal["protein"]
        total_fiber += meal["fiber"]
        total_calories += meal["calories"]

    return total_protein, total_fiber, total_calories


# ---------------------------
# Display Meal Plan
# ---------------------------
def display_meal_plan(meal_plan):
    if not meal_plan:
        print("No meal plan generated yet.")
        return

    for i, day in enumerate(meal_plan):
        print(f"\nDay {i+1}:")
        for meal_type, meal in day.items():
            print(f"{meal_type.capitalize()}: {meal['name']}")

        protein, fiber, calories = calculate_totals(day)
        print(f"Totals -> Protein: {protein}g | Fiber: {fiber}g | Calories: {calories}")


def main():
    recipes = load_recipes()
    meal_plan = []
    protein_goal = fiber_goal = calorie_goal = 0

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            protein_goal, fiber_goal, calorie_goal = get_user_goals()

        elif choice == "2":
            if protein_goal == 0:
                print("Please enter your goals first.")
            else:
                meal_plan = generate_meal_plan(
                    recipes, protein_goal, fiber_goal, calorie_goal
                )
                print("Meal plan generated!")

        elif choice == "3":
            display_meal_plan(meal_plan)

        elif choice == "4":
            print("Exiting SmartMeal Planner. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()