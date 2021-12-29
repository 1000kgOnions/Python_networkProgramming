# lookup(dia chi ip) -> country,continent,timezone
from geoip import geolite2
import socket
if __name__ == "__main__":
    hostname = 'www.vnexpress.net'
    ip_addr = socket.gethostbyname(hostname)
    match = geolite2.lookup(ip_addr)
    if match is not None:
        print("Country: ", match.country)
        print("Timezone: ", match.timezone)
        print("continent: ", match.continent)
