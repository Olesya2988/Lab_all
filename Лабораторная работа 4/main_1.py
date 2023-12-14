import json

INPUT_FILE = "input.json"


# TODO решите задачу
def task() -> float:
    with open(INPUT_FILE, 'r') as file_read:
        dict_ = json.load(file_read)
    sum_all = sum([i["score"] * i["weight"] for i in dict_])
    return float(format(sum_all, ".3f"))


print(task())
