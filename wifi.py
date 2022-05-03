def connect():
    import network
    # ssid = "Cardosal"
    ssid = "wifi-zone-ufam-1"
    password = ""
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("Already connected")
        return

    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
        pass
    print("Connection successful")
