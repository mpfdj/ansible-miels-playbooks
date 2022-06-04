#!/bin/bash
# https://matthewdavis111.com/certificates/self-signed-cert-for-local-dev/


# Variable to hold domain name, replace with desired domain
domain='miel.de.jaeger.nl'

# Create the certificate and private key
openssl req -x509 -out $domain.crt -keyout $domain.key \
  -newkey rsa:2048 -nodes -sha256  \
  -subj "/CN=$domain" -extensions EXT -config <( \printf "[dn]\nCN=$domain\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:$domain\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")

# Create pem
cat $domain.crt $domain.key >> $domain.pem