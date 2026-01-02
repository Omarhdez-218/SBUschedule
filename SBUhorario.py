import random
​
# List of pods
pods = ["B", "C", "D", "E", "F", "G",
        "I", "J", "K", "L", "breaker"]
​
#List of arbitrary's workers
workers = [
    "worker1",  #Jamie
    "worker2",  #Claudia
    "worker3",  #Mark
    "worker4",  #Omar
    "worker5",  #Bill
    "worker6",  #Sue
    "worker7",  #Taara
    "worker8",  #Lisa
    "worker9",  #Lysa
    "worker10", #Fritz
    "worker11", #Syed
    "worker12", #Anghy
    "worker13", #Paula
    "worker14", #Andrew
    "worker15", #Alina
    "worker16", #Terry
    "worker17", #Avery
]
​
# List of workers that can't be assigned pod "K"
float_workers = set(["worker4", "worker14", "worker15", "worker16", "worker17"])


# Shuffling items in Pods list
random.shuffle(pods)
​
# Assigning fixed days off for each worker
worker_passdays = {
    "worker1": [3, 4, 8, 13], #Jamie
    "worker2": [2, 7, 10, 11], #Claudia
    "worker3": [4, 5, 11, 12], #Mark
    "worker4": [3, 4, 8, 12], #Omar
    "worker5": [3, 4, 8, 13], #Bill
    "worker6": [2, 5, 10, 11], #Sue
    "worker7": [3, 4, 9, 12], #Taara
    "worker8": [3, 4, 9, 13], #Lisa
    "worker9": [1, 6, 10, 11], #Lysa
    "worker10": [2, 7, 10, 11], #Fritz
    "worker11": [2, 5, 10, 11], #Syeda
    "worker12": [3, 4, 9, 12], #Anghy
    "worker13": [3, 4, 8, 14], #Paula
    "worker14": [1, 6, 10, 11], #Andrew
    "worker15": [1, 6, 10, 11], #Alina
    "worker16": [3, 4, 8, 14], #Terry
    "worker17": [1, 7, 10, 11], #Avery
}

# Track used pods & add them to a set
used_pods = {}
for w in workers:
    used_pods[w] = set()
​
# Empty dictionary that will add each worker a unique position for each day
schedule = {}
​
​
for day in range(14):
    # Rotating pods
    daily_pods = pods[day:] + pods[:day]
    daily_assignment = {}
    pod_index = 0
​

    for worker in workers:
​
        # Assign passday to workerd based on workers_passday dict
        if (day + 1) in worker_passdays[worker]:
            daily_assignment[worker] = "passday"
            continue
​
        # Checks if a worker is already assigned a specific pod
        assigned = False
​
        for i in range(len(daily_pods)):
            # Prevents daily_pods being out of index
            candidate = daily_pods[pod_index % len(daily_pods)]
            pod_index = pod_index + 1
​
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
​
        if not assigned:
            raise RuntimeError("No available pod for " + worker +
                               " on day " + str(day + 1))
​
    schedule["day" + str(day + 1)] = daily_assignment
​
# Print schedule
for day in schedule:
    print(day + ": " + str(schedule[day]))
    print("")
