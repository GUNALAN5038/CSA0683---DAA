def minimumTimeRequired(jobs, k):
    def canFinish(jobs, k, mid, workers):
        if not jobs:
            return True
        job = jobs.pop()
        for i in range(k):
            if workers[i] + job <= mid:
                workers[i] += job
                if canFinish(jobs, k, mid, workers):
                    return True
                workers[i] -= job
            if workers[i] == 0:
                break
        jobs.append(job)
        return False

    left, right = max(jobs), sum(jobs)
    while left < right:
        mid = (left + right) // 2
        if canFinish(sorted(jobs, reverse=True), k, mid, [0] * k):
            right = mid
        else:
            left = mid + 1
    return left
jobs1 = [3, 2, 3]
k1 = 3
print(minimumTimeRequired(jobs1, k1)) 

jobs2 = [1, 2, 4, 7, 8]
k2 = 2
print(minimumTimeRequired(jobs2, k2)) 
