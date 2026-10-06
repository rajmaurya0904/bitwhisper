import pytest

from bitwhisper.schema import Constraint, Field, Schema, Type


def test_schema_creation():
    """Test that a schema can be created with magic and fields."""
    magic = b'\x89PNG\r\n\x1a\n'
    fields = [
        Field('width', Type.U32, [Constraint(min=1, max=10000)]),
        Field('height', Type.U32, [Constraint(min=1, max=10000)]),
    ]
    schema = Schema(magic=magic, fields=fields)
    assert schema.magic == magic
    assert schema.fields == fields

def test_schema_without_magic():
    """Test that a schema can be created without magic bytes."""
    fields = [Field('length', Type.U32, [])]
    schema = Schema(fields=fields)
    assert schema.magic == b""  # default is empty bytes
    assert schema.fields == fields

def test_invalid_type_raises():
    """Test that creating a Type with invalid string raises ValueError."""
    with pytest.raises(ValueError):
        Type('invalid_type')

def test_constraint_validation():
    """Test that constraints are validated correctly."""
    # Valid constraint with min only
    c1 = Constraint(min=0)
    assert c1.min == 0
    assert c1.max is None
    # Valid constraint with max only
    c2 = Constraint(max=10)
    assert c2.max == 10
    assert c2.min is None
    # Valid constraint with both
    c3 = Constraint(min=5, max=15)
    assert c3.min == 5
    assert c3.max == 15
    # Invalid constraint: min > max should raise ValueError
    with pytest.raises(ValueError):
        Constraint(min=20, max=10)

def test_schema_repr():
    """Test that schema has a reasonable representation."""
    magic = b'\\x89PNG'
    fields = [Field('width', Type.U32, [])]
    schema = Schema(magic=magic, fields=fields)
    repr_str = repr(schema)
    assert 'Schema' in repr_str
    assert 'width' in repr_str

def test_add_field():
    """Test that fields can be added via add_field method."""
    schema = Schema()
    schema.add_field('test_field', Type.U16, [Constraint(min=0, max=100)])
    assert len(schema.fields) == 1
    field = schema.fields[0]
    assert field.name == 'test_field'
    assert field.type == Type.U16
    assert len(field.constraints) == 1
    assert field.constraints[0].min == 0
    assert field.constraints[0].max == 100