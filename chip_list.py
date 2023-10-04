def display_chips(chips=None, max_chips_displayed=None, max_text_length=None):
    
    if not chips or not isinstance(chips, list) or len(chips) == 0:
        return []

    
    if max_chips_displayed and max_chips_displayed <= 0:
        raise ValueError("maxChipsDisplayed should be greater than 0")

    if max_text_length and max_text_length <= 0:
        raise ValueError("maxTextLength should be greater than 0")

    # Apply maxChipsDisplayed limitation
    displayed_chips = chips[:max_chips_displayed]

    # Process chips and apply the maxTextLength limitation
    for idx, chip in enumerate(displayed_chips):
        label = chip['label'][:max_text_length] if max_text_length else chip['label']
        if max_text_length and len(chip['label']) > max_text_length:
            label = label[:max_text_length - 1] + "…"  # Add ellipsis for exceeding text for available chips
        displayed_chips[idx]['label'] = label

    exceeding_text = None
    # Check if there are more chips than maxChipsDisplayed
    if max_chips_displayed and len(chips) > max_chips_displayed:
        exceeding_text = f"{len(chips) - max_chips_displayed} more items"

    return displayed_chips, exceeding_text
