from setuptools import setup

setup(
    name="electrum-bta-server",
    version="1.0",
    scripts=['run_electrum_bta_server','electrum-bta-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumbtaserver':'src'
        },
    py_modules=[
        'electrumbtaserver.__init__',
        'electrumbtaserver.utils',
        'electrumbtaserver.storage',
        'electrumbtaserver.deserialize',
        'electrumbtaserver.networks',
        'electrumbtaserver.blockchain_processor',
        'electrumbtaserver.server_processor',
        'electrumbtaserver.processor',
        'electrumbtaserver.version',
        'electrumbtaserver.ircthread',
        'electrumbtaserver.stratum_tcp',
        'electrumbtaserver.stratum_http'
    ],
    description="BataCoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/pooler/electrum-bta-server/",
    long_description="""Server for the Electrum Lightweight BataCoin Wallet"""
)


