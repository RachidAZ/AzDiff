pip install wheel
#Build
python3 setup.py bdist_wheel --version {__version__}

#install twine
pip install twine
# create file $HOME/.pypirc with pypip creds then release
python3 -m twine upload --repository testpypi dist/{package_name}.whl