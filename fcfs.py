# ask user for 5 num Process


def Process(p):
     numbers = []    
     print("\nEnter Process")   
     for i in range(1, p+1):   
        arrvl = int(input(f"Arrival Time P{i}: "))
        burst = int(input(f"Burst Time P{i}: "))
        print("")
        numbers.append((f"P{i}", arrvl, burst))
     
       
     return numbers
     
def Display(pronum):
    print("\n Process\tArrival Time\tBurst Time")

    #input = "\n ".join(str(num) for num in numbers)+"\tsum"
    waiting = []
    completion = []
    turnaround = []
    ctime = 0
    
    for label, arrvl, burst in pronum:
        ctime = max(ctime, arrvl) + burst
        completion.append(ctime)
        
        wtime = ctime - arrvl - burst
        waiting.append(wtime)
        
        tat = ctime - arrvl
        turnaround.append(tat)
        print(f" {label}\t\t{arrvl}\t\t{burst}")
        
    print(f"\nCompletion Time\tTurnaround Time\tWaiting Time")
    
    for i in range(len(pronum)):    
        print(f" {completion[i]}\t\t{turnaround[i]}\t\t{waiting[i]}")
    
def Main():    
    print("First Come, First Served(FCFS) \n")      
    
    numpt = int(input(f"How Many Process Time: ")) 
    pronum = Process(numpt)
    Display(pronum)

Main()

