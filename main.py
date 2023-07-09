import datetime

def remove_ids(input_f):
    all_ids = list(map(str.strip, input_f.readlines()))
    print(all_ids)

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

    return list(set(input_ids).difference(set(removal_ids)))


def write_ids(file_name: str, ids: list[str]):
    with open(file_name, 'x') as w_file:
        for u_id in ids:
            w_file.write(f"{u_id}\n")

if __name__ == "__main__":
    with open("input_ids.txt") as input_f:
        result_after_removal = remove_ids(input_f)

        time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')

        write_ids(f"result_{time_now}.txt", result_after_removal)
