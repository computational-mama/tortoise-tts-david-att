import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TorToiSe",
    packages=setuptools.find_packages(),
    version="2.4.2",
    author="ambika",
    author_email="ambika@ajaibghar.com",
    description="A high quality multi-voice text-to-speech library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/computational-mama/tortoise-tts-david-att",
    project_urls={},
    scripts=[
        'scripts/tortoise_tts.py',
    ],
    include_package_data=True,
    install_requires=[
        'tqdm',
        'rotary_embedding_torch',
        'inflect',
        'progressbar',
        'einops',
        'unidecode',
        'scipy',
        'librosa',
        'transformers',
        'tokenizers',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
