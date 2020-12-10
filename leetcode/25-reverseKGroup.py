# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseByStartAndEnd(self, start_node: ListNode, end_node: ListNode) -> None:
        '''
        s    1      2       3       4          end

        fake cur    2       3       4          end   
             cur <- next ->next_next  
                    cur    next     next_next 
                    cur <- next  -> next_next 
                            cur     next       next_next
                            cur  <- next   ->  next_next 
                                    cur        next     {End loop}
        '''
        fake_head: ListNode = start_node

        cur = fake_head.next
        next_node = cur.next
        if cur == end_node:
            return

        while next_node!=end_node:
            next_next_node = next_node.next
            next_node.next = cur

            cur = next_node
            next_node = next_next_node
        next_node.next = cur
        fake_head.next = next_node


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        fake_head = ListNode(0, head)
        cur: ListNode = fake_head

        cnt_nodes: int = 0
        while cur:
            start_node: ListNode = cur
            while cur:
                cur = cur.next
                if cur:
                    cnt_nodes = cnt_nodes + 1
                    if cnt_nodes == k:
                        end_node: ListNode =cur

                        new_fake_head = start_node.next
                        new_first_node = end_node.next
                        self.reverseByStartAndEnd(start_node, end_node)
                        new_fake_head.next = new_first_node
                        cur = new_fake_head
                        cnt_nodes = 0
                        break

        return fake_head.next
