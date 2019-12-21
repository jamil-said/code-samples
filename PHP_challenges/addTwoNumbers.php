<?php

/* addTwoNumbers
You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except 
the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/

/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */


class Solution {
    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {
        $l3 = $res = new ListNode(0);
        $carry = 0;
        while (true) {
            $v3 = ($l1->val ?: 0) + ($l2->val ?: 0) + $carry;
            $carry = ($v3 < 10) ? 0 : 1;
            $l3->val = $v3 % 10;
            $l1 = $l1->next;
            $l2 = $l2->next;
            if ($l1 || $l2 || $carry) {
                $l3->next = new ListNode(0);
                $l3 = $l3->next;
            }
            else
                break;
        }
        return $res;
    }
}


/* Alternative: this is fast but fails for integers bigger than PHP's limit

    function addTwoNumbers($l1, $l2) {
        $n1 = 0; 
        $n2 = 0;
        $i = 1;
        while ($l1) {
            $n1 += ($l1->val * $i);
            $i *= 10;
            $l1 = $l1->next;
        }
        $i = 1;
        while ($l2) {
            $n2 += ($l2->val * $i);
            $i *= 10;
            $l2 = $l2->next;
        }
        $n3 = $n1 + $n2;
        $l3 = $res = new ListNode(0);
        while (true) {
            $tmp = $n3 % 10;
            $l3->val = $tmp;
            $n3 = floor($n3 / 10);
            if ($n3 == 0)
                break;
            $l3->next = new ListNode(0);
            $l3 = $l3->next;
        }
        return $res;
    }

*/
