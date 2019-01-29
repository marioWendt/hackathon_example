from hackathon_example import greeting, parse_args, main
import pytest


def test_addit():
    assert result(3) == 6

def test_parse_args(argv, lang, name):
    args = parse_args(argv)
    assert args.name == name
    assert args.language == lang


def test_main(capsys):
    ret = main(["-l", "en", "John"])
    assert ret == 0
    captured = capsys.readouterr()
    assert captured[0] == "Hello, John!\n"  # stdout
    assert captured[1] == ""  # stderr
