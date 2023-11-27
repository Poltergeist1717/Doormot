def load_properties_in_batches_of_forty():
    all_listed_properties = properties.objects.all()
    list_of_properties_in_batches = []
    listed_properties_length = len(all_listed_properties)
    y = 0
    k = 39
    length_of_current_batch = len(list_of_properties_in_batches)

    for property_object in all_listed_properties:
        try:
            if listed_properties_length != 0:
                current_property = all_listed_properties[y]
                list_of_properties_in_batches.append(current_property)
                y += 1

                if y == k:
                    y = k
                    k += 39

                    yield list_of_properties_in_batches
                    list_of_properties_in_batches = []

                elif length_of_current_batch < 40 and y == listed_properties_length:
                    k = 39
                    y = 0

                    yield list_of_properties_in_batches
                    list_of_properties_in_batches = []
            else:
                return None
        except Exception as e:
            raise Exception("An error occurred: " + str(e))