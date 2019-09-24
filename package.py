from Jumpscale import j

class Package(j.baseclasses.threebot_package):
    """
    to start need to run 
    kosmos -p "j.tools.threebot_packages.get('faircoffe_trade',giturl='https://github.com/faircoffee-trade/www_faircoffe_trade.git',branch='production')"
    kosmos -p "j.servers.threebot.default.start(web=True, ssl=False)"
    """
    def _init(self, **kwargs):
        self.branch = kwargs["package"].branch or "master"
        self.faircoffe_trade = "https://github.com/faircoffee-trade/www_faircoffe_trade.git"

    def prepare(self):
        """
        called when the 3bot starts
        :return:
        """
        server = self.openresty
        server.install(reset=True)
        server.configure()
        website = server.websites.get("faircoffe_trade")
        website.ssl = False
        website.port = 80
        locations = website.locations.get("faircoffe_trade")
        static_location = locations.locations_static.new()
        static_location.name = "static"
        static_location.path_url = "/"
        path = j.clients.git.getContentPathFromURLorPath(self.faircoffe_trade, branch=self.branch, pull=True)
        static_location.path_location = path
        static_location.use_jumpscale_weblibs = True
        website.path = path
        locations.configure()
        website.configure()

    def start(self):
        """
        called when the 3bot starts
        :return:
        """
        self.prepare()
    def stop(self):
        """
        called when the 3bot stops
        :return:
        """
        pass

    def uninstall(self):
        """
        called when the package is no longer needed and will be removed from the threebot
        :return:
        """
        pas
