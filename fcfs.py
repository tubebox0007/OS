n = int(input("Enter number of processes: "))
at = list(map(int, input("Enter Arrival Times: ").split()))
bt = list(map(int, input("Enter Burst Times: ").split()))
CT = [0] * n
CT[0] = at[0] + bt[0]
for i in range(1, n):
    CT[i] = max(at[i], CT[i-1]) + bt[i]
TAT = [CT[i] - at[i] for i in range(n)]
WT = [TAT[i] - bt[i] for i in range(n)]
print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"P{i+1}\t{at[i]}\t{bt[i]}\t{CT[i]}\t{TAT[i]}\t{WT[i]}")
print(f"\nAverage Waiting Time: {sum(WT)/n:.2f}")
print(f"Average Turnaround Time: {sum(TAT)/n:.2f}")
