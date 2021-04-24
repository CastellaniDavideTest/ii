from setuptools import setup, find_packages
from requests import get

setup(
      name='iicd',
      version=get("https://api.github.com/repos/CastellaniDavide/ii/tags").json()[0]['name'].replace("v", ""), # Lastest release
      description=get("https://api.github.com/repos/CastellaniDavide/ii").json()['description'],
      long_description=get("https://raw.githubusercontent.com/CastellaniDavide/ii/main/docs/README.md").text,
      long_description_content_type="text/markdown",
      url=get("https://api.github.com/repos/CastellaniDavide/ii").json()['html_url'],
      author=get("https://api.github.com/repos/CastellaniDavide/ii").json()['owner']['login'],
      author_email=get(f"https://api.github.com/users/{get('https://api.github.com/repos/CastellaniDavide/ii').json()['owner']['login']}").json()['email'],
      license='GNU',
      packages=find_packages(),
      python_requires=">=3.6",
      platforms="linux_distibution",
      install_requires=[i for i in get("https://raw.githubusercontent.com/CastellaniDavide/ii/main/requirements/requirements.txt").text.split("\n") if not "#" in i and i != ''],
      zip_safe=True
      )
