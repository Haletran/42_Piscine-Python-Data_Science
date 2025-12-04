import os


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, item in enumerate(lst, start=1):
        try:
            cols = os.get_terminal_size().columns
        except OSError:
            cols = 80
        percent = i / total
        pct_text = f"{percent * 100:3.0f}%"
        info = f"{i}/{total}"
        width = max(10, cols - len(info) - 7)
        filled = int(width * percent)
        bar = "█" * filled + " " * (width - filled)

        os.write(1, f"\r{pct_text}|{bar}|{info}".encode())
        yield item

    os.write(1, b"\n")
