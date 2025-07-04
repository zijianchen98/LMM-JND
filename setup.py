from setuptools import setup, find_packages

setup(
    name="lmm-jnd",
    version="0.0.1",
    packages=find_packages(where='lmm-jnd'),
    author="Zijian Chen",
    author_email="zijian.chen@sjtu.edu.com",
    description="Large Multimodal Model Just Noticeable Difference",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zijianchen98/LMM-JND",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License", 
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)