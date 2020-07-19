python3 setup.py build
python3 setup.py install
# for pyenv
if [ ! -d "~/.pyenv" ]; then
pyenv rehash && hash -r
fi
