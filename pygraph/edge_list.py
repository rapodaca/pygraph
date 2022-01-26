from typing import Iterator, Tuple
from pygraph.graph import DuplicateEdge, Loop, UnknownNode


class EdgeList:
    def __init__(self, edges: list[Tuple[int, int]]):
        seen = set()

        for (sid, tid) in edges:
            if (sid, tid) in seen or (tid, sid) in seen:
                raise DuplicateEdge
            elif sid == tid:
                raise Loop

            seen.add((sid, tid))

        self._edges = list(edges)

    def __len__(self) -> int:
        return sum(1 for _ in self._nodes())

    def __contains__(self, id: int) -> bool:
        for sid, tid in self._edges:
            if id == sid or id == tid:
                return True
        else:
            return False

    def __iter__(self) -> Iterator[int]:
        return iter(self._nodes())

    def __repr__(self) -> str:
        return "EdgeList({})".format(self._edges)

    def iteredges(self) -> Iterator[Tuple[int, int]]:
        return iter(self._edges)

    def size(self) -> int:
        return len(self._edges)

    def iterneighbors(self, id: int) -> Iterator[int]:
        return iter(self._neighbors(id))

    def degree(self, id: int) -> int:
        return sum(1 for _ in self._neighbors(id))

    def has_edge(self, sid: int, tid: int) -> bool:
        if sid not in self or tid not in self:
            raise UnknownNode

        for edge in self._edges:
            if edge[0] == sid and edge[1] == tid:
                return True
            elif edge[1] == sid and edge[0] == tid:
                return True
        else:
            return False

    def _neighbors(self, id: int) -> Iterator[int]:
        if id not in self:
            raise UnknownNode
        else:
            return self._mates(id)

    def _mates(self, id: int) -> Iterator[int]:
        for sid, tid in self._edges:
            if id == sid:
                yield tid
            elif id == tid:
                yield sid

    def _nodes(self) -> Iterator[int]:
        seen = set()

        for sid, tid in self._edges:
            if sid not in seen:
                seen.add(sid)

                yield sid

            if tid not in seen:
                seen.add(tid)

                yield tid
