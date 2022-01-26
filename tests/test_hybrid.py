import pytest
from pygraph.hybrid import Hybrid

from pygraph.graph import HalfEdge, Loop, UnknownNode


class TestConstructor:
    def test_unknown_node(self):
        with pytest.raises(UnknownNode):
            Hybrid({0: [1]})

    def test_half_edge(self):
        with pytest.raises(HalfEdge):
            Hybrid({0: [1], 1: []})

    def test_loop(self):
        with pytest.raises(Loop):
            Hybrid({0: [0]})


class TestLen:
    def test(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        assert len(graph) == 3


class TestContains:
    def test_unknown(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        assert 3 not in graph

    def test_known(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        assert 0 in graph


class TestIter:
    def test(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        assert list(graph) == [0, 1, 2]


class TestRepr:
    def test(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        assert repr(graph) == "Hybrid({0: [1], 1: [0, 2], 2: [1]})"


class TestIteredges:
    def test(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        assert list(graph.iteredges()) == [(0, 1), (1, 2)]


class TestIterneighbors:
    def test_unknown(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        with pytest.raises(UnknownNode):
            graph.iterneighbors(3)

    def test_known(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        assert list(graph.iterneighbors(1)) == [0, 2]


class TestSize:
    def test(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        assert graph.size() == 2


class TestDegree:
    def test_unknown(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        with pytest.raises(UnknownNode):
            graph.degree(3)

    def test_known(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        assert graph.degree(1) == 2


class TestHasEdge:
    def test_source_unknown(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        with pytest.raises(UnknownNode):
            graph.has_edge(3, 0)

    def test_target_unknown(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        with pytest.raises(UnknownNode):
            graph.has_edge(0, 3)

    def test_edge(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        assert graph.has_edge(0, 1)

    def test_reverse_edge(self):
        graph = Hybrid({0: [1], 1: [0, 2], 2: [1]})

        assert graph.has_edge(1, 0)
