from typing import List

def count_bikes_needed(package_weights: List[int], bike_capacity: int) -> int:
    """
    Count the number of bikes needed to deliver the packages.

    Args:
        package_weights (List[int]): A list of weights of the packages to be delivered.
        bike_capacity (int): The maximum weight a bike can carry.

    Returns:
        int: The number of bikes needed.
    """
    number_of_bikes = 0

    for i in range(0, len(package_weights), 2):
        if i < len(package_weights) and i+1 < len(package_weights):
            if package_weights[i] + package_weights[i+1] <= bike_capacity:
                number_of_bikes += 1
            else:
                number_of_bikes += 2

    return number_of_bikes

def calculate_bike_deliveries(package_weights: List[int], bike_capacity: int) -> int:
    """
    Calculate the number of bikes needed to deliver packages based on their weights and the bike's capacity.

    Args:
        package_weights (List[int]): A list of weights of the packages to be delivered.
        bike_capacity (int): The maximum weight a bike can carry.

    Returns:
        int: The number of bikes needed to deliver all packages.
    """
    package_weights.sort()
    return count_bikes_needed(package_weights, bike_capacity)

# Test cases
package_weights = [5,3,2,5,6,1,4,7,9]
bike_capacity = 10
print(calculate_bike_deliveries(package_weights, bike_capacity))