## Publisher Subscriber

This code is is referenced to [modernpython repo.](https://github.com/rhettinger/modernpython)

Code implements a simple twitter-like app. The pubsub.py implements the data model and core services. 
The session.py loads sample data. The app.py file runs a webserver for the application. 
The views directory has the Bottle templates and the static directory 
has the static resources (icons and photos).

### Requirements
Python >= 3.6 required.  
Install dependencies with 
```bash
pip install -r requirements.txt
```
For better interaction is recommended to use [virtualenv](https://github.com/pypa/virtualenv).

To start the service, run:

```bash
(env) $ python app.py
```

Then point your browser to `http://localhost:8080/`

The login information is in the `session.py` file.
