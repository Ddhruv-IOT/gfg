    def __init__(self, data):
        self.data = data
        self.next = None

'''
import sys
sys.set_int_max_str_digits(0)
class Solution:
    def addTwoLists(self, num1, num2):
        sys.set_int_max_str_digits(1000000)
        f1=''
        f2=''
        temp=num1
        while temp:
            f1+=str(temp.data)
            temp=temp.next
        temp=num2
            f2+=str(temp.data)
        f1=str(int(f1)+int(f2))
        head=None
        temm=head
        for i in f1:
            n=Node(int(i))
            if not head:
                head=n
                temm=head
            else:
                temm.next=n
                temm=temm.next
#User function Template for python3
''' Node for linked list:
class Node:
        return head
...# } Driver Code Ends