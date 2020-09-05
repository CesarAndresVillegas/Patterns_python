import Singleton


@Singleton.singleton
class HelperTest:
    pass


def test_singleton():
    element1 = HelperTest()
    element2 = HelperTest()

    assert element1 == element2
