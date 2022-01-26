import my_box


def generate_2D_int_list(m,n):
    return [[i+j for i in range(n)] for j in range(m)]

my_box.print_2D_list(generate_2D_int_list(3,3))