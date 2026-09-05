def clean_lines(lines):

    cleaned = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if cleaned:

            previous = cleaned[-1]

            # Merge only if previous is a bullet
            # AND current line is clearly a continuation
            if (
                previous.startswith("•")
                and not line.startswith("•")
                and "|" not in line
            ):
                cleaned[-1] += " " + line
                continue

        cleaned.append(line)

    return cleaned