FROM nginx:1.27.2

RUN bash -c 'openssl req -x509 -out localhost.crt -keyout localhost.key -newkey rsa:2048 -nodes -sha256 -subj "/CN=localhost" -extensions EXT -config <( printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth" )'
RUN bash -c 'openssl req -x509 -out web.crt -keyout web.key -newkey rsa:2048 -nodes -sha256 -subj "/CN=web" -extensions EXT -config <( printf "[dn]\nCN=web\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:web\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth" )'

COPY nginx.conf /etc/nginx/nginx.conf

