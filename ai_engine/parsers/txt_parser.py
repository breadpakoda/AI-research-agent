def parse(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()

    except Exception as e:
        raise Exception(f"Failed to parse TXT: {e}")