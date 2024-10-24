n = int(input("Enter number of processes: "))
at = list(map(int, input("Enter Arrival Times: ").split()))
bt = list(map(int, input("Enter Burst Times: ").split()))
priority = list(map(int, input("Enter Priorities: ").split()))
processes = list(range(n))
process_info = list(zip(processes, at, bt, priority))
process_info.sort(key=lambda x: (x[3], x[1]))
processes, at, bt, priority = zip(*process_info)
CT = [0] * n
TAT = [0] * n
WT = [0] * n
CT[0] = at[0] + bt[0]
for i in range(1, n):
    CT[i] = max(at[i], CT[i-1]) + bt[i]
TAT = [CT[i] - at[i] for i in range(n)]  
WT = [TAT[i] - bt[i] for i in range(n)] 
print(f"\nPID\tAT\tBT\tPriority\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{processes[i]+1}\t{at[i]}\t{bt[i]}\t{priority[i]}\t\t{CT[i]}\t{TAT[i]}\t{WT[i]}")
print(f"\nAverage Turnaround Time: {sum(TAT)/n:.2f}")
print(f"Average Waiting Time: {sum(WT)/n:.2f}")
