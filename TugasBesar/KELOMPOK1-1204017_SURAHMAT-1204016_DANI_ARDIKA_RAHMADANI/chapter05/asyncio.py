import asyncio
import sys


async def calculate_shipping_cost(weight):
    # Simulate calculating the shipping cost
    await asyncio.sleep(2)
    shipping_cost = weight * 10  # Assume the cost is $10 per kilogram
    return shipping_cost


async def calculate_delivery_time(distance):
    # Simulate calculating the delivery time
    await asyncio.sleep(3)
    delivery_time = distance * 0.5  # Assume the time is 0.5 hours per kilometer
    return delivery_time


async def main():
    weight = int(sys.argv[1])
    distance = int(sys.argv[2])
    print(f"Weight: {weight} kg")
    print(f"Distance: {distance} km")

    shipping_cost_future = asyncio.ensure_future(calculate_shipping_cost(weight))
    delivery_time_future = asyncio.ensure_future(calculate_delivery_time(distance))

    await asyncio.wait([shipping_cost_future, delivery_time_future])

    shipping_cost = shipping_cost_future.result()
    delivery_time = delivery_time_future.result()

    print(f"Shipping cost: ${shipping_cost}")
    print(f"Delivery time: {delivery_time} hours")


if __name__ == '__main__':
    asyncio.run(main())
