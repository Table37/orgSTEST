def restart_program():
    import os
    import sys
    python = sys.executable
    os.execl(python, python, * sys.argv)
def run():
        import subprocess
        pel = input("Run which:?\nA- orgST visual | C- Channels\n>> ").lower()

        if pel == 'a':
            subprocess.run(["python3", "PYextras/app.py"])
        if pel == 'c':
            inpu = input("W - WebServer : T - Terminal ").lower()
            match inpu:
                case "w":
                    subprocess.run(['cd', 'cv', '|', 'python3', 'server.py'])
                case "t":
                    subprocess.run(["python3", "PYextras/channelviewer.py"])
        else:
            print("please input the assigned letter of a certain choice, and not the name")
            print('')
            restart_program()
def sauce(yes_ins, jsonfile):
        print(" Would you like to dump raw data?")
        d = input(" Y/N: ")
        if yes_ins.count(d):
            print(jsonfile)

def orgid():
    print("Creating an orgID")
    print("Please understand we are unable to recover your password")
    print("And we currently cannot change passwords")
    print("If you forget your password please make a new user")
    import orgid.client
    orgid.client.crusr()

def hist(jsonfile):
    print(" version= ", jsonfile["version"])
    print(" updates=", jsonfile["updates"])
    print(" eufi ver-", jsonfile["eufi"])
    print(" authors: ", jsonfile["authors"])

def pride():
    import subprocess
    print("OHHHHHH CAAAANADAAAAAA")
    subprocess.run(["python3", "PYextras/TheFlag.py"])

def head():
    import socket
    print(f"orgST © 2024-2025 by Wdboyes13, progman.task is licensed under CC BY-NC-ND 4.0\n'orgST', 'organizationSTATION', and the orgST logo are trademarks of orgST.")
    print("---------------------------------------")
    print("orgST Terminal 1.8")
    print("Refer to the readme for more information.")
    inp = input(f"{socket.gethostname()} >>")
    return inp