git pull
git checkout dev
sudo kill -9 $(sudo lsof -t -i:8000)
python app.py