[README.md](https://github.com/user-attachments/files/28725462/README.md)
# Signal Transform DSL

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Parser](https://img.shields.io/badge/parser-Lark-green.svg)
![DSL](https://img.shields.io/badge/domain-specific-language-orange.svg)
![Status](https://img.shields.io/badge/status-experimental-yellow.svg)

A lightweight **domain-specific language (DSL)** for defining and evaluating signal transformations over structured numeric data.

It provides a declarative syntax for expressing:
- statistical filters
- conditional aggregations
- composable signal functions

All compiled through a **grammar → AST → evaluation pipeline**.

---

## ✨ Example

### DSL

```dsl
stable(x) = std(x) < 5

t(y) = sum(y where stable(x))
```

### Equivalent Python-ish logic

```python
stable = lambda x: np.std(x) < 5
t = lambda x, y: y[stable(x)].sum()
```

---

## 🧠 Key Idea

Instead of writing imperative transformations over arrays, you define **signal relationships declaratively**:

```
signals → predicates → filtered aggregations → outputs
```

Think:

> "Define *what* a signal means, not *how* to compute it."

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A[DSL Source Code] --> B[Lark Parser]
    B --> C[Parse Tree]
    C --> D[Transformer]
    D --> E[AST Nodes]
    E --> F[Evaluator]
    F --> G[Computed Results]
```

---

## 📁 Project Structure

```
signal_transform/
│
├── dsl/
│   └── grammar.lark        # DSL grammar (Lark)
│
├── src/
│   ├── ast_nodes.py        # AST node definitions
│   ├── transformer.py      # Parse tree → AST
│   ├── evaluate.py         # AST execution engine
│
└── README.md
```

---

## 🧾 DSL Syntax

### 1. Signal Definitions

Define reusable predicates over signals:

```dsl
stable(x) = std(x) < 5
```

---

### 2. Conditional Aggregation

Filter before aggregation:

```dsl
mean(y where x > 0)
sum(y where stable(x))
```

---

### 3. Composition

Signals can depend on other signals:

```dsl
stable(x) = std(x) < 2
clean(x) = mean(x where stable(x))
```

---

### 4. Nested Expressions

```dsl
score(x, y) = mean(x where y > threshold)
```

---

## 🔄 Compilation Pipeline

### Step 1 — Parse DSL

Grammar defined in:

```
dsl/grammar.lark
```

Uses Lark to convert source into a parse tree.

---

### Step 2 — Build AST

Handled by:

```
src/transformer.py
```

---

### Step 3 — Evaluate AST

Handled by:

```
src/evaluate.py
```

Executes AST nodes using vectorized operations.

---

## 🧱 AST Design

Core node types:

| Node Type        | Purpose                          |
|------------------|----------------------------------|
| Signal           | Named signal reference           |
| Constant         | Numeric literal                  |
| BinaryOp         | Arithmetic / comparisons         |
| FunctionCall     | std, mean, sum, etc.            |
| WhereClause      | Filtering condition              |

---

## ⚙️ Execution Model

```
data → mask → transform → aggregate → output
```

Example:

```dsl
sum(y where x > 0)
```

becomes:

```python
mask = x > 0
result = y[mask].sum()
```

---

## 🧪 Python Usage

```python
from lark import Lark
from src.transformer import DSLTransformer
from src.evaluate import Evaluator

parser = Lark.open("dsl/grammar.lark", start="start")

dsl_code = """
stable(x) = std(x) < 5
t(y) = sum(y where stable(x))
"""

tree = parser.parse(dsl_code)
ast = DSLTransformer().transform(tree)

result = Evaluator().evaluate(ast, context={
    "x": x_array,
    "y": y_array
})

print(result)
```

---

## 🔍 Design Philosophy

- Compiler architecture for data transforms
- Signal-first composability
- Vectorized execution model

---

## 🚧 Future Work

- Window functions (rolling, lag, diff)
- JIT compilation to NumPy/JAX
- AST optimization passes
- Streaming execution
- Dependency graph engine

---

## 📦 Dependencies

- Python ≥ 3.10
- Lark parser

```bash
pip install lark
```

---

## 📜 License

MIT
