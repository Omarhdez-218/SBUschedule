
import random

# List of pods
pods = ["B", "C", "D", "E", "F", "G",
        "I", "J", "K", "L", "breaker1", "breaker2"]

#List of arbitrary's workers
workers = [
    "worker1",  #Bill
    "worker2",  #Sue
    "worker3",  #Mark
    "worker4",  #Syeda
    "worker5",  #Lisa1
    "worker6",  #Lisa2
    "worker7",  #Claudia
    "worker8",  #Tara
    "worker9",  #Jamie??
    "worker10", #....
    "worker11", #Omar
    "worker12", #newGuy
    "worker13", #Alina
    "worker14", #newGirl
]

# List of workers that can't be assigned pod "K"
float_workers = set(["worker11", "worker12", "worker13", "worker14"])

# Shuffling items in Pods list
random.shuffle(pods)

# Assigning fixed days off for each worker
worker_passdays = {
    "worker1": [4, 9],
    "worker2": [2, 7],
    "worker3": [1, 10],
    "worker4": [3, 12],
    "worker5": [5, 11],
    "worker6": [6, 14],
    "worker7": [8, 13],
    "worker8": [1, 6],
    "worker9": [2, 12],
    "worker10": [3, 7],
    "worker11": [4, 10],
    "worker12": [5, 13],
    "worker13": [8, 14],
    "worker14": [9, 11]
}

# Track used pods & add them to a set
used_pods = {}
for w in workers:
    used_pods[w] = set()

# Empty dictionary that will add each worker a unique position for each day
schedule = {}


for day in range(14):
    # Rotating pods
    daily_pods = pods[day:] + pods[:day]
    daily_assignment = {}
    pod_index = 0

    for worker in workers:

        # Assign passday to workerd based on workers_passday dict
        if (day + 1) in worker_passdays[worker]:
            daily_assignment[worker] = "passday"
            continue

        # Checks if a worker is already assigned a specific pod
        assigned = False

        for i in range(len(daily_pods)):
            # Prevents daily_pods being out of index
            candidate = daily_pods[pod_index % len(daily_pods)]
            pod_index = pod_index + 1

            # Float worker cannot take K
            if worker in float_workers and candidate == "K":
                if "float" not in used_pods[worker]:
                    daily_assignment[worker] = "float"
                    used_pods[worker].add("float")
                    assigned = True
                    break
                continue
                    
            if candidate not in used_pods[worker]:
                daily_assignment[worker] = candidate
                used_pods[worker].add(candidate)
                assigned = True
                break

        if not assigned:
            raise RuntimeError("No available pod for " + worker +
                               " on day " + str(day + 1))

    schedule["day" + str(day + 1)] = daily_assignment

# Print schedule
for day in schedule:
    print(day + ": " + str(schedule[day]))
