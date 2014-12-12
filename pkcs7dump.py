#!/usr/bin/python
#
# Read ASN.1/PEM PKCS#7 on stdin, parse it into plain text,
# then build substrate from it
#
from pyasn1_modules import rfc2315, pem
from pyasn1.codec.der import encoder, decoder
import sys
    
if len(sys.argv) != 1:
    print("""Usage:
$ cat pkcs7Certificate.pem | %s""" % sys.argv[0])
    sys.exit(-1)
    
data = sys.stdin.read()

contentInfo, rest = decoder.decode(data, asn1Spec=rfc2315.ContentInfo())

print(contentInfo.prettyPrint())

contentType = contentInfo.getComponentByName('contentType')

contentInfoMap = {
    (1, 2, 840, 113549, 1, 7, 1): rfc2315.Data(),
    (1, 2, 840, 113549, 1, 7, 2): rfc2315.SignedData(),
    (1, 2, 840, 113549, 1, 7, 3): rfc2315.EnvelopedData(),
    (1, 2, 840, 113549, 1, 7, 4): rfc2315.SignedAndEnvelopedData(),
    (1, 2, 840, 113549, 1, 7, 5): rfc2315.DigestedData(),
    (1, 2, 840, 113549, 1, 7, 6): rfc2315.EncryptedData()
    }

content, _ = decoder.decode(
    contentInfo.getComponentByName('content'),
    asn1Spec=contentInfoMap[contentType]
    )

print(content.prettyPrint())
