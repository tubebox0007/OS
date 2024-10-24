n = int(input("Enter number of processes: "))
at = list(map(int, input("Enter Arrival Times: ").split()))
bt = list(map(int, input("Enter Burst Times: ").split()))
qt = int(input("Enter Time Quantum: "))
CT = [0] * n
remaining_time = bt[:] 
time = 0 
done = False
while not done:
    done = True  
    for i in range(n):
        if remaining_time[i] > 0: 
            done = False  
            t = min(qt, remaining_time[i])  
            time += t  
            remaining_time[i] -= t 
            if remaining_time[i] == 0: 
                CT[i] = time
TAT = [CT[i] - at[i] for i in range(n)] 
WT = [TAT[i] - bt[i] for i in range(n)]  
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{i + 1}\t{at[i]}\t{bt[i]}\t{CT[i]}\t{TAT[i]}\t{WT[i]}")
print(f"\nAverage WT: {sum(WT)/n:.2f}, Average TAT: {sum(TAT)/n:.2f}")
