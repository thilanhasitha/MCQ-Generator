from setuptools import setup,find_packages

setup(
    name='Mcq Generator',
    version = '0.0.1',
    author = 'thilan hasitha',
    author_email ='yasanjithbgth@gmail.com',
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages = find_packages()
)