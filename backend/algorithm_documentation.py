from dataclasses import dataclass, field


@dataclass
class AlgorithmResult:
    algorithm: str
    steps: list = field(default_factory=list)
    result: list = field(default_factory=dict)


@dataclass
class AlgorithmStep:
    action: str
    explanation: str
    state: dict = field(default_factory=dict)
