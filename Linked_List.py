class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val 
    self.next = next 

def reverseList(head):
  prev = None 
  curr = head 

  while curr:
    nxt = curr.next 
    curr.next = prev 
    prev = curr 
    curr = nxt 
  
  return prev 

def middleNode(head):
  slow = fast = head 
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow 

def mergeTwoLists(list1, list2):
  dummy = ListNode()
  tail = dummy 

  while list1 and list2:
    if list1.val < list2.val:
      tail.next = list1
      list1 = list1.next 
    
    else:
      tail.next = list2 
      list2 = list2.next 
    
    tail = tail.next 
  
  tail.next = list1 or list2 

  return dummy.next 

def removeNthFromEnd(head, n):
  dummy = ListNode(0, head)

  left = dummy 
  right = head 

  while n > 0:
    right = right.next 
    n -= 1 
  
  while right:
    left = left.next 
    right = right.next 

  left.next = left.next.next 

  return dummy.next 

def hasCycle(head):
  slow = fast = head 

  while fast and fast.next:
    slow = slow.next 
    fast = fast.next.next 

    if slow == fast:
      return True 
    
  return False 

def reorderList(head):
  slow = fast = head 

  while fast and fast.next:
    slow = slow.next 
    fast = fast.next.next 

  prev = None 
  curr = slow.next 
  slow.next = None 

  while curr:
    nxt = curr.next 
    curr.next = prev 
    prev = curr 
    curr = nxt 

  first = head 
  second = prev 

  while second:
    temp1 = first.next 
    temp2 = second.next 

    first.next = second 
    second.next = temp1 

    first = temp1 
    second = temp2 

def reverseKGroup(head, k):
  dummy = ListNode(0)
  dummy.next = head 

  groupPrev = dummy 

  while True:
    kth = groupPrev 

    for _ in range(k):
      kth = kth.next 

      if not kth:
        return dummy.next 
      
    groupNext = kth.next 

    prev = groupNext 
    curr = groupPrev.next 

    while curr != groupNext:
      temp = curr.next 
      curr.next = prev 
      prev = curr 
      curr = temp 
    
    temp = groupPrev.next 

    groupPrev.next = kth 
    groupPrev = temp 
    