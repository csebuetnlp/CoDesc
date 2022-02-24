# setup linux environment
sudo apt-get install curl
sudo apt-get install p7zip

# install docker
./setup/install_docker.sh

# setup python environment
pip install --upgrade pip
pip install mega.py
pip install pandas
pip install numpy
pip install jsonlines
pip install javalang
pip install transformers
pip install tqdm
pip install nltk
pip install prettytable
pip install torch==1.5.1
pip install gdown

# download dataset
mkdir data/
python Setup/Download_data.py


# setup CodeSearchNet
git clone https://github.com/code-desc/CodeSearchNet.git
sudo cp -rf -t CodeSearchNet/resources/data/ data/sample_data/csn_preprocessed_data/java/
cd CodeSearchNet/
script/setup
cd ..


