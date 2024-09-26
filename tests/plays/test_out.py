from baseball_scorecard.plays.out import Out

out_play = "U3"
strikeout_looking = "!K"


def test_out_get_metapost_data_labels():
    """Test that the generated metapost data for labeled outs is correct."""

    expected_label = (
        f"    label(btex {{\\bigsf {out_play}}} etex, outlabel) withcolor outclr;\n"
    )

    # Test first out
    expected_output = expected_label + "    draw_out_one(xstart,ystart,clr);\n"
    out = Out(out_play, 1)
    assert out.get_metapost_data() == expected_output

    # Test second out
    expected_output = expected_label + "    draw_out_two(xstart,ystart,clr);\n"
    out = Out(out_play, 2)
    assert out.get_metapost_data() == expected_output

    # Test third out
    expected_output = expected_label + "    draw_out_three(xstart,ystart,clr);\n"
    out = Out(out_play, 3)
    assert out.get_metapost_data() == expected_output


def test_out_get_metapost_data_strikeout_looking():
    """Test that the generated metapost data for strikeout looking outs is correct."""

    expected_label = "    draw_strikeout_looking(outlabel, outclr);\n"

    # Test first out
    expected_output = expected_label + "    draw_out_one(xstart,ystart,clr);\n"
    out = Out(strikeout_looking, 1)
    assert out.get_metapost_data() == expected_output

    # Test second out
    expected_output = expected_label + "    draw_out_two(xstart,ystart,clr);\n"
    out = Out(strikeout_looking, 2)
    assert out.get_metapost_data() == expected_output

    # Test third out
    expected_output = expected_label + "    draw_out_three(xstart,ystart,clr);\n"
    out = Out(strikeout_looking, 3)
    assert out.get_metapost_data() == expected_output


def test_out_string_output():
    """Test that the string method for the Out class is printing the expected format."""
    out = Out(out_play, 1)
    assert str(out) == "Out #1: U3"
