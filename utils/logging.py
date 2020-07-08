class Log:
    def e(self, tag, msg):
        print("[ %s ] ERROR: %s" % (tag, msg))
    def w(self, tag, msg):
        print("[ %s ] WARNING: %s" % (tag, msg))
    def i(self, tag, msg):
        print("[ %s ] INFO: %s" % (tag, msg))
    def d(self, tag, msg):
        print("[ %s ] DEBUG: %s" % (tag, msg))
    def v(self, tag, msg):
        print("[ %s ] VERBOSE: %s" % (tag, msg))
