from setuptools import Extension, setup, Command, find_packages

VERSION = '0.1'

setup (
    name = 'boxing',
    version = VERSION,
    description = 'A waveform plugin for PyCBC',
    author = 'Yifan Wang',
    author_email = 'yifan.wang@aei.mpg.de',
    url = 'https://github.com/yi-fan-wang/boxing',
    keywords = ['gravitational waves', 'pycbc'],
    packages = find_packages(),
    entry_points = {"pycbc.waveform.td":[
                        "IMRPhenomTPHM_J = boxing.genwave:gen_imrphenomtphmj",
                       ],
                    },
    python_requires='>=3.8',
    install_requires=[
        'pycbc',
        'numpy',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)