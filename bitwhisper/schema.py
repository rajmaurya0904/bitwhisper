"""Declarative schema model for bitwhisper.

A :class:`Schema` describes a binary structure: an optional magic prefix and an
ordered list of :class:`Field` objects. Each field has a name, a :class:`Type`
and a list of :class:`Constraint` objects that the field's value must satisfy
for a match to be reported.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Type(Enum):
    """Supported primitive field types."""

    U8 = "u8"
    U16 = "u16"
    U32 = "u32"
    U64 = "u64"
    I8 = "i8"
    I16 = "i16"
    I32 = "i32"
    I64 = "i64"
    F32 = "f32"
    F64 = "f64"
    BYTES = "bytes"

    @property
    def size(self) -> int:
        """Size in bytes for fixed-size types, 0 for variable-size types."""
        return _TYPE_SIZES[self]


_TYPE_SIZES = {
    Type.U8: 1,
    Type.U16: 2,
    Type.U32: 4,
    Type.U64: 8,
    Type.I8: 1,
    Type.I16: 2,
    Type.I32: 4,
    Type.I64: 8,
    Type.F32: 4,
    Type.F64: 8,
    Type.BYTES: 0,
}


@dataclass
class Constraint:
    """A constraint that a field's value must satisfy."""

    min: int | None = None
    max: int | None = None

    def __post_init__(self) -> None:
        if self.min is not None and self.max is not None and self.min > self.max:
            raise ValueError("min cannot be greater than max")


@dataclass
class Field:
    """A field in a schema."""

    name: str
    type: Type
    constraints: list[Constraint] = field(default_factory=list)


@dataclass
class Schema:
    """A binary schema."""

    magic: bytes = b""
    fields: list[Field] = field(default_factory=list)

    def add_field(self, name: str, type: Type, constraints: list[Constraint] | None = None) -> None:
        """Add a field to the schema."""
        self.fields.append(Field(name, type, constraints or []))