cd /home/ec2-user
sudo dnf install -y gcc-c++ make git docker
sudo dnf groupinstall -y "Development Tools"
sudo usermod -aG docker ec2-user
newgrp docker
sudo systemctl enable docker
sudo systemctl start docker
echo 'export DOCKER_BUILDKIT=1' >> ~/.bash_profile
source ~/.bash_profile
