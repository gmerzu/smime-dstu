from pyasn1.type.base import Asn1Item
from pyasn1.type.univ import namedtype, Sequence, ObjectIdentifier, Any

class MetaSchema(type):
    def __new__(cls, name, bases, attrs):
        fields = []
        for name in attrs.get('__order__', []):
            field = attrs.pop(name)
            if isinstance(field, Asn1Item):
                pass
            else:
                field = field()

            fields.append(namedtype.NamedType(name, field))

        attrs['componentType'] = namedtype.NamedTypes(*fields)
        return super(MetaSchema, cls).__new__(cls, name, bases + (object,), attrs)


class Schema(Sequence):
    __metaclass__ = MetaSchema

class Message(Schema):
    contentType = ObjectIdentifier
    content = Any

    __order__ = ['contentType', 'content']
