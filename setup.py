from setuptools import setup, find_packages

setup(
    name="cex",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask==3.0.2",
        "python-binance==1.0.19",
        "python-dotenv==1.0.1",
        "SQLAlchemy==2.0.27",
        "psycopg2-binary==2.9.9"
    ],
) 