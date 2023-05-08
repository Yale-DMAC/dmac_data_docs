# ArchivesSpace Custom Build Workflow

1. Create a new branch of ArchivesSpace, pulling in any commits needed, and push to an ArchivesSpace Github repository: e.g. [https://github.com/fordmadox/archivesspace/tree/2.4.1.yale.20190124](https://github.com/fordmadox/archivesspace/tree/2.4.1.yale.20190124) 
2. Test out the branch by running it in development locally (preferably with a database snapshot), with all of the same plugins listed within [https://github.com/YaleArchivesSpace/aspace-deployment/blob/master/test/plugins.yml](https://github.com/YaleArchivesSpace/aspace-deployment/blob/master/test/plugins.yml) 
    * For instructions on setting up a development version of ASpace, start here: ~~http://archivesspace.github.io/archivesspace/user/archivesspace-build-system/  ~~[https://archivesspace.github.io/tech-docs/development/dev.html](https://archivesspace.github.io/tech-docs/development/dev.html) 
3. If everything looks good (and we should have some automated tests here too!), it’s time to create a new docker image:
    * First, make sure you have a Docker Hub account and all things Docker installed locally;
    * From your archivesspace Github directory, making sure that you’re on the new branch that you’re testing, and then run the following (although the first two likely won’t be required, unless you’re testing with the Docker build, as well):
        1. docker-compose stop
        2. docker-compose rm
        3. docker-compose build
    * If the Docker build is successful, it’s now time to push your image to Docker Hub (so make sure you’re logged into Docker Hub):
        4. Your new image is tagged “latest”, and LYRASIS would like us to change that tag name to branch the branch name that we’re using. Now type:
        5. USER=whatever your Docker Hub username is
        6. TAG=whatever your Github archivesspace branch name is
            * E.g. TAG=2.7.1.yale.20210921
        7. docker tag archivesspace_app:latest $USER/archivesspace:$TAG
        8. docker push $USER/archivesspace:$TAG
4. Once the image is successfully pushed to Docker Hub, it’s time to update our “aspace-deployment” Github repository to reference the new custom build.
    * E.g. [https://github.com/YaleArchivesSpace/aspace-deployment/blob/master/test/docker-image-version.txt](https://github.com/YaleArchivesSpace/aspace-deployment/blob/master/test/docker-image-version.txt) 
5. If everything checks out in TEST, repeat step 4 and update the custom build reference for PROD.