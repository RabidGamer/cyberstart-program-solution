import requests

file = open("file.txt", "w")

string1 = requests.get("https://assess.joincyberdiscovery.com/challenge-files/clock-pt1?verify=AnrZkxnniqbjIWQXkXyYxg%3D%3D")
string2 = requests.get("https://assess.joincyberdiscovery.com/challenge-files/clock-pt2?verify=AnrZkxnniqbjIWQXkXyYxg%3D%3D")
string3 = requests.get("https://assess.joincyberdiscovery.com/challenge-files/clock-pt3?verify=AnrZkxnniqbjIWQXkXyYxg%3D%3D")
string4 = requests.get("https://assess.joincyberdiscovery.com/challenge-files/clock-pt4?verify=AnrZkxnniqbjIWQXkXyYxg%3D%3D")
string5 = requests.get("https://assess.joincyberdiscovery.com/challenge-files/clock-pt5?verify=AnrZkxnniqbjIWQXkXyYxg%3D%3D")
stringAll = (((((string1.content)+(string2.content))+(string3.content))+(string4.content))+(string5.content))


url = b"https://assess.joincyberdiscovery.com/challenge-files/get-flag?verify=AnrZkxnniqbjIWQXkXyYxg%3D%3D&string=".decode('utf-8')
stringDone = stringAll.decode('utf-8')

file.write((url) + (stringDone))
print((url) + (stringDone))
