# Question: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem?isFullScreen=true
def insertNodeAtHead(llist, data):
    # Write your code here
    nn = SinglyLinkedListNode(data)
    nn.next=llist
    return(nn)
