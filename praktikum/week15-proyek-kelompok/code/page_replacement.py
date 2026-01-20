import os
from utils.table import print_table

def run_page_replacement():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, "data", "page_data.txt")

    with open(data_path) as f:
        pages = list(map(int, f.read().split()))

    frames = 3
    fifo, lru = [], []
    fifo_fault, lru_fault = 0, 0
    rows = []

    for p in pages:
        # FIFO
        if p in fifo:
            fifo_status = "Hit"
        else:
            fifo_status = "Fault"
            fifo_fault += 1
            if len(fifo) == frames:
                fifo.pop(0)
            fifo.append(p)

        # LRU
        if p in lru:
            lru_status = "Hit"
            lru.remove(p)
        else:
            lru_status = "Fault"
            lru_fault += 1
            if len(lru) == frames:
                lru.pop(0)
        lru.append(p)

        rows.append([
            p,
            " ".join(map(str, fifo)),
            fifo_status,
            " ".join(map(str, lru)),
            lru_status
        ])

    print("\nPAGE REPLACEMENT (FIFO & LRU)")
    print_table(
        ["Page", "FIFO Frame", "FIFO Status", "LRU Frame", "LRU Status"],
        rows
    )

    print(f"\nTotal FIFO Fault : {fifo_fault}")
    print(f"Total LRU  Fault : {lru_fault}")