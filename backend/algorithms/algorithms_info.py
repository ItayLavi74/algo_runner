from enum import Enum

# this file contain data of all algorithms available for other files to import and accses
"""
properties list: needStartNode: bool
                 edgeSignAssump: int (-1, 0, 1)


"""


class EdgeSign(Enum):
    NON_ZERO = 2
    POSITIVE_ONLY = 1
    NON_NEGATIVE = 0
    ANY = -1


# algorithm assumtions constructor
class AlgorithmInfo():
    def __init__(self, *, need_start_node=False, edge_sign_assump=EdgeSign.ANY):
        self.need_start_node = need_start_node
        self.edge_sign_assump = edge_sign_assump


dijkstra = AlgorithmInfo(need_start_node=True,
                         edge_sign_assump=EdgeSign.NON_NEGATIVE)
