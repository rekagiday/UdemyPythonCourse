def get_one(dict, key):
    try:
        return dict[key]
    except KeyError:
        return None
