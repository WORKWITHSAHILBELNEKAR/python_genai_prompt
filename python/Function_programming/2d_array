def create_and_print_2d_array(rows, cols, elements):
    assert len(elements) == rows * cols, "Insufficient or extra elements provided"
    matrix = [elements[i * cols:(i + 1) * cols] for i in range(rows)]
    print("2D Array:")
    for row in matrix:
        print(" ".join(map(str, row)))


rows, cols = 2, 3
elements = [1, 2, 3, 4, 5, 6]
create_and_print_2d_array(rows, cols, elements)
