# Task 1.1
def book_finder(book_name, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if book_name.lower() in line.lower():
                return "Available" if "available" in line.lower() else "Not Available"
        return "Book not found"

book_name = "Harry Potter"
book_availability = book_finder(book_name, "book_inventory.txt")
print(f"The availability of {book_name} is: {book_availability}")


# Task 1.2
import csv

def price(book_name, csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if book_name.lower() in row[0].lower():
                return row[1]
        return "Price not found"

book_name = "Harry Potter"
book_price = price(book_name, "book_prices.csv")
print(f"The price of {book_name} is: {book_price}")


# Task 1.3
def write_availability_to_csv(availability_dict, output_csv):
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Book', 'Availability'])
        for book, availability in availability_dict.items():
            writer.writerow([book, availability])

availability_dict = {
    "Harry Potter": "Available",
    "Lord of the Rings": "Not Available",
    "Game of Thrones": "Available"
}
write_availability_to_csv(availability_dict, "book_availability.csv")
