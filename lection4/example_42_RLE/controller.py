


def main():
    input = input_data('42_input_decoded.txt')
    split = split_data(input)
    result = encrypter(split)
    output_data(result)