Packaging
=========

Packaging for Ubuntu and CentOS using Docker
--------------------------------------------

We provide Dockerfiles for CentOS 7 and Ubuntu 14.04.  A Dockerfile for Ubuntu >
14.04 should work by just changing the "FROM" statement of the Ubuntu 14.04
Dockerfile.  Using these, you can easily build rpm and deb packages for
synergy-service without having to setup the build system on your own system.

The build process using Docker is made of 3 steps:

1. Build the docker image

2. Setup the build variables

3. Run the build with docker

If the build is successful, the package will be put in the build directory
inside the synergy-service directory.


### Example for CentOS 7

- go into the directory that contains the Dockerfile for CentOS 7

      cd synergy-service/packaging/docker/centos7

- build the docker image and tag it

      docker build -t synergy-centos7-builder .

- edit the file `synergy-service/packaging/docker/build_env.sh` to define environment variables.

- launch the container

      docker run -i -v /path/to/synergy-service:/tmp/synergy-service \
                 --env-file=/path/to/synergy-service/packaging/docker/build_env.sh \
                 synergy-centos7-builder

  This actually mount the synergy-service directory to `/tmp/synergy-service` on
  the guest.
  It also loads environment variables from the `build_env.sh` file.

- the resulting rpm should be in the build directory if successful


### Example for Ubuntu 14.04

- go into the directory that contains the Dockerfile for Ubuntu 14.04

      cd synergy-service/packaging/docker/ubuntu-14.04

- build the docker image and tag it

      docker build -t synergy-ubuntu14.04-builder .

- edit the file `synergy-service/packaging/docker/build_env.sh` to define environment variables.

- launch the container

      docker run -i -v /path/to/synergy-service:/tmp/synergy-service \
                 --env-file=/path/to/synergy-service/packaging/docker/build_env.sh \
                 synergy-ubuntu14.04-builder

- the resulting deb should be in the build directory if successful


Packaging for Ubuntu
--------------------

1. Install the necessary build packages:
  - debhelper
  - dh-systemd
  - build-essential
  - devscripts
  - python-all
  - python-setuptools

2. Make a gzip archive of synergy-service named `python-synergy-service_VERSION.orig.tar.gz`.

3. Copy `synergy-service/packaging/debian` to `synergy-service/debian`.

4. Go in the `synergy-service` directory and build with `debuild -us -uc`.


Packaging for CentOS
--------------------

1. Install the necessary build packages:
  - rpm-build
  - python-devel
  - python-setuptools

2. Setup your rpmbuild environment if not already done.

       mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

3. Move `synergy-service/packaging/rpm/python-synergy.spec` to
   `~/rpmbuild/SPECS`.

4. Create a source archive:

       cp -r /path/to/synergy-service ~/rpmbuild/SOURCES/python-synergy-service
       tar cjf python-synergy-service python-synergy-service.tar.bz2

5. Go in `~/rpmbuild/SPECS` and buils with `rpmbuild -ba python-synergy.spec`.