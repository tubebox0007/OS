n = int(input("Enter number of processes: "))
processes = [{'id': i+1, 'AT': int(at), 'BT': int(bt)} for i in range(n) for at, bt in [input(f"Enter AT and BT for process {i+1}: ").split()]]
processes.sort(key=lambda p: p['AT'])
current_time = total_WT = total_TAT = 0
for _ in range(n):
    available_processes = [p for p in processes if p['AT'] <= current_time and 'WT' not in p]
    if available_processes:
        p = min(available_processes, key=lambda p: p['BT'])
    else:
        current_time = processes[_]['AT']
        p = min([p for p in processes if p['AT'] <= current_time and 'WT' not in p], key=lambda p: p['BT'])
    current_time += p['BT']
    p['TAT'], p['WT'] = current_time - p['AT'], current_time - p['AT'] - p['BT']
    total_WT += p['WT']
    total_TAT += p['TAT']
    print(f"P{p['id']} -> CT: {current_time}, TAT: {p['TAT']}, WT: {p['WT']}")
print(f"Avg TAT: {total_TAT/n:.2f}, Avg WT: {total_WT/n:.2f}")
