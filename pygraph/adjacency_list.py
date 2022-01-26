from typing import Iterator, Tuple
from pygraph.graph import DuplicateEdge, HalfEdge, Loop, UnknownNode


class AdjacencyList:
    def __init__(self, adjacency: dict[int, list[int]]):
        for sid, tids in adjacency.items():
            for tid in tids:
                try:
                    sids = adjacency[tid]
                except KeyError:
                    raise UnknownNode

                if sid not in sids:
                    raise HalfEdge
                elif tids.count(tid) > 1:
                    raise DuplicateEdge
                elif tid == sid:
                    raise Loop

        self._adjacency = dict(adjacency)

    def __len__(self) -> int:
        return len(self._adjacency)

    def __contains__(self, id: int) -> bool:
        return id in self._adjacency

    def __iter__(self) -> Iterator[int]:
        return iter(self._adjacency.keys())

    def __repr__(self) -> str:
        return "AdjacencyList({})".format(self._adjacency)

    def iteredges(self) -> Iterator[Tuple[int, int]]:
        for sid, tids in self._adjacency.items():
            for tid in tids:
                if sid < tid:
                    yield (sid, tid)

    def iterneighbors(self, id: int) -> Iterator[int]:
        return iter(self._neighbors(id))

    def size(self) -> int:
        return sum(1 for _ in self.iteredges())

    def degree(self, id: int) -> int:
        return len(self._neighbors(id))

    def has_edge(self, sid: int, tid: int) -> bool:
        if tid not in self:
            raise UnknownNode

        return tid in self._neighbors(sid)

    def _neighbors(self, id: int) -> list[int]:
        try:
            result = self._adjacency[id]
        except KeyError:
            raise UnknownNode

        return result
