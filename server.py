from geemusic import app
from OpenSSL import SSL
import os


if __name__ == '__main__':
    context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
    context.use_privatekey_file('server.key')
    context.use_certificate_file('server.crt')

    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port, debug=True, ssl_context=context)
