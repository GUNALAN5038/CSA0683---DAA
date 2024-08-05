def container_loader(containers, capacity):
    containers.sort(reverse=True)
    total_weight = 0
    for container in containers:
        if total_weight + container <= capacity:
            total_weight += container
    return total_weight

containers = [10, 20, 30, 40, 50]
capacity = 100
print("Maximum weight loaded in container:", container_loader(containers, capacity))
