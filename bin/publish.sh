rm -rf build
rm -rf dist
rm -rf ezpp.egg-info
python3 setup.py sdist bdist_wheel
twine upload dist/*