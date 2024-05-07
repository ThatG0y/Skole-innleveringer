from veksle_penger import veksle_penger


def test_veksle_penger_99():
    veksle_penger(99) == (4, 1, 1, 4)


def test_veksle_penger_3():
    veksle_penger(3) == (0, 0, 0, 3)


def test_veksle_penger_0():
    veksle_penger(0) == (0, 0, 0, 0)


def test_veksle_penger_500():
    veksle_penger(500) == (0, 0, 0, 0)


def test_veksle_penger_20():
    veksle_penger(20) == (1, 0, 0, 0)


def test_veksle_penger_41():
    veksle_penger(41) == (2, 0, 0, 2)


def kjør_alle():  # hadde visst ikke pytest installert. uheldig
    test_veksle_penger_0()
    test_veksle_penger_20()
    test_veksle_penger_3()
    test_veksle_penger_41()
    test_veksle_penger_500()
    test_veksle_penger_99


kjør_alle()
