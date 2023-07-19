import datetime
from collections import OrderedDict

class Removal:
    def __init__(self, value: str, status: bool):
        self.value = value
        self.is_fine_status = status

def remove_ids(input_f) -> list[str]:
    all_ids = OrderedDict()
    removal_ids = OrderedDict()
    is_input_ids = True

    for unique_id in input_f:
        unique_id_strip = unique_id.strip()
        if unique_id_strip == '-':
            is_input_ids = False
            continue

        if is_input_ids:
            all_ids[unique_id_strip] = True
        else:
            removal_ids[unique_id_strip] = True

    input_removal_ids: list[Removal] = [Removal(x, True) for x in all_ids.keys()]

    for input_id in input_removal_ids:
        if any(removal_id in input_id.value for removal_id in removal_ids.keys()):
            input_id.is_fine_status = False

    return [y.value for y in input_removal_ids if y.is_fine_status]

def write_ids(file_name: str, ids: list[str]):
    with open(file_name, 'w') as w_file:
        for u_id in ids:
            w_file.write(f"{u_id}\n")

if __name__ == "__main__":
    with open("input_ids.txt") as input_f:
        result_after_removal = remove_ids(input_f)

        time_now = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')

        write_ids(f"result_{time_now}.txt", result_after_removal)