from setuptools import setup


if __name__ == '__main__':
    setup(
        name="hdrpy",
        version="0.1",
        description="HDR histogram implementation based on numpy",
        author="Dmitri Pribysh",
        autor_email="dmand@yandex.ru",
        url="https://github.com/dmand/hdrpy",
        license='Apache 2.0',
        platform='any',

        packages=["hdrpy"],
        install_requires=['numpy>=1.14.0'],
        keywords=['hdrpy', 'hdr', 'histogram', 'high dynamic range'],
        classifiers=[
            "Intended Audience :: Developers",
            "Intended Audience :: Information Technology",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: POSIX :: Linux",
            "Operating System :: MacOS",
            "Operating System :: Microsoft :: Windows",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
        ],
    )

