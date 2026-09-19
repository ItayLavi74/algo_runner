from dataclasses import dataclass
from enum import Enum
from algorithms import *
from typing import Callable

# this file contain data of all algorithms available for other files to import and accses
"""
properties list: needStartNode: bool
                 edgeSignAssump: int (-1, 0, 1)


"""


def get_algorithm_function(algorithm: str):
    match algorithm:
        case 'dijkstra': return dijkstra

    print("unable to find algorithm in 'get_algorithm_function'")


class EdgeSign(Enum):
    NON_ZERO = 2
    POSITIVE_ONLY = 1
    NON_NEGATIVE = 0
    ANY = -1


@dataclass
class AlgorithmInfo:
    function: Callable
    need_start_node: bool
    edge_sign_assump: EdgeSign


dijkstra_info = AlgorithmInfo(function=dijkstra,
                              need_start_node=True,
                              edge_sign_assump=EdgeSign.NON_NEGATIVE)
