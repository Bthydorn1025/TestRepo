#from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        self.elementCount = 0
        self.count = 0

    def printSolution(self):
      printval = self.front
      while printval is not None: #if queue isnt empty, we will print the data in the queue and move to the next element to print
         print(printval.data, end=" ") #if no items are in the queue, function stops
         printval = printval.next


    def linearSearch(self, Target):
        printval = self.front
        while printval.data < Target:
            self.elementCount = self.elementCount + 1 #We will add 1 to the current counter that starts at 0
            Queue.dequeue(q) #if self.front is less than the target we dequeue that element
            printval = printval.next #move next element to the front
        return self.elementCount #return the total element count

    def isEmpty(self):
        if (self.front == None):
            return True
        else:
            return False

    def size(self):
        return self.count + 1


    def dequeue(self):
        self.data = self.front.data
        self.front = self.front.next
        self.length = self.length-1 #dequeue pops off the first element in the queue and the next element becomes the front element.
        self.count = self.count - 1 #count is the size of the queue and the size decreases by 1 after dequeue
        if (self.length == 0):
            self.rear = 0
        return self.data

    def enqueue(self, item):
        temp = Node(item)
        if (self.rear == None):
            self.front = self.rear = temp #if there are no items in the queue, the front and rear are the item added because temp is the only element
            return 0
        self.rear.next = temp #Item goes to the back of the queue
        self.rear = temp
        self.count = self.count + 1 #Added 1 to the size of the queue

    def bubbleSort(self):
        end = None
        while end != self.front:
            start = self.front #start at the front of the queue
            while start.next != end: #continue trough the queue while there are still elements
                nextval = start.next
                if start.data > nextval.data: #if the first value is greater than the next value
                    start.data, nextval.data = nextval.data, start.data #we switch the order of the elements
                start = start.next #front element goes to the next element
                nextval = nextval.next #go onto the next element
            end = start


if __name__ == '__main__':
    #Decalred local variables
    q = Queue() #creation of the queue
    minimum = 0
    maximum = 5
    userInput = 0

    print("Please enter GPA's: (Enter -1 to exit): ")
    while userInput != -1 and userInput >= minimum and userInput <= maximum: #adding elements while userInput is not -1
        userInput = float(input())
        q.enqueue(userInput)
    else:
        print("Here are the elements in the queue: ") #when -1, prints elements in the queue
    q.printSolution()
    print("\n")

    q.bubbleSort() #calling bubble sort algorithm for the queue
    q.dequeue() #dequeueing the -1
    print("Here are the GPA's after being bubble sorted:")
    q.printSolution()
    print("\n")

    print("Size of queue: ", q.size())
    queueSize = q.size() #prints the size of the queue

    Target = float(input("What is the minimum cutoff GPA for this school?: "))

    print(q.linearSearch(Target), "GPA's have been removed from the list.")
    print("Remaining list: ")
    q.printSolution()

























