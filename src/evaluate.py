from ast_nodes import Signal, Constant, Diff, Cumsum, Eq, And, Or
import torch

def evaluate(node, ctx):

    if isinstance(node, Signal):
        return ctx[node.name]

    if isinstance(node, Constant):
        return node.value

    if isinstance(node, Diff):
        return torch.diff(evaluate(node.expr, ctx))

    if isinstance(node, Cumsum):
        return torch.cumsum(evaluate(node.expr, ctx), dim=0)

    if isinstance(node, Eq):
        return evaluate(node.left, ctx) == evaluate(node.right, ctx)

    if isinstance(node, And):
        return evaluate(node.left, ctx) & evaluate(node.right, ctx) # what do we want And to do?

    if isinstance(node, Or):
        return evaluate(node.left, ctx) | evaluate(node.right, ctx)
