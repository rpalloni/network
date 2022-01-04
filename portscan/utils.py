import json
import os
from multiprocessing.pool import ThreadPool

def extract_json_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def display_progress_bar(port_idx, port_size, cli):
    bar_max_width = 45  # set width max and apply proportion => x:45=idx:698
    bar_current_width = bar_max_width * port_idx // port_size
    bar = "█" * bar_current_width + "-" * (bar_max_width - bar_current_width)
    progress = "%.1f" % (port_idx / port_size * 100)
    cli.print(f"|{bar}| {progress} %", end="\r", style="bold green")
    if port_idx == port_size:
        print()


def threadpool_executor(function, iterable, cli):
    number_of_workers = os.cpu_count()
    print(f"\nRunning using {number_of_workers} workers.\n")
    with ThreadPool(number_of_workers) as pool:
        for idx, value in enumerate(pool.imap(function, iterable), 1):
            # print(f'list index: {idx}', value)
            display_progress_bar(idx, len(iterable), cli) # idx => ports list index, len => ports list size
