
curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -
sudo dnf install -y nodejs
curl -LO https://github.com/grafana/k6/releases/download/v0.45.0/k6-v0.45.0-linux-amd64.tar.gz
tar -xvzf k6-v0.45.0-linux-amd64.tar.gz
sudo mv k6-v0.45.0-linux-amd64/k6 /usr/local/bin/
k6 run test.js
