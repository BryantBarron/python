# https://dmoj.ca/problem/ecoo21p1


startHW = int(input())
interval = int(input())
messageReceived = int(input())

firstInterval = startHW + interval
secondInterval = firstInterval + interval
thirdInterval = secondInterval + interval

print(f"Timer at first interval: {firstInterval}")
print(f"Timer at second interval: {secondInterval}")
print(f"Timer at third interval: {thirdInterval}")

if(messageReceived > thirdInterval):
    print('Who knows when you\'ll get a response...')
elif((messageReceived > secondInterval) and (messageReceived < thirdInterval)):
    print(f"You will get a response after {thirdInterval} minutes.")
elif((messageReceived > firstInterval) and (messageReceived < secondInterval)):
    print(f"You will get a response after {secondInterval} minutes.")
else:
    print(f"You will get a response after {firstInterval} minutes.")