import setuptools

setuptools.setup(
    name="maybeapple",
    version="0.0.0",
    package_data={},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],
    entry_points={
        'console_scripts': ['maybeapple = maybeapple.__main__:main'],
    },
    python_requires=">=3.6",
    install_requires=["argparse==1.4.0"],
)
