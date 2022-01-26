from typing import Iterator, Tuple
from pygraph.graph import HalfEdge, Loop, UnknownNode


class Hybrid:
    def __init__(self, adjacency: dict[int, list[int]]):
        self._edges = []

        for sid, tids in adjacency.items():
            for tid in tids:
                try:
                    sids = adjacency[tid]
                except KeyError:
                    raise UnknownNode

                if sid not in sids:
                    raise HalfEdge
                elif sid == tid:
                    raise Loop
                elif sid < tid:
                    self._edges.append((sid, tid))

        self._adjacency = dict(adjacency)

    def __len__(self) -> int:
        return len(self._adjacency)

    def __contains__(self, id: int) -> bool:
        return id in self._adjacency

    def __iter__(self) -> Iterator[int]:
        return iter(self._adjacency.keys())

    def __repr__(self) -> str:
        return "Hybrid({})".format(self._adjacency)

    def iteredges(self) -> Iterator[Tuple[int, int]]:
        return iter(self._edges)

    def size(self) -> int:
        return len(self._edges)

    def iterneighbors(self, id: int) -> Iterator[int]:
        return iter(self._neighbors(id))

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
