import Factory


def test_factory():
    desired_shape = 'Square'
    attributes = {"side": 2}

    shape = Factory.ShapeFactory.create_shape(desired_shape, attributes)
    assert shape.__dict__ == {"side": 2}
