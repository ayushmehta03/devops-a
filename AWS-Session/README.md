# Deploying a Node Js Application on AWS EC2

# easy steps to follow for deployment

create ec2 instance on aws

download the pem key 

add the configuration in the terminal

#cmd

chmod 400 key_path

ssh -i key_path machine_details@public_ip_v4 address

#setup git

sudo apt update if ubunutu machine

sudo apt install git -y


#install node js and npm + verify

sudo apt install node

node --version


sudo apt install npm

npm --version

#clone the repo

git clone paste the link 


#move to the repo path

cd folder_name 


#install dependencies

npm install


#aws console steps

go to aws ec2 dashboard

security groups 

add security for the port on which app is running eg.3000

save it 

#final step

take the public ipv4 address and allign it with the port

eg> public_ipv4:port_number

done and dusted


### Project is deployed on AWS 🎉
