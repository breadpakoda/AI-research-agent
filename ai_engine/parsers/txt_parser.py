import re


def parse(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        paragraphs = []
        for paragraph in re.split(r"\n\s*\n+", text):
            cleaned = " ".join(paragraph.split())
            if cleaned:
                paragraphs.append(cleaned)

        return paragraphs

    except Exception as e:
        raise Exception(f"Failed to parse TXT: {e}")


# print(parse("parsers/aa.txt"))