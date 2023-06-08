import asyncio
import Pyro4
from mpi4py import MPI

async def connect_to_server():
    inventory = Pyro4.Proxy("PYRONAME:inventory")

    while True:
        print("\n=== Inventory Management Menu ===")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. Show all items")
        print("5. Show item details")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_id = input("Enter item ID: ")
            item_name = input("Enter item name: ")
            result = inventory.add_item(item_id, item_name)
            print(result)

        elif choice == "2":
            item_id = input("Enter item ID to remove: ")
            result = inventory.remove_item(item_id)
            print(result)

        elif choice == "3":
            item_id = input("Enter item ID to update: ")
            new_name = input("Enter new item name: ")
            result = inventory.update_item(item_id, new_name)
            print(result)

        elif choice == "4":
            items = inventory.get_all_items()
            if items:
                print("=== All Items ===")
                for item_id, item_name in items.items():
                    print(f"ID: {item_id}, Name: {item_name}")
            else:
                print("No items found.")

        elif choice == "5":
            item_id = input("Enter item ID to show details: ")
            item_name = inventory.get_item_details(item_id)
            if item_name:
                print("=== Item Details ===")
                print(f"ID: {item_id}, Name: {item_name}")
            else:
                print("Item not found.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

async def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank != 0:
        await connect_to_server()

    barrier = comm.bcast(None, root=0)
    await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())
