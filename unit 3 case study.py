# Hospital Patient Queue Management System
# Using Queue and Linked List

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class HospitalQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Add patient to queue
    def add_patient(self, name):
        new_node = Node(name)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(name, "added to the queue.")

    # Serve next patient
    def serve_patient(self):
        if self.front is None:
            print("No patients waiting.")
            return

        print("Now serving:", self.front.name)
        self.front = self.front.next

        if self.front is None:
            self.rear = None

    # Display waiting patients
    def display_queue(self):
        if self.front is None:
            print("Queue is empty.")
            return

        current = self.front
        print("\nPatients waiting:")

        while current:
            print("->", current.name)
            current = current.next

    # Count waiting patients
    def count_patients(self):
        count = 0
        current = self.front

        while current:
            count += 1
            current = current.next

        print("Total waiting patients:", count)


hospital = HospitalQueue()

while True:
    print("\n===== HOSPITAL QUEUE SYSTEM =====")
    print("1. Add Patient")
    print("2. Serve Patient")
    print("3. Display Waiting List")
    print("4. Count Patients")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter patient name: ")
        hospital.add_patient(name)

    elif choice == "2":
        hospital.serve_patient()

    elif choice == "3":
        hospital.display_queue()

    elif choice == "4":
        hospital.count_patients()

    elif choice == "5":
        print("Hospital Queue System Closed.")
        break

    else:
        print("Invalid choice. Try again.")