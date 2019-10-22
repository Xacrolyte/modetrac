# Modetrac

## Introduction :clipboard:

**Modetrac** is a premature motion detection and tracking program which allows the user to redefine and use it for various purposes like
airwriting and hand gesture recognition. The code written can be extended to any number of devices and via wireless network setup.

Read more about in the research paper: [Modetrac-paper](https://docs.google.com/document/d/1uQKKRtI5o4usYDdXfiEHEjII8T70OmRxLxBKD5asQu4/edit?usp=sharing)
## Steps to Setup :scroll:

You have to fork and clone the project to follow the following setup guidelines:
### 1. Create Virtual Environment :earth_asia:

```sh
$ virtualenv -p python3  VENV_NAME
```

#### Activate

```sh
windows: > VENV_NAME/Scripts/activate

linux:   $ source VENV_NAME/bin/activate

macos:   $ source VENV_NAME/bin/activate
```

### 2. Install requirements :information_source:

```sh
$ pip3 install -r requirements.txt
```

## Steps to Contribute :scroll:

### 1. Fork it :fork_and_knife:

You can get a fork/copy of [Modetrac](https://github.com/xacrolyte/modetrac) by using the <kbd><b>Fork</b></kbd></a> button.

### 2. Clone it :busts_in_silhouette:

You need to clone (download) it to local machine using    
```sh
$ git clone https://github.com/Your_Username/modetrac.git
```
> This makes a local copy of repository in your machine.

### 3. Set it up :arrow_up:

Run the following commands to see that your local copy has a reference to your forked remote repository in Github :octocat:

```sh
$ git remote -v
origin  https://github.com/Your_Username/modetrac.git (fetch)
origin  https://github.com/Your_Username/modetrac.git (push)
```

Now, lets add a reference to the original [Modetrac](https://github.com/xacrolyte/modetrac) repository using

```sh
>$ git remote add upstream https://github.com/xacrolyte/modetrac.git
```

> This adds a new remote named ***upstream***

See the changes using

```sh
$ git remote -v
origin    https://github.com/Your_Username/modetrac.git (fetch)
origin    https://github.com/Your_Username/modetrac.git (push)
upstream  https://github.com/xacrolyte/modetrac.git (fetch)
upstream  https://github.com/xacrolyte/modetrac.git (push)
```

### 4. Sync it :recycle:

Always keep your local copy of repository updated with the original repository.
Before making any changes and/or in an appropriate interval, run the following commands *carefully* to update your local repository.

```sh
# Fetch all remote repositories and delete any deleted remote branches
$ git fetch --all --prune

# Switch to `master` branch
$ git checkout master

# Reset local `master` branch to match `upstream` repository's `master` branch
$ git reset --hard upstream/master

# Push changes to your forked `Algo_Ds_Notes` repo
$ git push origin master
```

### 5. Ready Steady Go... :turtle: :rabbit2:

Once you have completed these steps, you are ready to start contributing by checking our Issues and creating Pull Requests.

### 6. Create a new branch :bangbang:

Whenever you are going to make contribution. Please create seperate branch using command and keep your `master` branch clean (i.e. synced with remote branch).

```sh
# It will create a new branch with name Branch_Name and switch to branch Folder_Name
$ git checkout -b Folder_Name
```

Create a seperate branch for contibution and try to use same name of branch as of folder.

To switch to desired branch

```sh
# To switch from one folder to other
$ git checkout Folder_Name
```

To add the changes to the branch. Use

```sh
# To add all files to branch Folder_Name
$ git add .
```

Type in a message relevant for the code reveiwer using

```sh
# This message get associated with all files you have changed
$ git commit -m 'relevant message'
```

Now, Push your awesome work to your remote repository using

```sh
# To push your work to your remote repository
$ git push -u origin Folder_Name
```

Finally, go to your repository in browser and click on `compare and pull requests`.
Then add a title and description to your pull request that explains your precious effort.

## How to use :scroll:

### 1. Run the script 

```sh
$ python motion_tracker.py
```

#### Default input device is set to 0 (primary webcam). :camera:

```python
      #Capture window(down)
      capwindow = cv2.VideoCapture(0)
      #Capture wireless window(down)
      #capwindow = cv2.VideoCapture('http://10.103.121.102:8080/shot.jpg')
      #capwindow.set(3,width)
      #capwindow.set(4,height)
```

### 2. Watch your every movement being tracked :man:

#### Change values for optimization

```python
#Video processing
      	grey = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
      	blur = cv2.GaussianBlur(grey, (7,7), 0)
      	ret, threshold = cv2.threshold(blur, 15, 255, cv2.THRESH_BINARY)
      	dilated = cv2.dilate(threshold, np.ones((7,7), np.uint8), iterations=1)
      	eroded = cv2.erode(dilated, np.ones((7,7), np.uint8), iterations=1)
```
### 3. Contribute :smile:

#### Apply smoothness and storage 