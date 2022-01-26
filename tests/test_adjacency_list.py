import pytest

from pygraph.graph import DuplicateEdge, HalfEdge, Loop, UnknownNode
from pygraph.adjacency_list import AdjacencyList


class TestConstructor:
    def test_unknown_node(self):
        with pytest.raises(UnknownNode):
            AdjacencyList({0: [1]})

    def test_half_edge(self):
        with pytest.raises(HalfEdge):
            AdjacencyList({0: [1], 1: []})

    def test_duplicate_edge(self):
        with pytest.raises(DuplicateEdge):
            AdjacencyList({0: [1, 1], 1: [0]})

    def test_loop(self):
        with pytest.raises(Loop):
            AdjacencyList({0: [0]})


class TestLen:
    def test(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        assert len(graph) == 3


class TestContains:
    def test_unknown(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        assert 3 not in graph

    def test_known(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        assert 0 in graph


class TestIter:
    def test(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        assert list(graph) == [0, 1, 2]


class TestRepr:
    def test(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        assert repr(graph) == "AdjacencyList({0: [1], 1: [0, 2], 2: [1]})"


class TestIteredges:
    def test(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        assert list(graph.iteredges()) == [(0, 1), (1, 2)]


class TestIterneighbors:
    def test_unknown(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        with pytest.raises(UnknownNode):
            graph.iterneighbors(3)

    def test_known(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        assert list(graph.iterneighbors(1)) == [0, 2]


class TestSize:
    def test(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        assert graph.size() == 2


class TestDegree:
    def test_unknown(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        with pytest.raises(UnknownNode):
            graph.degree(3)

    def test_known(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        assert graph.degree(1) == 2


class TestHasEdge:
    def test_source_unknown(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        with pytest.raises(UnknownNode):
            graph.has_edge(3, 0)

    def test_target_unknown(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        with pytest.raises(UnknownNode):
            graph.has_edge(0, 3)

    def test_edge(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        assert graph.has_edge(0, 1)

    def test_reverse_edge(self):
        graph = AdjacencyList({0: [1], 1: [0, 2], 2: [1]})

        assert graph.has_edge(1, 0)
