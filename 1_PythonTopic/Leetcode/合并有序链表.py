# @Version  :1.0
# @Author   :李祎凡
# @File     :合并有序链表
# @Time     :2025/3/26 下午10:57
# @Other    :文件说明
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy


        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next


        curr.next = list1 if list1 else list2
        return dummy.next
