from pyasn1.codec.ber import encoder, decoder
from smime_dstu import Message

def test_file_encoding():
    raw = open('./signed1.r').read()
    data = decoder.decode(raw, asn1Spec=Message())
    msg = Message()
    msg['contentType'], msg['content']= data[0]
    assert encoder.encode(msg) == raw
