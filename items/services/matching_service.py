from items.models import LostItem
from items.utils.text_matching import text_similarity
from items.utils.item_text import build_item_text


def match_found_to_lost(found_item, threshold=60):
    found_text = build_item_text(found_item)

    candidates = LostItem.objects.filter(
        category=found_item.category
    )

    matches = []

    for lost in candidates:
        lost_text = build_item_text(lost)
        score = text_similarity(found_text, lost_text)

        if score >= threshold:
            matches.append({
                "lost_item": lost,
                "score": round(score, 2)
            })

    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches
