from constants import MAJOR_COLORS, MINOR_COLORS


def color_index_pair_number(major_color_index, minor_color_index):
    return major_color_index * 5 + minor_color_index + 1


def get_md_header():
    return "| Pair Number | Major Color | Minor Color |\n| --- | --- | --- |\n"


def get_md_row(pair_num, major_color, minor_color):
    return f"| {pair_num} | {major_color} | {minor_color} |\n"


def get_csv_header():
    return "Pair Number,Major Color,Minor Color\n"


def get_csv_row(pair_num, major_color, minor_color):
    return f"{pair_num},{major_color},{minor_color}\n"


def form_reference_table(header_formatter, row_formatter):
    table_string = header_formatter()
    for i, major in enumerate(MAJOR_COLORS):
        for j, minor in enumerate(MINOR_COLORS):
            table_string += row_formatter(color_index_pair_number(i, j), major, minor)
    return table_string
