def build_item_text(item):
    parts = [
        item.title or "",
        item.description or "",
        str(item.category) if item.category else ""
    ]
    return " ".join(parts)
