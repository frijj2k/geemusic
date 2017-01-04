from geemusic import app
import ssl
import os


if __name__ == '__main__':

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('server.crt', 'server.key')

    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port, debug=True, ssl_context=context)
