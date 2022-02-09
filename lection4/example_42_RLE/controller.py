import output as out
import input as inn
import split_and_encode as logic


def start_encode(file):
    input = inn.input_data(file)
    # input check!!!
    result = logic.encoder(input)
    out.output_data(result, '42_output_encoded.txt')

def start_decode(file):
    input = inn.input_data(file)
    # input check!!!
    result = logic.decoder(input)
    out.output_data(result, '42_output_decoded.txt')
