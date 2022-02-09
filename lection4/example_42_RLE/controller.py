import output as out
import input as inn
import split_and_encode as logic


def start_encode():
    input = inn.input_data('42_input_decoded.txt')
    result = logic.encoder(input)
    out.output_data(result, '42_output_encoded.txt')