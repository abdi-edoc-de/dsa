

class Solution {

    /**
     * @param ListNode $head
     * @param Integer $k
     * @return ListNode
     */
    function reverseKGroup($head, $k) {
        if ($head === null || $k === 1) {
            return $head;
        }

        $dummy = new ListNode(0);
        $dummy->next = $head;

        $current = $dummy;
        $prev = $dummy;
        $next = null;
        $length = 0;

        // Calculate length of the list
        while ($current->next !== null) {
            $length++;
            $current = $current->next;
        }

        while ($length >= $k) {
            $current = $prev->next;
            $next = $current->next;

            for ($i = 1; $i < $k; $i++) {
                $current->next = $next->next;
                $next->next = $prev->next;
                $prev->next = $next;
                $next = $current->next;
            }

            $prev = $current;
            $length -= $k;
        }

        return $dummy->next;
    }
}
