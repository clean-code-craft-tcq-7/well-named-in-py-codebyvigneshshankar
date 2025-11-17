import pytest

from constants import MAJOR_COLORS, MINOR_COLORS
from print_reference_manual import (color_index_pair_number, get_csv_header,
                                    get_csv_row, get_md_header, get_md_row)


def test_color_index_pair_number():
    assert color_index_pair_number(0, 0) == 1
    assert color_index_pair_number(4, 4) == 25

def test_get_md_header():
    md_header = get_md_header()
    assert ("| Pair Number | Major Color | Minor Color |\n| --- | --- | --- |\n" in md_header)

def test_get_md_row():
    md_row = get_md_row(1, MAJOR_COLORS[1], MINOR_COLORS[1])
    assert f"| 1 | {MAJOR_COLORS[1]} | {MINOR_COLORS[1]} |\n" in md_row

def test_get_csv_header():
    csv_header = get_csv_header()
    assert "Pair Number,Major Color,Minor Color\n" in csv_header

def test_get_csv_row():
    csv_row = get_csv_row(1, MAJOR_COLORS[1], MINOR_COLORS[1])
    assert f"1,{MAJOR_COLORS[1]},{MINOR_COLORS[1]}\n" in csv_row

if __name__ == "__main__":  # pragma: no cover
    pytest.main([__file__, "-v"])
