def deleteService(msg):
    def helper_callback(reply_msg):
        # is msg valid or not?
        msg.reply(reply_msg)
    payload = msg.body["payload"]
    deleteService_helper(payload, helper_callback)

def deleteService_helper(payload, callback):
    callback(sth)

python: functools.partial(func[,*args][, **keywords]) 
Return a new partial object which when called will behave like func called with the positional arguments args and keyword arguments keywords. If more arguments are supplied to the call, they are appended to args. If additional keyword arguments are supplied, they extend and override keywords.