<h1 align="center">
  <br>
  BMS (Message Bombing Service) v1.0.0
  <br>
</h1>


<p align="center">A free and open-source SMS bombing application.</p>

## NOTES:


> **this program is just the enhanced sms part of the TBomb git repo, fetched and modified by myself. you can contribute or check the TBomb by [clicking here..](https://https://github.com/TheSpeedX/TBomb).**

> **Termux version from Play Store is not supported since 2019, please use the latest version from F-Droid Store!**

- The application requires active internet connection to contact the APIs.
- You would not be charged for any SMS dispatched as a consequence of this script.
- For best performance, use single thread with considerable delay time.
- Always ensure that you are using the latest version and have Python 3.
- This application must not be used to cause harm/discomfort/trouble to others.
- By using this, you agree that you cannot hold the contributors responsible for any misuse.

## Compatibility
Check your Python version by typing in
```shell script
$ python --version
```
If you get the following
```shell script
Python 3.12.1
```
or any version greater than or equal to 3.4, this script has been tested and confirmed to be supported. For obsolete versions of Python (eg 2.7), use discretion while executing the script as it has not been tested there.

## Features

- Unlimited (with abuse protection) and super-fast bombing with multithreading
- Flexible with addition of newer APIs with the help of JSON documents
- Modular codebase and snippets can be easily embedded in other program


## Usage:
just run:
```shell
python bomber.py --help
```

### Install from GIT
```shell script
git clone https://github.com/h4jack/bms.git
cd bms
```

#### For Termux

To use the bomber type the following commands in Termux:
```shell script
pkg install git -y 
pkg install python -y 
git clone https://github.com/h4jack/bms.git
cd bms
```

##### Install dependencies:

```shell script
brew install git
brew install python3
sudo easy_install pip
sudo pip install --upgrade pip
git clone https://github.com/h4jack/bms.git
cd bms
pip install -r requirements.txt
```


## Contributors of TBomb

- Catch **[t0xic0der](https://github.com/t0xic0der)** at https://atlasdoc.netlify.app
- Check **[Avinash](https://github.com/AvinashReddy3108)** at https://github.com/AvinashReddy3108
- Mail **[scpketer](https://github.com/scpketer)** at scpketer@protonmail.ch
- Mail **[0n1cOn3](https://github.com/0n1cOn3)** at 0n1cOn3@gmx.ch
- Ping **Rieltar** at https://t.me/RieltarReborn
- Check **[Bishal](https://github.com/kbshal)** at https://github.com/kbshal

### TODO:

- [x] Make Code More Readable and Extensible
- [ ] Make Code More Efficient and Faster
- [ ] Add More Mail Spam APIs
- [ ] Add More SMS Spam APIs
- [ ] Add More Call Spam APIs
- [ ] Resolve threading issue in some devices

Give a ★ if you like this project!
