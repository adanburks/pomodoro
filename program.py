from datetime import datetime, timedelta, date, time


def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------')
    print('    POMODORO TIMER')
    print('----------------------')
    print()


def run_event_loop():
    work_interval = timedelta(minutes=25)
    rest_interval = timedelta(minutes=5)
    break_interval = timedelta(minutes=15)


    loop = 0
    # while loop < 4:

def timer(n):
    while n > 0:
        n -= 1
        if n == 0:
            print('Time has elapsed')



if __name__ == '__main__':
    main()
