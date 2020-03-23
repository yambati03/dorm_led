class Log:
    def e(tag, msg):
        print("[ %s ] ERROR: %s" % (tag, msg))
    def w(tag, msg):
        print("[ %s ] WARNING: %s" % (tag, msg))
    def i(tag, msg):
        print("[ %s ] INFO: %s" % (tag, msg))
    def d(tag, msg):
        print("[ %s ] DEBUG: %s" % (tag, msg))
    def v(tag, msg):
        print("[ %s ] VERBOSE: %s" % (tag, msg))
