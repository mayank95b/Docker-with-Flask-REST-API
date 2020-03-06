# Flask_with_REST_API

Flask is a web application framework written in Python. It is developed by Armin Ronacher, who leads an international group of Python enthusiasts named Pocco. Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine. 
Flask is often referred to as a micro framework. It aims to keep the core of an application simple yet extensible.

### Difference b/w Web application and Web Service is that :
- in most of the cases web services will return json where as Web application will return web pages i.e. index.html(eg. return render_template("index.html")

- All communications b/w server/server,server/browser, browser/browser will in  some form of text/json (images or videos are invalid.)

- For example Json data can send as  shown below :

                {
                  "field1" : 3,  # value can be number,string,boolean & array
                  "field2" : "abc",
                  "boolean" : 1,
                  "array" : [1,2,3,4,"abc"],
                  "array of objects" :
                  [
                      {
                         "field1" : 1
                      },

                      {
                         "field2" : "abc"
                      }
                  ],

                  "array of nested array":
                  [
                   {
                     "nested array":
                     [

                         {
                            "field2" : "abc",
                            "name" : "Mayank"
                         }
                     ]
                   }

                   ]
## Docker Concept

Docker is a platform for developers and sysadmins to build, run, and share applications with containers. The use of containers to deploy applications is called containerization. Containers are not new, but their use for easily deploying applications is.

Docker is a popular virtualization tool that replicates a specific operating environment on top of a host OS. Each environment is called a container.

Docker integrates with Jenkins and Bamboo, too. If you use it together with one of these automation servers, you can further improve your delivery workflow. Besides, Docker is also great for cloud computing. In recent years, all major cloud providers such as AWS and Google Cloud added support for Docker. So, if you are planning a cloud migration, Docker can ease the process for you.

### Docker Engine

Docker Engine is a client-server application with these major components:

   - A server which is a type of long-running program called a daemon process (the dockerd command).

   - A REST API which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.

   - A command line interface (CLI) client (the docker command).

   <img src ="flow.png">


### Set up your Docker environment

Please refer to below reference :
  
      https://docs.docker.com/install/linux/docker-ce/ubuntu/
