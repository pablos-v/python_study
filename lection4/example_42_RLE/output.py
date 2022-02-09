def output_data(result, adress):
    with open(adress, 'w') as file:
        file.write(result)