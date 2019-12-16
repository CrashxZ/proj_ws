import os

while 1:
    i = input("Enter code >")
    if i == 0:
        os.system("rosservice call /dji_sdk/mfio_config \"mode: 0 channel: 0 init_on_time_us: 500 pwm_freq: 50\"")
        print("\nReset")
    elif i == 1:
        os.system("rosservice call /dji_sdk/mfio_config \"mode: 0 channel: 0 init_on_time_us: 2500 pwm_freq: 50\"")
        print("\nFired")
    else:
        exit()

