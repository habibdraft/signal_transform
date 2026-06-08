from dataclasses import dataclass

class Node:
    pass


@dataclass
class Signal(Node):
    name: str


@dataclass
class Constant(Node):
    value: float


@dataclass
class Diff(Node):
    expr: Node


@dataclass
class Cumsum(Node):
    expr: Node


@dataclass
class Eq(Node):
    left: Node
    right: Node


@dataclass
class And(Node):
    left: Node
    right: Node


@dataclass
class Or(Node):
    left: Node
    right: Node
