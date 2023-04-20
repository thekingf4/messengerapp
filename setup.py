# -*- coding: utf-8 -*-


import setuptools

setuptools.setup(
    name="messenger_tab",
    version="0.1",
    license="MIT",
    description="gwchat Open edX course_tab",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Platform :: Open edX",
        "Natural Language :: English",
        "Environment :: Web Environment",
    ],
    entry_points={
        "lms.djangoapp": [
            "messenger_tab = messenger_tab.apps:MessengerAppConfig",
        ],
        "openedx.course_tab": [
            "messenger_tab = messenger_tab.plugins:MessengerAppTab",
        ]
    },
)
