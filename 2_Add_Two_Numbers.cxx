/*
2. Add Two Numbers
Medium


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

2 —> 4 —> 3 —> None

5 —> 6 —> 4 —> None

7 —> 0 —> 8 —> None

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) { 
    ListNode* head = new ListNode();
    ListNode* tmp = head;
    bool last = false;  //variable to keep track whether the last two two digits added up to value >= 10
    while(l1 != NULL || l2 != NULL)
    {
        int sum;
        if(l1 == NULL)
            sum = l2->val; 
        else if(l2 == NULL)
            sum = l1->val;
        else 
            sum = l1->val + l2->val;
        
        if(!last && sum < 10)
        {
            tmp->next = new ListNode(sum);
            last = false;
        }
        else if(!last && sum >= 10)
        {
            tmp->next = new ListNode(sum%10);
            last = true;
        }
        else if(last && sum+1 < 10)
        {
            tmp->next = new ListNode(sum+1);
            last = false;
        }
        else
        {
            tmp->next = new ListNode((sum+1)%10);
            last = true;
        }
        tmp = tmp->next;
        if(l1 != NULL)
            l1 = l1->next;
        if(l2 != NULL)
            l2 = l2->next;
    }
    if(last)
        tmp->next = new ListNode(1);
    return head->next;
}
};
