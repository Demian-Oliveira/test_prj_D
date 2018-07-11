import pkg_resources
from packageb.package_B import PackageB


class ProjectD(PackageB):
    def __init__(self):
        pass

    def print_version(self):
        super().print_version()
        try:
            version = pkg_resources.require("projectd")[0].version
            print('Project_D: {}'.format(version))
        except:
            print('=== Project_D ===')
