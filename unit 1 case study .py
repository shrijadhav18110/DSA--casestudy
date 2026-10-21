# Smart E-commerce Product Sorting System
# Using Merge Sort (Divide and Conquer)

products = [
    {"name": "Mouse", "price": 499, "rating": 4.2, "popularity": 85},
    {"name": "Headphones", "price": 1499, "rating": 4.5, "popularity": 95},
    {"name": "Keyboard", "price": 799, "rating": 4.0, "popularity": 70},
    {"name": "Laptop Stand", "price": 999, "rating": 4.7, "popularity": 80},
    {"name": "USB Cable", "price": 199, "rating": 3.9, "popularity": 60},
    {"name": "Power Bank", "price": 1299, "rating": 4.3, "popularity": 90}
]


def merge_sort(items, key, descending=False):
    if len(items) <= 1:
        return items

    mid = len(items) // 2

    left = merge_sort(items[:mid], key, descending)
    right = merge_sort(items[mid:], key, descending)

    return merge(left, right, key, descending)


def merge(left, right, key, descending):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if descending:
            condition = left[i][key] >= right[j][key]
        else:
            condition = left[i][key] <= right[j][key]

        if condition:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def display_products(items):
    print("\n{:<20} {:<12} {:<10} {:<12}".format(
        "Product", "Price", "Rating", "Popularity"
    ))
    print("-" * 55)

    for p in items:
        print("{:<20} {:<12} {:<10} {:<12}".format(
            p["name"], p["price"], p["rating"], p["popularity"]
        ))


while True:
    print("\nSMART E-COMMERCE PRODUCT SORTING SYSTEM")
    print("1. Sort by Price")
    print("2. Sort by Rating")
    print("3. Sort by Popularity")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Thank you!")
        break

    if choice == "1":
        key = "price"
    elif choice == "2":
        key = "rating"
    elif choice == "3":
        key = "popularity"
    else:
        print("Invalid choice!")
        continue

    order = input("1. Low to High  2. High to Low: ")

    sorted_products = merge_sort(
        products, key, descending=(order == "2")
    )

    display_products(sorted_products)