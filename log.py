from datetime import datetime as dt
import datetime
import os


class Log:
    log = None
    current_action = None
    current_start_time = None
    
    @staticmethod
    def _get_delta_str(d: datetime.timedelta):
        return str(d.seconds // 60)
    
    def __init__(self):
        Log.log = self
        today = str(datetime.date.today())
        self.log_path = 'log_' + today + '.csv'
        if not os.path.isfile(self.log_path):
            with open(self.log_path, 'w') as log_file :
                log_file.write(','.join(['action', 'start time', 'end time', 'duration']) + '\n')

    def start(self, action: str):
        if self.current_action:
            self.end(self.current_action)
        self.current_start_time = dt.now()
        self.current_action = action
        
    def end(self, action: str):
        now = dt.now()
        start_time = self.current_start_time.strftime("%H:%M")
        end_time = now.strftime("%H:%M")
        delta = self._get_delta_str(now - self.current_start_time)
        with open(self.log_path, 'a') as log_file:
            log_file.write(','.join([action, start_time, end_time, delta]) + '\n')
            
    def show(self):
        with open(self.log_path) as log_file:
            for line in log_file:
                print(line.strip())

    def current(self):
        print('on mode: ', self.current_action, ' for the last ',
              self._get_delta_str(dt.now() - self.current_start_time), ' minutes')

    def total_time_work(self):
        """
        :return: the total amount of time spend working today
        """
        # TODO
        pass




log = Log()

#  Functions for console use


def work():
    log.start('work')


def pause():
    log.start('pause')


def show():
    log.show()


def current():
    log.current()
