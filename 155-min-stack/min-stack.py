class MinStack(object):

    def __init__(self):
        # Initialize an empty list to act as our stack
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # If the stack is empty, the new value is also the minimum
        if not self.stack:
            self.stack.append((val, val))
        else:
            # Get the current minimum from the top of the stack
            current_min = self.stack[-1][1]
            # The new minimum is the smaller of the new value and the current minimum
            new_min = min(val, current_min)
            # Push the new value and the new minimum as a pair
            self.stack.append((val, new_min))

    def pop(self):
        """
        :rtype: None
        """
        # Pop the entire pair from the top
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # Return the actual value from the top pair
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        # Return the stored minimum from the top pair
        if self.stack:
            return self.stack[-1][1]
        return None
        