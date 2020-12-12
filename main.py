# ib_api_connection.py
import datetime

from IBAPI.ib_api_connection import IBAPIApp

if __name__ == '__main__':
    # Application parameters
    host = '127.0.0.1'  # Localhost, but change if TWS is running elsewhere
    port = 7497  # Change to the appropriate IB TWS account port number
    client_id = 1234

    print("Launching IB API application...")

    # Instantiate the IB API application
    app = IBAPIApp(host, port, client_id)

    print("Successfully launched IB API application...")

    # Obtain the server time via the IB API app
    server_time = app.obtain_server_time()
    server_time_readable = datetime.datetime.utcfromtimestamp(
        server_time
    ).strftime('%Y-%m-%d %H:%M:%S')

    print("Current IB server time: %s" % server_time_readable)

    # Disconnect from the IB server
    app.disconnect()

    print("Disconnected from the IB API application. Finished.")