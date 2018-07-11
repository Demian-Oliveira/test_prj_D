from setuptools import setup, find_packages


def install_deps():
    """Reads requirements.txt and preprocess it
    to be feed into setuptools.

    This is the only possible way (we found)
    how requirements.txt can be reused in setup.py
    using dependencies from private github repositories.

    Links must be appendend by `-{StringWithAtLeastOneNumber}`
    or something like that, so e.g. `-9231` works as well as
    `1.1.0`. This is ignored by the setuptools, but has to be there.

    Warnings:
        to make pip respect the links, you have to use
        `--process-dependency-links` switch. So e.g.:
        `pip install --process-dependency-links {git-url}`

    Returns:
         list of packages and dependency links.
    """
    default = open('requirements.txt', 'r').readlines()
    new_pkgs = []
    links = []
    for resource in default:
        if 'git+ssh' in resource or 'git+https' in resource:
            pkg = resource.split('#')[-1]
            links.append(resource.strip() + '-9876543210')
            new_pkgs.append(pkg.replace('egg=', '').rstrip())
        else:
            new_pkgs.append(resource.strip())
    return new_pkgs, links

pkgs, new_links = install_deps()

# pip install -vvv git+https://github.com/dmyanster/test_prj_D --process-dependency-links

setup(
    # Needed to silence warnings
    name='ProjectD',
    url='https://github.com/dmyanster/test_prj_D',
    author='Dmyan',
    author_email='dmyan@qwerty.com',
    # Needed to actually package something
    packages=['projectd'],

    install_requires=pkgs,
    dependency_links=new_links,

    # # # Needed for dependencies
    # install_requires=['PackageB'],
    # dependency_links=[
    #     # # 'git+https://github.com/dmyanster/test_pkg_A.git@v{}#egg=PackageA.egg-info'.format('0.0.4'),
    #     # # 'git+https://github.com/dmyanster/test_pkg_B.git@v{}#egg=PackageB.egg-info'.format('0.0.1'),
    #     # 'https://github.com/dmyanster/test_pkg_A.git@v{}#egg=PackageA.egg-info'.format('0.0.4'),
    #     # 'https://github.com/dmyanster/test_pkg_B.git@v{}#egg=PackageB.egg-info'.format('0.0.1'),
    #
    #     'https://github.com/dmyanster/test_pkg_A/archive/v{}.zip#egg=PackageA.egg-info'.format('0.0.4'),
    #     'https://github.com/dmyanster/test_pkg_B/archive/v{}.zip#egg=PackageB.egg-info'.format('0.0.1'),
    # ],

    # *strongly* suggested for sharing
    version='0.0.1',

    license='private test code',
    description='any description',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.rst').read(),
    # # if there are any scripts
    # ~/anaconda3/envs/design2.0-v0.2/bin
    # ~/anaconda3/bin
    scripts=['bin/start', 'scripts/start.py'],
)

# # Limpando tudo
# # cd /Users/demianoliveira/anaconda3/lib/python3.6/site-packages
#
# cd ~/PycharmProjects/envs
# source deactivate
# rm -rf env-ProjectD
#
# # Creating enviroment and installing
#
# cd ~/PycharmProjects/envs
# python -m venv env-ProjectD
# source activate env-ProjectD
# pip install git+https://github.com/dmyanster/test_prj_D --process-dependency-links
#
#
# # Updating
# pip install git+https://github.com/dmyanster/test_prj_D --process-dependency-links --upgrade
