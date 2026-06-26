def FCFS():    
    # User input
    def Process(p):
        numbers = []    
        print("\nEnter Process")   
        for i in range(1, p+1):   
            arrvl = int(input(f"Arrival Time P{i}: "))
            burst = int(input(f"Burst Time P{i}: "))
            print("")
            numbers.append((f"P{i}", arrvl, burst))
              
        return sorted(numbers, key=lambda x: x[1])  
    
    # Gantt Chart
    def Chart(pronum, completion):
        print("\nGantt Chart:")
        gantt = " |"
        timeline = " 0"

        prev_completion = 0
        for i in range(len(pronum)):
            label = pronum[i][0]
            start_time = prev_completion if prev_completion > pronum[i][1] else pronum[i][1]
            end_time = completion[i]
            prev_completion = end_time

            gantt += f" {label} | "
            timeline += f" {' ' * (len(label) + 1)}{end_time} "

        print(gantt)
        print(timeline)

    # Display
    def Display(pronum):
        print("\n Process\tArrival Time\tBurst Time")
    
        waiting = []
        completion = []
        turnaround = []
        ctime = 0
        total_tat = 0
        total_wt = 0
        
        for label, arrvl, burst in pronum:
            ctime = max(ctime, arrvl) + burst
            completion.append(ctime)
            
            tat = ctime - arrvl
            turnaround.append(tat)
            total_tat += tat
            
            wtime = tat - burst
            waiting.append(wtime)
            total_wt += wtime
            
            print(f" {label}\t\t{arrvl}\t\t{burst}")
            
        print(f"\nCompletion Time\tTurnaround Time\tWaiting Time")
        
        for i in range(len(pronum)):    
            print(f" {completion[i]}\t\t{turnaround[i]}\t\t{waiting[i]}")
        
        atat = total_tat / len(pronum)
        awt = total_wt / len(pronum)
        
        print(f"\n Average Turnaround Time: {atat:.2f}\n Average Waiting Time: {awt:.2f}")
        
        return completion  

    # Start execution
    print("\nFirst Come, First Served (FCFS)")      
    while True:
        try:   
            numpt = int(input("How Many Processes: ")) 
            pronum = Process(numpt)
            completion_times = Display(pronum)
            Chart(pronum, completion_times)
            break
        except ValueError:
            print("Invalid Input, try again.\n")

def SRTF():
    # User input
    def Process(p):
        numbers = []    
        arrival_times = []
        burst_times = []
        print("\nEnter Process")   
        for i in range(1, p + 1):   
            arrvl = int(input(f"Arrival Time P{i}: "))
            burst = int(input(f"Burst Time P{i}: "))
            print("")
            arrival_times.append(arrvl)
            burst_times.append(burst)
            numbers.append(f"P{i}")
        return numbers, arrival_times, burst_times  
    
    # Gantt Chart
    def Chart(pronum, completion):
        print("\nGantt Chart:")
        gantt = " |"
        timeline = " 0"

        prev_completion = 0
        for i in range(len(pronum)):
            label = pronum[i]
            start_time = prev_completion if prev_completion > arrival_times[i] else arrival_times[i]
            end_time = completion[i]
            prev_completion = end_time

            gantt += f" {label} | "
            timeline += f" {' ' * (len(label) + 1)}{end_time} "

        print(gantt)
        print(timeline)

   
    def CalculateTimes(pronum, arrival_times, burst_times):
        current_time = 0
        completed = 0
        total_tat = 0
        total_wt = 0
        remaining = burst_times[:]  # Remaining burst times
        completion = []
        turnaround = []
        waiting = []

        while completed < len(pronum):
            idx = -1
            for i in range(len(pronum)):
                if arrival_times[i] <= current_time and remaining[i] > 0 and (idx == -1 or remaining[i] < remaining[idx]):
                    idx = i
            if idx != -1:
                remaining[idx] -= 1
                current_time += 1
                if remaining[idx] == 0:
                    completion_time = current_time
                    turnaround_time = completion_time - arrival_times[idx]
                    waiting_time = turnaround_time - burst_times[idx]
                    completion.append(completion_time)
                    turnaround.append(turnaround_time)
                    waiting.append(waiting_time)
                    total_tat += turnaround_time
                    total_wt += waiting_time
                    completed += 1
            else:
                current_time += 1

        return completion, turnaround, waiting, total_tat, total_wt

    # Display results
    def Display(pronum, arrival_times, burst_times, completion, turnaround, waiting, total_tat, total_wt):
        print("\n Process\tArrival Time\tBurst Time")
        for i in range(len(pronum)):
            print(f" {pronum[i]}\t\t{arrival_times[i]}\t\t{burst_times[i]}")
        
        print(f"\nCompletion Time\tTurnaround Time\tWaiting Time")
        for i in range(len(pronum)):    
            print(f" {completion[i]}\t\t{turnaround[i]}\t\t{waiting[i]}")
        
        atat = total_tat / len(pronum)
        awt = total_wt / len(pronum)
        
        print(f"\nAverage Turnaround Time: {atat:.2f}\nAverage Waiting Time: {awt:.2f}")
    
    # Start execution
    print("\nShortest Remaining Time First (SRTF)")      
    while True:
        try:   
            numpt = int(input("How Many Processes: ")) 
            pronum, arrival_times, burst_times = Process(numpt)
            completion, turnaround, waiting, total_tat, total_wt = CalculateTimes(pronum, arrival_times, burst_times)
            Display(pronum, arrival_times, burst_times, completion, turnaround, waiting, total_tat, total_wt)
            Chart(pronum, completion)
            break
        except ValueError:
            print("Invalid Input, try again.\n")

def SJF():    
    # User input
    def Process(p):
        numbers = []    
        print("\nEnter Process")   
        for i in range(1, p+1):   
            arrvl = int(input(f"Arrival Time P{i}: "))
            burst = int(input(f"Burst Time P{i}: "))
            print("")
            numbers.append((f"P{i}", arrvl, burst))
              
        return sorted(numbers, key=lambda x: (x[1], x[2]))  
    # Gantt Chart
    def Chart(pronum, completion):
        print("\nGantt Chart:")
        gantt = " |"
        timeline = " 0"

        prev_completion = 0
        for i in range(len(pronum)):
            label = pronum[i][0]
            start_time = prev_completion if prev_completion > pronum[i][1] else pronum[i][1]
            end_time = completion[i]
            prev_completion = end_time

            gantt += f" {label} |"
            timeline += f" {' ' * (len(label) + 1)}{end_time} "

        print(gantt)
        print(timeline)

    # Display
    def Display(pronum):
        print("\n Process\tArrival Time\tBurst Time")
    
        waiting = []
        completion = []
        turnaround = []
        ctime = 0
        total_tat = 0
        total_wt = 0
        
        for label, arrvl, burst in pronum:
            ctime = max(ctime, arrvl) + burst
            completion.append(ctime)
            
            tat = ctime - arrvl
            turnaround.append(tat)
            total_tat += tat
            
            wtime = tat - burst
            waiting.append(wtime)
            total_wt += wtime
            
            print(f" {label}\t\t{arrvl}\t\t{burst}")
            
        print(f"\nCompletion Time\tTurnaround Time\tWaiting Time")
        
        for i in range(len(pronum)):    
            print(f" {completion[i]}\t\t{turnaround[i]}\t\t{waiting[i]}")
        
        atat = total_tat / len(pronum)
        awt = total_wt / len(pronum)
        
        print(f"\n Average Turnaround Time: {atat:.2f}\n Average Waiting Time: {awt:.2f}")
        
        return completion 

    print("\nShortest Job First (SJF)")      
    while True:
        try:   
            numpt = int(input("How Many Processes: ")) 
            pronum = Process(numpt)
            completion_times = Display(pronum)
            Chart(pronum, completion_times)
            break
        except ValueError:
            print("Invalid Input, try again.\n")

     

def RR():
    # User input
    def Process(p):
        numbers = []    
        arrival_times = []
        burst_times = []
        for i in range(1, p + 1):   
            arrvl = int(input(f"Arrival Time P{i}: "))
            burst = int(input(f"Burst Time P{i}: "))
            print("")
            arrival_times.append(arrvl)
            burst_times.append(burst)
            numbers.append(f"P{i}")
        return numbers, arrival_times, burst_times  

    # Gantt Chart
    def Chart(pronum, completion):
        print("\nGantt Chart:")
        gantt = " |"
        timeline = " 0"

        prev_completion = 0
        for i in range(len(pronum)):
            label = pronum[i]
            start_time = prev_completion if prev_completion > arrival_times[i] else arrival_times[i]
            end_time = completion[i]
            prev_completion = end_time

            gantt += f" {label} | "
            timeline += f" {' ' * (len(label) + 1)}{end_time} "

        print(gantt)
        print(timeline)


    def CalculateTimes(pronum, arrival_times, burst_times, quantum):
        current_time = 0
        remaining_burst = burst_times[:]  
        completion = [-1] * len(pronum)
        turnaround = [-1] * len(pronum)
        waiting = [-1] * len(pronum)
        queue = []
        total_tat = 0
        total_wt = 0

        while any(r > 0 for r in remaining_burst):  
            for i in range(len(pronum)):
                if arrival_times[i] <= current_time and remaining_burst[i] > 0:
                    queue.append(i)

            if queue:
                idx = queue.pop(0)
                time_slice = min(remaining_burst[idx], quantum)
                current_time += time_slice
                remaining_burst[idx] -= time_slice

                if remaining_burst[idx] == 0 and completion[idx] == -1:
                    completion[idx] = current_time
                    turnaround[idx] = completion[idx] - arrival_times[idx]
                    waiting[idx] = turnaround[idx] - burst_times[idx]

                total_tat += turnaround[idx]
                total_wt += waiting[idx]

            else:
                current_time += 1  # Increment time if queue is empty

        return completion, turnaround, waiting, total_tat, total_wt

    # Display results
    def Display(pronum, arrival_times, burst_times, completion, turnaround, waiting, total_tat, total_wt):
        print("\n Process\tArrival Time\tBurst Time")
        for i in range(len(pronum)):
            print(f" {pronum[i]}\t\t{arrival_times[i]}\t\t{burst_times[i]}")
        
        print(f"\nCompletion Time\tTurnaround Time\tWaiting Time")
        for i in range(len(pronum)):    
            print(f" {completion[i]}\t\t{turnaround[i]}\t\t{waiting[i]}")
        
        atat = total_tat / len(pronum)
        awt = total_wt / len(pronum)
        
        print(f"\nAverage Turnaround Time: {atat:.2f}\nAverage Waiting Time: {awt:.2f}")
    
    # Start execution
    print("\nRound Robin Scheduling (RR)")      
    while True:
        try:   
            numpt = int(input("How Many Processes: ")) 
            quantum = int(input("Enter Time Quantum: "))
            pronum, arrival_times, burst_times = Process(numpt)
            completion, turnaround, waiting, total_tat, total_wt = CalculateTimes(pronum, arrival_times, burst_times, quantum)
            Display(pronum, arrival_times, burst_times, completion, turnaround, waiting, total_tat, total_wt)
            Chart(pronum, completion)
            break
        except ValueError:
            print("Invalid Input, try again.\n")

                       
def Choices(choice):
    match choice:
        case 1: 
            FCFS()
        case 2: 
            SJF()
        case 3: 
            SRTF()
        case 4: 
            RR()     
               
def Main():
    print("Welcome to CPU Scheduling (OS)")
    print("Name: John Benedict M. Villegas")
    print("Section:  BSIT 1A")
    
    print("\nChoose CPU Scheduling: ")
    print(" 1. First Come, First Served (FCFS)")
    print(" 2. Shortest Job First (SJF)")
    print(" 3. Shortest Remaining Time First (SRTF)")
    print(" 4. Round Robin (RR)")
    
    while True:
        try:
            choice = int(input(f"\nEnter your choice (1-4): "))
            if choice not in [1, 2, 3, 4]:
                raise ValueError("Invalid choice. Please enter a number between 1 and 4.") 
            break          
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")
    
    Choices(choice)   
     
Main()
