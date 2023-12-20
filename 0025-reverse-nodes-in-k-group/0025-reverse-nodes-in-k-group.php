
class Solution {
    function reverseKGroup($head, $k) {
        if ($head === null || $k === 1) {
            return $head;
        }

        $dummy = new ListNode(0);
        $dummy->next = $head;
        $prevGroupEnd = $dummy;

        while ($head !== null) {
            $tail = $head;
            // Find the k-th node in the group
            for ($i = 0; $i < $k - 1; $i++) {
                $tail = $tail->next;
                if ($tail === null) {
                    return $dummy->next;  // Less than k nodes remaining, so no more reversals
                }
            }

            $nextGroupStart = $tail->next;
            // Reverse the group
            list($newHead, $newTail) = $this->reverse($head, $tail);
            // Connect the reversed group with the rest of the list
            $prevGroupEnd->next = $newHead;
            $newTail->next = $nextGroupStart;

            $prevGroupEnd = $newTail;
            $head = $nextGroupStart;
        }

        return $dummy->next;
    }

    private function reverse($start, $end) {
        $prev = $end->next;
        $current = $start;

        while ($prev !== $end) {
            $temp = $current->next;
            $current->next = $prev;
            $prev = $current;
            $current = $temp;
        }

        return array($end, $start);  // new head, new tail
    }
}

// Helper function to print the linked list
function printLinkedList($head) {
    $current = $head;
    while ($current !== null) {
        echo $current->val . ' ';
        $current = $current->next;
    }
    echo "\\n";
}

// Creating and testing the linked list
$head = new ListNode(1);
$current = $head;
foreach ([2, 3, 4, 5] as $value) {
    $current->next = new ListNode($value);
    $current = $current->next;
}

$solution = new Solution();
$reversedHead = $solution->reverseKGroup($head, 2);
printLinkedList($reversedHead);
