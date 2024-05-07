from veksle_penger_v2 import veksle_penger_v2


def test_veksle_penger_99():
    veksle_penger_v2(99) == (0, 0, 0, 0)


def test_veksle_penger_100():
    veksle_penger_v2(100) == (5, 0, 0, 0)


def test_veksle_penger_250():
    veksle_penger_v2(250) == (12, 1, 0, 0)


def test_veksle_penger_500():
    veksle_penger_v2(500) == (0, 0, 0, 0)


def test_veksle_penger_20():
    veksle_penger_v2(20) == (0, 0, 0, 0)


def test_veksle_penger_0():
    veksle_penger_v2(0) == (0, 0, 0, 0)


def test_veksle_penger_350():
    veksle_penger_v2(350) == (17, 1, 0, 0)


def test_veksle_penger_300():
    veksle_penger_v2(300) == (15, 0, 0, 0)


def test_veksle_penger_250():
    veksle_penger_v2(250) == (12, 1, 0, 0)


def test_veksle_penger_400():
    veksle_penger_v2(400) == (20, 0, 0, 0)


def test_veksle_penger_70():
    veksle_penger_v2(70) == (0, 0, 0, 0)


def kjør_alle():  # hadde visst ikke pytest installert. uheldig
    test_veksle_penger_0()
    test_veksle_penger_20()
    test_veksle_penger_100
    test_veksle_penger_250
    test_veksle_penger_500()
    test_veksle_penger_99


kjør_alle()
