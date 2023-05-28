# Simple Image File Server

## ABOUT 

This system supports simple image files viewer.  
You can manage and share your image files easily.  

## USAGE

### ENVIRONMENT

* Python3.6

### INSTALL

```bash
git clone https://github.com/pyohei/image-viewer.git
cd simple-image-server
```

If you want to activate virtualenv, type the below sentence.  

```bash
python -m venv venv
source venv/bin/activate
```

### SETUP

After install, you must import python library.  

```bash
pip install -r requirements.txt
```

### PREPARE

Before executing, you prepare image folder which you will use in this script.  

### EXECUTE

You can execute the below command (using the upper directory name).

```bash
python servermain.py `your image file directory`
```

If you want to execute sample, 

```bash
python server/main.py sample
```

## Plugin

I'm using jQuery plugin of [jQuery.TosRUs](http://tosrus.frebsite.nl/).  
Thanks!  

## LICENSE

* [MIT](https://github.com/pyohei/image-viewer/master/LICENSE)
