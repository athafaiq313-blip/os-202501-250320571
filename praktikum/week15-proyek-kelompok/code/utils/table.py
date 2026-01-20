def print_table(headers, rows):
    widths = [len(h) for h in headers]

    for row in rows:
        for i, item in enumerate(row):
            widths[i] = max(widths[i], len(str(item)))

    def line():
        print("+" + "+".join("-" * (w + 2) for w in widths) + "+")

    line()
    print("| " + " | ".join(headers[i].ljust(widths[i]) for i in range(len(headers))) + " |")
    line()

    for row in rows:
        print("| " + " | ".join(str(row[i]).ljust(widths[i]) for i in range(len(row))) + " |")

    line()