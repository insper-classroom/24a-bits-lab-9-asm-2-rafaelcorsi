#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test
import os.path

import pytest
import yaml

try:
    from telemetry import telemetryMark

    pytestmark = telemetryMark()
except ImportError as err:
    print("Telemetry não importado")


def source(name):
    dir = os.path.dirname(__file__)
    src_dir = os.path.join(dir, ".")
    return os.path.join(src_dir, name)

@pytest.mark.telemetry_files(source("max.nasm"))
def test_max():
    ram = {0: 35, 1: 7}
    tst = {2: 35}
    assert nasm_test("max.nasm", ram, tst)

    ram = {0: 7, 1: 63}
    tst = {2: 63}
    assert nasm_test("max.nasm", ram, tst)

@pytest.mark.telemetry_files(source("abs.nasm"))
def test_abs():
    ram = {1: -1}
    tst = {0: 1}
    assert nasm_test("abs.nasm", ram, tst)

    ram = {1: 35}
    tst = {0: 35}
    assert nasm_test("abs.nasm", ram, tst)

@pytest.mark.telemetry_files(source("mult.nasm"))
def test_mult():
    ram = {0: 2, 1: 2}
    tst = {3: 4}
    assert nasm_test("mult.nasm", ram, tst)

    ram = {0: 32, 1: 16}
    tst = {3: 512}
    assert nasm_test("mult.nasm", ram, tst, 10000)

@pytest.mark.telemetry_files(source("div.nasm"))
def test_div():
    ram = {0: 0, 1: 5}
    tst = {2: 0}
    assert nasm_test("div.nasm", ram, tst)

    ram = {0: 4, 1: 2}
    tst = {2: 2}
    assert nasm_test("div.nasm", ram, tst)

    ram = {0: 30, 1: 5}
    tst = {2: 6}
    assert nasm_test("div.nasm", ram, tst, 10000)

    ram = {0: 46, 1: 5}
    tst = {2: 9}
    assert nasm_test("div.nasm", ram, tst, 10000)

    ram = {0: 1023, 1: 7}
    tst = {2: 146}
    assert nasm_test("div.nasm", ram, tst, 10000)
