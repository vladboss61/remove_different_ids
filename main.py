import datetime

class Removal:
    def __init__(self, value: str, status: bool):
        self.value = value
        self.status = status

def remove_ids(input_f):
    all_ids = list(map(str.strip, input_f.readlines()))

    input_ids = []
    removal_ids = []

    is_input_ids = True

    for unique_id in all_ids:
        if unique_id == '-':
            is_input_ids = False
            continue

        if is_input_ids:
            input_ids.append(unique_id)
        else:
            removal_ids.append(unique_id)

        input_removal_ids: list[Removal] = [Removal(x, False) for x in input_ids]

        for input_id in input_removal_ids:
            for removal_id in removal_ids:
                if input_id.value == removal_id:
                    input_id.status = True

    return [y.value for y in input_removal_ids if not y.status]


def write_ids(file_name: str, ids: list[str]):
    with open(file_name, 'x') as w_file:
        for u_id in ids:
            w_file.write(f"{u_id}\n")

if __name__ == "__main__":
    with open("input_ids.txt") as input_f:
        result_after_removal = remove_ids(input_f)

        time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')

        write_ids(f"result_{time_now}.txt", result_after_removal)
