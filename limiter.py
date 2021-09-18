
from datetime import datetime

clientUniqueId = "" # unique ID of the requestor
reqTime = datetime.now()
requestor.add(clientUniqueId, 0)
requestor.incrementReq(clientUniqueId) #requestor class keeping data of requestor ID and requests counts with date and time, localy on json

def limit_client_request(lim_per_sec, lim_per_min):
    
    ##limit based on argument passed
    if ((reqTime - requestor.getReqTime(clientUniqueId)).seconds < 1 and requestor.getReqCount(clientUniqueId) > lim_per_sec  ):
        return '😣 Page is quite busy, try again after some time'
    else:
        requestor.clearCount(clientUniqueId, reqTime)

    if (round((reqTime - recordedReqTime).seconds/60) < 1 and requestor.getReqCount(clientUniqueId) > lim_per_min  ):
        return '😣 Page is quite busy, try again after some time'
    else:
        requestor.clearCount(clientUniqueId, reqTime)

    requestor.setTime(clientUniqueId, reqTime)


