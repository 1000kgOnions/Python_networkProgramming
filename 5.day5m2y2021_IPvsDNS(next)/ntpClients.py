import ntplib
from time import ctime
#request
if __name__ =='__main__':
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    #tx_time
    print("Time: {}".format(ctime(response.tx_time)))
    #stratum
    print("Stratum: {}".format(response.stratum))
    #ref_time, offset
    print("reference time: {}".format(ctime(response.ref_time)))
    print("offset: {}".format(response.offset))
    #root_delay
    print("delay: {}".format(response.root_delay))