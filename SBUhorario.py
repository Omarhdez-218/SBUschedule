
import random

pods = ["B", "C", "D", "E", "F", "G",
        "I", "J", "K", "L", "breaker1", "breaker2"]

workers = [
    "worker1", "worker2", "worker3", "worker4",
    "worker5", "worker6", "worker7", "worker8",
    "worker9", "worker10", "worker11", "worker12",
    "worker13", "worker14"
]

float_workers = set(["worker11", "worker12", "worker13", "worker14"])

random.shuffle(pods)

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

used_pods = {}
for w in workers:
    used_pods[w] = set()

schedule = {}

for day in range(14):
    daily_pods = pods[day:] + pods[:day]
    daily_assignment = {}
    pod_index = 0

    for worker in workers:

        # Pass day
        if (day + 1) in worker_passdays[worker]:
            daily_assignment[worker] = random.choice(["passday1", "passday2"])
            continue

        assigned = False

        for i in range(len(daily_pods)):
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
