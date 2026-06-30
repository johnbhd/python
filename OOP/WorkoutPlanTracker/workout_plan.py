import json
import os


class WorkoutPlan:
    def __init__(self, day, workout_name, exercises=None, completed=False):
        self.day = day
        self.workout_name = workout_name
        self.exercises = exercises if exercises is not None else []
        self.completed = completed

    def show_info(self):
        status = "Done" if self.completed else "Not Done"

        print(f"Day: {self.day}")
        print(f"Workout: {self.workout_name}")
        print(f"Status: {status}")
        print("Exercises:")

        if not self.exercises:
            print("- No exercise yet")
        else:
            for exercise in self.exercises:
                print(f"- {exercise}")


class WorkoutTracker:
    def __init__(self, file_name="workout_plans.json"):
        self.file_name = file_name
        self.workouts = []

    def show_menu(self):
        print("\nWorkout Plan Tracker")
        print("1. View workouts")
        print("2. Add workout")
        print("3. Exit")

    def add_workout(self):
        day = input("Enter workout day: ")
        workout_name = input("Enter workout name: ")

        exercises = []

        while True:
            exercise = input("Enter exercise or type done: ")

            if exercise.lower() == "done":
                break

            exercises.append(exercise)

        workout = WorkoutPlan(day, workout_name, exercises)
        self.workouts.append(workout)

        print("Workout added successfully.")

    def view_workouts(self):
        if not self.workouts:
            print("No workouts yet.")
            return

        for index, workout in enumerate(self.workouts, start=1):
            print(f"\nWorkout #{index}")
            workout.show_info()

    def run(self):
        while True:
            self.show_menu()

            choice = input("Choose option: ")

            if choice == "1":
                self.view_workouts()

            elif choice == "2":
                self.add_workout()

            elif choice == "3":
                print("Exit...")
                break

            else:
                print("Invalid choice...")


def initialize_project():
    file_name = "workout_plans.json"

    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump([], file, indent=4)

        print("Project initialized.")
        print("workout_plans.json created.")
    else:
        print("Project already initialized.")


def main():
    initialize_project()

    tracker = WorkoutTracker()
    tracker.run()


main()