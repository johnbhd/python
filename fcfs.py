def FCFS():    
    #user input
    def Process(p):
        numbers = []    
        print("\nEnter Process")   
        for i in range(1, p+1):   
            arrvl = int(input(f"Arrival Time P{i}: "))
            burst = int(input(f"Burst Time P{i}: "))
            print("")
            numbers.append((f"P{i}", arrvl, burst))
              
        return numbers

    # display    
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
            
            wtime = ctime - arrvl - burst
            waiting.append(wtime)
            total_wt += wtime
            
            print(f" {label}\t\t{arrvl}\t\t{burst}")
            
        print(f"\nCompletion Time\tTurnaround Time\tWaiting Time")
        
        for i in range(len(pronum)):    
            print(f" {completion[i]}\t\t{turnaround[i]}\t\t{waiting[i]}")
        
        atat = total_tat / len(pronum)
        awt = total_wt / len(pronum)
        
        print(f"\n Average Turn around Time: {atat: .2f}\n Average waiting time: {awt: .2f}")

    #1st display
    print("\nFirst Come, First Served(FCFS) ")      
    while True:
        try:   
            numpt = int(input(f"How Many Process Time: ")) 
            pronum = Process(numpt)
            Display(pronum)
            break
        except ValueError:
            print("Invalid Input, try again.\n")
  
def  SJF():
     print("\nShortest Job First")
     
def  SRTF():
     print("\nShortest Remaining Time First")
     
def  RR():
     print("\nRound Robin")
                       
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
