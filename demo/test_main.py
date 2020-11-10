import importlib


def test_import():
    ff = importlib.import_module("fun")
    getattr(ff, "a")()


def test_getimport():
    mod = "fun.a"
    strs = mod.split('.')
    for str in strs[:len(strs) - 1]:
        im = importlib.import_module(str)
        if hasattr(im, strs[-1]):
            getattr(im, strs[-1])()


def test_getvalue():
    globals()["value"] = 123
    print(eval("value"))
