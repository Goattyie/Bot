sudo apt install make gcc g++ git curl build-essential libreadline-dev libbz2-dev libssl-dev libsqlite3-dev libxslt1-dev libxml2-dev python3-dev zlib1g-dev libffi-dev -y
curl https://pyenv.run | bash
cat bashrc >> ~/.bashrc
. ~/.bashrc

pyenv install 3.5.10
pyenv local 3.5.10
pip3 install --upgrade pip -y
pip3 install tensorflow==1.5 -y
pip3 uninstall numpy -y
pip3 install numpy==1.16.4 flask -y