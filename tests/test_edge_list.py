import pytest

from pygraph.graph import DuplicateEdge, UnknownNode, Loop
from pygraph.edge_list import EdgeList


class TestConstructor:
    def test_duplicate_edge(self):
        with pytest.raises(DuplicateEdge):
            EdgeList([(0, 1), (0, 1)])

    def test_duplicate_edge_reversed(self):
        with pytest.raises(DuplicateEdge):
            EdgeList([(0, 1), (1, 0)])

    def test_loop(self):
        with pytest.raises(Loop):
            EdgeList([(0, 0)])


class TestLen:
    def test(self):
        graph = EdgeList([(0, 1), (1, 2)])

        assert len(graph) == 3


class TestContains:
    def test_known(self):
        graph = EdgeList([(0, 1)])

        assert 0 in graph

    def test_unknown(self):
        graph = EdgeList([(0, 1)])

        assert 2 not in graph


class TestIter:
    def test(self):
        graph = EdgeList([(0, 1), (1, 2)])

        assert list(graph) == [0, 1, 2]


class TestRepr:
    def test(self):
        graph = EdgeList([(0, 1), (1, 2)])

        assert repr(graph) == "EdgeList([(0, 1), (1, 2)])"


class TestIterEdges:
    def test(self):
        graph = EdgeList([(0, 1), (1, 2)])

        assert list(graph.iteredges()) == [(0, 1), (1, 2)]


class TestSize:
    def test(self):
        graph = EdgeList([(0, 1), (1, 2)])

        assert graph.size() == 2


class TestIterneighbors:
    def test_unknown(self):
        graph = EdgeList([(0, 1), (1, 2)])

        with pytest.raises(UnknownNode):
            graph.iterneighbors(3)

    def test_known(self):
        graph = EdgeList([(0, 1), (1, 2)])

        assert list(graph.iterneighbors(1)) == [0, 2]


class TestDegree:
    def test_unknown(self):
        graph = EdgeList([(0, 1), (1, 2)])

        with pytest.raises(UnknownNode):
            graph.degree(3)

    def test_known(self):
        graph = EdgeList([(0, 1), (1, 2)])

        assert graph.degree(1) == 2


class TestHasEdge:
    def test_source_unknown(self):
        graph = EdgeList([(0, 1), (1, 2)])

        with pytest.raises(UnknownNode):
            graph.has_edge(3, 0)

    def test_target_unknown(self):
        graph = EdgeList([(0, 1), (1, 2)])

        with pytest.raises(UnknownNode):
            graph.has_edge(0, 3)

    def test_edge(self):
        graph = EdgeList([(0, 1), (1, 2)])

        assert graph.has_edge(0, 1)

    def test_reverse_edge(self):
        graph = EdgeList([(0, 1), (1, 2)])

        assert graph.has_edge(1, 0)

    def test_non_edge(self):
        graph = EdgeList([(0, 1), (1, 2)])

        assert not graph.has_edge(0, 2)
