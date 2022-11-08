# basic repo
https://hub.docker.com/r/wso2/wso2am
# components images
https://hub.docker.com/u/wso2/


# start API Manager instance

# shell access & server logs

# jmeter
docker run justb4/jmeter:5.5 -n -t bin/examples/CSVSample.jmx -l bin/examples/mytest1.jtl
docker cp <container-id>:/opt/apache-jmeter-5.5/bin/examples .
docker run --mount type=bind,source="$PWD/results/",target="/opt/apache-jmeter-5.5/bin/examples/" justb4/jmeter:5.5 -n -t bin/examples/CSVSample.jmx -l ./bin/examples/mytest1.jtl