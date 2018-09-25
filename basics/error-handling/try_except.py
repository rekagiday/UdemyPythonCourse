def get_one(dict, key):
    try:
        return dict[key]
    except KeyError:
        return None
    else:
        print("Yay, its in the dict!")
    finally:
        print("We are done here.")
