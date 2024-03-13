def collapse_list_of_lists(list_of_lists: list[list[str]]):
    content = []
    for l in list_of_lists:
        content.append("\n".join(l))
    return "\n\n".join(content)