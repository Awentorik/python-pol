



import json
import os

current_dir = os.getcwd()

def task() -> float:
    json_file_name = 'input.json'
    with open(os.path.join(current_dir, json_file_name), 'r') as file:
        data = json.load(file)
    sum_of_products = sum([item["score"] * item["weight"] for item in data])
    return round(sum_of_products, 3)

print(task())