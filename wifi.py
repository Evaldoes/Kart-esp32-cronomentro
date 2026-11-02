def connect():
    import network
    from config import WIFI_SSID as ssid, WIFI_PASSWORD as password
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("Already connected")
        return

    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
        pass
    print("Connection successful")
