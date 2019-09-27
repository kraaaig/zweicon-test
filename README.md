# Zweicon-test

- Infrastucture provider: **GCP**
- Machine: **VM instance**
- Platform: **Docker**

---
# Steps 

## Setup Infra

### Steps to enable Infra
- #### Create VM instance
  Minimal VM instance created based on Centos 7

      gcloud beta compute --project=<project> instances create instance-1 --description="Zweicon test" --zone=<zone> --machine-type=f1-micro --subnet=default --network-tier=<tier> --maintenance-policy=MIGRATE --service-account=<account> --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=docker-5000 --image=centos-7-v20190916 --image-project=centos-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=instance-1 --reservation-affinity=any

- #### Create FW rule to enable access to port `5000` on VM instance

      gcloud beta compute --project=<project> firewall-rules create docker-50001 --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:5000,udp:5000 --source-ranges=0.0.0.0/0 --target-tags=docker-5001

- #### Install docker on Centos 7 VM Instance

      sudo yum install -y yum-utils device-mapper-persistent-data lvm2
      sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
      sudo yum install docker-ce
      sudo usermod -aG docker $(whoami)
      sudo systemctl enable docker.service
      sudo systemctl start docker.service
  _* This docker installation commands can be added as script when VM instance boot_
    

## Build, tag and push docker image to registry

- Build image
  
      docker build --rm -f "Dockerfile" -t zweicon-test:1.0.0-alpine .

- Tagging

      docker tag zweicon-test:1.0.0-alpine kraaaig/zweicon-test:1.0.0-alpine

- Push

      docker push kraaaig/zweicon-test:1.0.0-alpine

## Run image inside VM created

      docker pull kraaaig/zweicon-test:1.0.0-alpine
      docker run --rm -it -p 5000:5000/tcp kraaaig/zweicon-test:1.0.0-alpine

## Test service (VM instance GCP)

      curl http://34.95.240.233:5000/