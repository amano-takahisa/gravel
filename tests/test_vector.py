from gravel import Vector


class TestVector:
    def test_vector(self):
        vector = Vector()
        assert hasattr(vector, 'to_gdf')

