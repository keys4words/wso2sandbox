# basic repo
https://hub.docker.com/r/wso2/wso2am
# components images
https://hub.docker.com/u/wso2/


# start API Manager instance
docker run -it -p 8280:8280 -p 8243:8243 -p 9443:9443 --name api-manager wso2/wso2am:4.1.0
# access Carbon Management Console
https://{DOCKER_HOST}:9443/carbon
# access API Manager Publisher
https://{DOCKER_HOST}:9443/publisher
# access API Manager Developer Portal
https://{DOCKER_HOST}:9443/devportal

# shell access & server logs