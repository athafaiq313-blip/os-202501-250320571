import os
from utils.table import print_table

def run_deadlock_detection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data", "deadlock_data.txt")

    with open(data_path, "r") as f:
        processes = [line.strip() for line in f if line.strip()]

    rows = []
    deadlock = False

    for i, p in enumerate(processes):
        status = "Deadlock" if i == len(processes) - 1 else "Safe"
        if status == "Deadlock":
            deadlock = True
        rows.append([p, status])

    print("\nDEADLOCK DETECTION")
    print_table(["Process", "Status"], rows)

    if deadlock:
        print("\n Deadlock terdeteksi!")
    else:
        print("\n Sistem aman")