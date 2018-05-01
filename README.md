# GuestWiFi

GuestWIFI is a Python flask application with flic support to automatically change the WiFi password of a guest network on a DD-Wrt access point. The app has an online webpage to manage the password, uses a flic button to initiate the password change, and integrates an ESC/POS network thermal printer to print the new generated credentials in form of a voucher.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

#### WebApp
All required pip packages are included in the file [requirements.txt](requirements.txt). The app uses:

```
python 3
flask
python-esc-pos
fliclib
```

#### Flic Server
To use the flic button service, a flicd server is required. We use the linux version available here: [fliclib-linux-hci](https://github.com/50ButtonsEach/fliclib-linux-hci)

The flicd service can be installed on the same machine or on another server such as a Raspberry pi 3.

#### DD-Wrt Router or Access Point
You have to enable the ssh server on the router.

You neet to install in dd-wrt the ssh public key of the host running the app, so that the app can connect without password and send commands by ssh.

### Installing Development Environment
1. Set up a virtual environment with python 3 in the repo directory.
```
virtualenv .
```

2. Activate the virtual environment.
```
source bin/activate
```

3. install APP dependencies.
```
pip install -r requirements.txt
```

4. Adjust the settings in [settings.py](settings.py) according to your set-up.

5. Run the development server.
```
python manage.py runserver
```

6. Connect to the server `http://127.0.0.1:5000`

## Deployment
Deployment to Apache 2.4 can be achieved with the included [GuestWiFi.wsgi](GuestWiFi.wsgi) script.

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Filippo Fontana** - *Initial work*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
