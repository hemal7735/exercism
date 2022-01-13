def transform(legacy_data):
    data = {}

    for point in legacy_data:
        for letter in legacy_data[point]:
            data[letter.lower()] = point
    
    return data

