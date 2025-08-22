# setup.py
from setuptools import setup, find_packages
from pathlib import Path

root = Path(__file__).parent
readme = (root / "README.md").read_text(encoding="utf-8")

setup(
    name="prime-polarity",
    version="0.2.0",
    description="Empirical polarity scoring (AUC/PI) for number-theoretic generators",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Contributors to prime-polarity",
    license="MIT",
    python_requires=">=3.9",

    # ---- src/ layout ----
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,

    # ---- runtime & dev deps ----
    install_requires=[
        "mpmath>=1.3.0",
        "numpy>=1.22",
    ],
    extras_require={
        "dev": [
            "pytest>=7",
            "ruff>=0.4",
            "black>=24.0",
        ],
    },

    # ---- console entry point ----
    entry_points={
        "console_scripts": [
            "prime-polarity=prime_polarity.cli:main",
        ]
    },

    # (optional) PyPI metadata niceties
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    keywords=["primes", "zeta", "AUC", "ROC", "analytics"],
)
