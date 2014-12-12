from pyasn1.type.univ import namedtype, Sequence, ObjectIdentifier, Any

class Message(Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('type', ObjectIdentifier()),
        namedtype.NamedType('body', Any())
    )

