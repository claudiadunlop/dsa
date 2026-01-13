"""Tests for HashMap implementation."""

import pytest
from dsa.maps.hash_map import HashMap


class TestHashMap:
    """Tests for the HashMap class."""

    def test_new_map_is_empty(self):
        m = HashMap()
        assert m.is_empty()
        assert len(m) == 0

    def test_setitem_getitem(self):
        m = HashMap()
        m["key"] = "value"
        assert m["key"] == "value"

    def test_setitem_updates_existing(self):
        m = HashMap()
        m["key"] = "value1"
        m["key"] = "value2"
        assert m["key"] == "value2"
        assert len(m) == 1

    def test_getitem_missing_raises(self):
        m = HashMap()
        with pytest.raises(KeyError):
            _ = m["missing"]

    def test_delitem(self):
        m = HashMap()
        m["key"] = "value"
        del m["key"]
        assert "key" not in m
        assert len(m) == 0

    def test_delitem_missing_raises(self):
        m = HashMap()
        with pytest.raises(KeyError):
            del m["missing"]

    def test_contains(self):
        m = HashMap()
        m["key"] = "value"
        assert "key" in m
        assert "other" not in m

    def test_len(self):
        m = HashMap()
        assert len(m) == 0
        m["a"] = 1
        assert len(m) == 1
        m["b"] = 2
        assert len(m) == 2
        del m["a"]
        assert len(m) == 1

    def test_get_with_default(self):
        m = HashMap()
        m["key"] = "value"
        assert m.get("key") == "value"
        assert m.get("missing") is None
        assert m.get("missing", "default") == "default"

    def test_iteration(self):
        m = HashMap()
        m["a"] = 1
        m["b"] = 2
        m["c"] = 3
        keys = set(m)
        assert keys == {"a", "b", "c"}

    def test_keys_values_items(self):
        m = HashMap()
        m["a"] = 1
        m["b"] = 2
        assert set(m.keys()) == {"a", "b"}
        assert set(m.values()) == {1, 2}
        assert set(m.items()) == {("a", 1), ("b", 2)}

    def test_many_items(self):
        m = HashMap()
        for i in range(100):
            m[str(i)] = i
        assert len(m) == 100
        for i in range(100):
            assert m[str(i)] == i

    def test_integer_keys(self):
        m = HashMap()
        m[1] = "one"
        m[2] = "two"
        assert m[1] == "one"
        assert m[2] == "two"

    def test_collision_handling(self):
        """Test that collisions are handled correctly."""
        m = HashMap(capacity=3)  # Small capacity to force collisions
        m["a"] = 1
        m["b"] = 2
        m["c"] = 3
        m["d"] = 4
        m["e"] = 5
        assert len(m) == 5
        assert m["a"] == 1
        assert m["e"] == 5
