import numpy as np
no_p, no_r = 5, 4
allocated = np.array([[4, 0, 0, 1], [1, 1, 0, 0], [1, 2, 5, 4], [0, 6, 3, 3], [0, 2, 1, 2]])
maximum = np.array([[6, 0, 1, 2], [1, 7, 5, 0], [2, 3, 5, 6], [1, 6, 5, 3], [1, 6, 5, 6]])
available, visited, seq = np.array([3, 2, 1, 1]), np.zeros(no_p), []
needed = maximum - allocated
while len(seq) < no_p:
    for i in range(no_p):
        if not visited[i] and np.all(needed[i] <= available):
            seq.append(i)
available += allocated[i]
visited[i] = 1
print("Needed Resource:\n", needed, "\nThe system is Safe\nSafe")
Sequence:(" seq\nAvailable Resource:", available,"")
