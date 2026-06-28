import json 
import os

class WorkoutPlan:    
    def __init__(self, day, workout_name, exercise, completed):
        self.day = day
        self.workout_name = workout_name
        self.exercise = exercise
        self.completed = completed
        
        
    
        
class WorkoutTracker:
    def __init__(self, file_name="workout_plans.json"):
            self.file_name = file_name
            self.workout = []
            
    def show_menu(self):
        print("\nWorkout Plan Tracker")
        print("1. View workouts")
        print("2. Add workout")
        print("3. Exit")

    def run(self):
        while True:
            self.show_menu()
            
            choice = input("Choose opitons: ")
            
            if (choice == "1"):
                print("view...")
                
            elif (choice == "2"):
                print("Add...")
             
            elif (choice == "3"):
                print("Exit...")
                break
            else:
                print("Invalid choice...")
                
                           
        
def main():
    tracker = WorkoutTracker()
    tracker.run()
    
    
main()