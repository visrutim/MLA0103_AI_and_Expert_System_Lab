"""Experiment 10: Towers of Hanoi using recursion."""

def hanoi(n, source, auxiliary, destination):
    if n <= 0:
        return
    hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)

if __name__ == "__main__":
    disks = 3
    print(f"Moves for {disks} disks:")
    hanoi(disks, "A", "B", "C")
