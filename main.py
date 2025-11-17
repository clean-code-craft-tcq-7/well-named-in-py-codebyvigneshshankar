from print_reference_manual import (form_reference_table, get_md_header,
                                    get_md_row)


def main():
    md_table = form_reference_table(
        header_formatter=get_md_header, row_formatter=get_md_row
    )
    print(md_table)


if __name__ == "__main__":
    main()
