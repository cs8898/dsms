class Config:
    DSMS_PORT = 8080
    DSMS_VERSION = '0.0.1'
    DSMS_DEVELOPER = 'cs8898'
    DSMS_FILE = 'dsms.json'
    DSMS_TEXT = "________    _________   _____    _________\n" \
                "\______ \  /   _____/  /     \  /   _____/\n" + \
                " |    |  \ \_____  \  /  \ /  \ \_____  \\\n" + \
                " |    `   \/        \/    Y    \/        \\\n" + \
                "/_________/_________/_____|____/_________/\n" \
                " Dead      Simple    Monitoring Solution\n"

    HOSTS = []

    def set_config_file(self, args=None):
        if args is not None:
            if args.c is not "":
                self.DSMS_FILE = args.c

    def set_other_args(self, args=None):
        if args is not None:
            if args.p is not -1:
                self.DSMS_PORT = args.p

    def set_hosts(self, hosts=None):
        if hosts is not None:
            self.HOSTS = hosts


config = Config()
