def filter_dump(filename, objects, typename):
    import pickle
    new_obj = list(filter(lambda x: isinstance(x, typename), objects))
    with open(filename, 'wb') as file:
        pickle.dump(new_obj, file)

