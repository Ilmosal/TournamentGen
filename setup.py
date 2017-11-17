from setuptools import setup, find_packages

setup(
	name="TournamentGen",
	version="0.1.11",
	author="Ilmo Salmenperä",
	author_email="ilmo.salmenperä@helsinki.fi",
	packages=find_packages(),
	include_package_data=True,
	url="http://github.com/MrCubanfrog/TournamentGen",
	license="LICENSE",
	description="A Program for generating tournament brackets",
	install_requires=[
	],
	long_description=open("README.md").read(),
	entry_points='''
		[console_scripts]
		tournamentgen=tournamentgen.bin.TournamentGen:run
	''',
)
