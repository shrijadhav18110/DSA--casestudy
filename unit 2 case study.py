# Metro Station Connectivity System
# Using Graph and Adjacency Matrix

stations = [
    "Pune",
    "PCMC",
    "Shivajimaharajnagar",
    "Civil Court",
    "Vanaz"
]

n = len(stations)

# Create adjacency matrix
matrix = [[0] * n for _ in range(n)]


def add_connection(station1, station2):
    if station1 in stations and station2 in stations:
        i = stations.index(station1)
        j = stations.index(station2)

        matrix[i][j] = 1
        matrix[j][i] = 1

        print("Connection added successfully!")
    else:
        print("Invalid station name!")


def display_matrix():
    print("\nMetro Station Adjacency Matrix")
    print(" " * 18, end="")

    for station in stations:
        print(f"{station[:8]:>10}", end="")

    print()

    for i in range(n):
        print(f"{stations[i]:<18}", end="")
        for j in range(n):
            print(f"{matrix[i][j]:>10}", end="")
        print()


def check_connection(station1, station2):
    if station1 in stations and station2 in stations:
        i = stations.index(station1)
        j = stations.index(station2)

        if matrix[i][j] == 1:
            print(station1, "has a direct connection to", station2)
        else:
            print(station1, "has no direct connection to", station2)
    else:
        print("Invalid station name!")


# Sample metro connections
add_connection("Pune", "Shivajinagar")
add_connection("Shivajinagar", "Civil Court")
add_connection("Civil Court", "PCMC")
add_connection("Civil Court", "Vanaz")

while True:
    print("\n===== METRO CONNECTIVITY SYSTEM =====")
    print("1. Display all stations")
    print("2. Add connection")
    print("3. Display adjacency matrix")
    print("4. Check direct connection")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nMetro Stations:")
        for station in stations:
            print("-", station)

    elif choice == "2":
        s1 = input("Enter first station: ")
        s2 = input("Enter second station: ")
        add_connection(s1, s2)

    elif choice == "3":
        display_matrix()

    elif choice == "4":
        s1 = input("Enter first station: ")
        s2 = input("Enter second station: ")
        check_connection(s1, s2)

    elif choice == "5":
        print("Thank you for using Metro Connectivity System!")
        break

    else:
        print("Invalid choice! Please try again.")