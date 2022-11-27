import time
print("Starting 6-second sleep")
for x in range(2, 6):
    print('Sleep {} seconds..'.format(x))
    time.sleep(x) # "Sleep" for x seconds
print('Done!')
