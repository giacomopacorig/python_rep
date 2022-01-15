class ExamException(Exception):
    pass



class MovingAverage:

    def __init__(self, window_size):

        if type(window_size) is not int:
            raise ExamException("window_size must be an integer")

        if not window_size > 0 :
            raise ExamException("window_size must be greater than zero")
        
        self.window_size = window_size


    def compute(self, series):

        if type(self.window_size) is not int:
            raise ExamException("window_size must be an integer")

        if not self.window_size > 0 :
            raise ExamException("window_size must be greater than zero")

        if series is None:
            raise ExamException("series must be defined")
        
        if not isinstance(series, list):
            raise ExamException("series must be a list")

        if not len(series) >= self.window_size:
            raise ExamException("series length must be greater than window_size")

        if not all(isinstance(x, (int, float)) for x in series):
            raise ExamException("series tipo must be int or float")

        avg = []
        for i in range(len(series) - self.window_size + 1):
            avg_i = sum(series[i:i+self.window_size]) / self.window_size
            avg.append(avg_i)
        return avg

m = MovingAverage(3);
r = m.compute([2, 4, 8, 16, 32]);
print(r);