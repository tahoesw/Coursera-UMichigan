"""
As we have seen, two instances of the Point class each have their own instance variable x. Setting x in one
 instance doesn’t affect the other instance.

A class can also have class variables. A class variable is set as part of the class definition.

For example, consider the following version of the Point class. Here we have added a graph method that
 generates a string representing a little text-based graph with the Point plotted on the graph. It’s not
 a very pretty graph, in part because the y-axis is stretched like a rubber band, but you can get the
 idea from this.

Note that there is an assignment to the variable printed_rep on line 20. It is not inside any method.
 That makes it a class variable. It is accessed in the same way as instance variables. For example, on
 line 33, there is a reference to self.printed_rep. If you change line 20, you have it print a different
 character at the x,y coordinates of the Point in the graph.
"""
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

# class method
    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(2, 3)
p2 = Point(7, 12)
print(p1.graph())
print()
print(p2.graph())
