tax = 0.10
INVENTORY_FILE = "inventory.txt"

deliveries = 0


def load_inventory():
    """Read saved total and history. Start with empty inventory if file is unreadable"""
    try:
        with open(INVENTORY_FILE, "r") as f:
            total = int(f.readline().strip())
            line = f.readline().strip()
            history = [int(x) for x in line.split(",")] if line else []
        print(f"Loaded saved inventory: total = {total}, history = {history}\n")
        return total, history
    except FileNotFoundError:
        print("No inventory file found. Starting with an empty inventory.\n")
        return 0, []
    except ValueError:
        print("Inventory file is unreadable. Starting with an empty inventory.\n")
        return 0, []

def save_inventory(total, history):
    """Write the total and history back to file."""
    with open(INVENTORY_FILE, "w") as f:
        f.write(f"{total}\n")
        f.write(",".join(str(x) for x in history) + "\n")
        print(f"Inventory saved to {INVENTORY_FILE}")

    
def get_valid_input():
    user_input = input("Enter stock quantity: ").strip()
    if user_input.lower() == "quit":
        return "quit"

    if not user_input.isdigit():
        print(f"Error: '{user_input}' is not a valid number. Please enter a whole number.\n")
        return None

    return int(user_input)

def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * tax


def generate_report(total_units, failed_attempts, history):
    total_tax = calculate_tax(total_units)
    print("=== End of Session Report ===")
    print(f"Total Deliveries Processed: {deliveries}")
    print(f"Total Units Processed: {total_units}")
    print(f"Total Tax Collected: {total_tax:.2f}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    print(f"Transaction History: {history}")


def main():
    global deliveries
    total_inventory, history = load_inventory()
    failed_entries = 0

    print("=== Smart Inventory Auditor ===")
    print("Enter stock quantities to add to inventory.")
    print("Type 'quit' to stop and see the report.\n")

    while True:
        user_input = get_valid_input()

        if user_input == "quit":
            break

        if user_input is None:
            failed_entries += 1
            continue

        quantity = user_input

        if quantity < 0:
            print("Error: Negative quantities are not allowed.\n")
            failed_entries += 1
            continue
        else:
            total_inventory = process_delivery(total_inventory, quantity)
            history.append(quantity)
            deliveries += 1
            print(f"Accepted: +{quantity} units. Running total: {total_inventory}\n")

    generate_report(total_inventory, failed_entries, history)
    save_inventory(total_inventory, history)


main()
