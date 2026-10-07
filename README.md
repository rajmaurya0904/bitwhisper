# Bitwhisper

Terminal tool that loads a binary file and finds headers or structures by field constraints (e.g. 'u32 length between 10 and 100 following magic PNG'), using a small declarative schema. For reverse engineers and file-format hackers.

## Installation

You can install Bitwhisper in the following ways:

### From source (editable mode)

For development, install the package in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

This installs the package and the optional `dev` dependencies (testing and linting tools).

### From source (production)

If you only want the runtime dependencies (currently none), you can install without the dev extras:

```bash
pip install -e .
```

### From PyPI (when available)

Once published, you can install from PyPI:

```bash
pip install bitwhisper
```

To get the development dependencies when installing from PyPI:

```bash
pip install "bitwhisper[dev]"
```

However, note that the package is not yet on PyPI, so the above may not work until the first release.

## Usage

## Schema format

Bitwhisper uses a small declarative schema to describe binary structures. A schema consists of an optional *magic* byte sequence that must appear at the start of the file, followed by an ordered list of fields. Each field has a name, a data type, and optional constraints that restrict the allowed values.

### Types

The supported primitive types are:

- `U8`, `U16`, `U32`, `U64` – unsigned integers of 8, 16, 32 and 64 bits.
- `I8`, `I16`, `I32`, `I64` – signed integers of 8, 16, 32 and 64 bits.
- `F32`, `F64` – IEEE‑754 floating point numbers (single and double precision).
- `Bytes` – raw byte sequence of a fixed length (specified via a `length` constraint).
- `String` – UTF‑8 encoded text (optionally constrained by a regular expression).

### Constraints

Constraints are optional and are used to filter values during a search. The most common constraints are:

- `min` / `max` – numeric lower and upper bounds.
- `length` – exact length for `Bytes` fields.
- `regex` – regular expression that a `String` field must match.

A constraint is represented by the :class:`~bitwhisper.schema.Constraint` class. Providing both `min` and `max` is allowed; providing only one is also valid. Supplying an invalid combination (e.g. `min` greater than `max`) raises a ``ValueError``.

### Example schema

```python
from bitwhisper.schema import Schema, Field, Type, Constraint

# PNG file header schema example
png_schema = Schema(
    magic=b"\x89PNG\r\n\x1a\n",
    fields=[
        Field("width",  Type.U32, [Constraint(min=1, max=10000)]),
        Field("height", Type.U32, [Constraint(min=1, max=10000)]),
        Field("bit_depth", Type.U8, [Constraint(min=1, max=8)]),
        Field("color_type", Type.U8, []),
    ],
)
```

In this example:

- The magic bytes ``\x89PNG\r\n\x1a\n`` identify a PNG file.
- The ``width`` and ``height`` fields are unsigned 32‑bit integers that must be between 1 and 10 000.
- ``bit_depth`` is an unsigned 8‑bit integer limited to the range 1‑8.
- ``color_type`` has no constraints and will match any ``U8`` value.

The schema can be passed to the Bitwhisper CLI or used programmatically to locate matching structures inside a binary blob.


TODO: fill in as the build loop lands the core feature.

## Example

TODO.

## FAQ

TODO.

## License

MIT -- see [LICENSE](LICENSE).