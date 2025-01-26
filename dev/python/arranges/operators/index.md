# Set operations

They try to be set-like, supporting most of the operations that the `set`
object does.

Actually, dunno how much of this I'm missing. Raise a ticket if there are
gaps.

| **Symbol** |       **Name**       |       **Code**       |
|:----------:|:--------------------:|:--------------------:|
| `A ⋂ B`    | intersection         | `A & B`              |
| `A ⋃ B`    | union                | `A | B`              |
| `A ⊆ B`    | subset               | `A <= B`             |
| `A ⊂ B`    | proper subset        | `A < B`              |
| `A ⊇ B`    | superset             | `A >= B`             |
| `A ⊃ B`    | proper superset      | `A > B`              |
| `A = B`    | equality             | `A == B`             |
| `A'`       | complement           | `~A`                 |
| `A \ B`    | relative complement  | `A - B`              |
| `A ∆ B`    | symmetric difference | `(A | B) - (A & B)`  |
| `a ∈ A`    | membership           | `a in A`             |
| `|A|`      | cardinality          | `len(A)`             |
| `Ø`        | empty set            | `Ranges("")`         |
| `ℕ0`       | natural numbers      | `Ranges(":")`        |
