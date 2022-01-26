from typing import Iterator, Protocol, Tuple


class DuplicateNode(Exception):
    """Raised when building a graph with duplicate nodes."""


class DuplicateEdge(Exception):
    """Raised when building a graph with duplicate edges."""


class Loop(Exception):
    """Raised when building a graph with with a loop."""


class UnknownNode(Exception):
    """Raised when accessing a node whose id is not found."""


class HalfEdge(Exception):
    """Raised when building an adjacency-style graph without a back edge."""


class Graph(Protocol):
    """A graph that implements the Minimal Graph API.

    https://depth-first.com/articles/2020/01/06/a-minimal-graph-api/
    """

    def __len__(self) -> int:
        """Return the number of nodes in this graph."""
        ...

    def __contains__(self, id: int) -> bool:
        """Return True if this graph contains the node identified by `id`.

        Args:
            id (int): the node's identifier

        Returns:
            bool: True if the id was foundm, False otherwise
        """
        ...

    def __iter__(self) -> Iterator[int]:
        """Iterate the nodes of this graph."""
        ...

    def __repr__(self) -> str:
        """Return a debugging representation."""
        ...

    def iteredges(self) -> Iterator[Tuple[int, int]]:
        """Iterate the edges of this graph."""
        ...

    def size(self) -> int:
        """Return the number of edges."""
        ...

    def iterneighbors(self, id: int) -> Iterator[int]:
        """Iterate the neighbors of a node.

        Args:
            id (int): the node's identifier

        Yields:
            Iterator[int]: iterator over the neighbors of the node

        Raises:
            UnknownNode: if `id` was not found
        """
        ...

    def degree(self, id: int) -> int:
        """Return the number of neighbors connected to a node.

        Args:
            id (int): the node's identifier

        Returns:
            int: the number of neighbors connected to the node

        Raises:
            UnknownNode: if `id` was not found
        """
        ...

    def has_edge(self, sid: int, tid: int) -> bool:
        """Return True if an edge between the two indicated nodes exists.

        The return value of `has_edge(a, b)` should be identical to the
        return value of `has_edge(b, a)` for an undirected graph.

        Args:
            sid (int): the first node's id
            tid (int): the second nodes's id

        Returns:
            bool: True if an edge exists between the nodes, or False otherwise

        Raises:
            UnknownNode: if either `sid` or `tid` were not found
        """
        ...
