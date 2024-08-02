#!/usr/bin/env python3

print("Initial test success")


def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5
