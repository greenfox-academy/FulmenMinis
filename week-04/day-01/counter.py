#Counter
#
#    Create Counter class
#        which has an integer field value
#        when creating it should have a default value 0 or we can specify it when creating
#        we can add(number) to this counter another whole number
#        or we can add() without parameters just increasing the counter's value by one
#        and we can get() the current value
#        also we can reset() the value to the initial value
#    Check if everything is working fine with the proper test
#        Download test_counter.py and place it next to your solution
#        Run the test file as a usual python program

class Counter(object):
    value_initial = 0

    def __init__(self, value=0):
        self.value = value
        Counter.value_initial = value

    def add(self, num=None):
        if num != None:
            self.value += num
        else:
            self.value += 1 
    
    def get(self):
        return self.value
    
    def reset(self):
        self.value = Counter.value_initial
