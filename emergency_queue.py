# emergency_queue.py

class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []  # list of Patient objects

    # Move a node UP the heap to restore heap property
    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency < self.data[parent].urgency:
                # swap
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    # Move a node DOWN the heap to restore heap property
    def heapify_down(self, index):
        size = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    # Add a patient
    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    # Print the heap
    def print_heap(self):
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")

    # Return most urgent patient without removing
    def peek(self):
        if self.data:
            return self.data[0]
        return None

    # Remove and return most urgent patient
    def remove_min(self):
        if not self.data:
            return None

        min_patient = self.data[0]
        last = self.data.pop()

        if self.data:
            self.data[0] = last
            self.heapify_down(0)

        return min_patient


# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()

    # Insert patients
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.insert(Patient("Riley", 2))

    heap.print_heap()

    # Peek test
    next_up = heap.peek()
    print("Next up:", next_up.name, next_up.urgency)

    # Remove test
    served = heap.remove_min()
    print("Served:", served.name)

    heap.print_heap()

    # Edge case: remove until empty
    heap.remove_min()
    heap.remove_min()
    heap.remove_min()
    print("After clearing heap:", heap.data)

    # Edge case: peek on empty heap
    print("Peek empty:", heap.peek())
