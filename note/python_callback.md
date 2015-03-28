def deleteService(msg):
    def helper_callback(reply_msg):
        # is msg valid or not?
        msg.reply(reply_msg)
    payload = msg.body["payload"]
    deleteService_helper(payload, helper_callback)

def deleteService_helper(payload, callback):
    callback(sth)