class Solution { 
    function reverseKGroup($head, $k) {
        if ($head === null || $k === 1) {
            return $head;
        }

        $dummy = new ListNode(0, $head); // Sentinel node
        $groupPrev = $dummy;

        while ($head !== null) {
            $tail = $head;
            for ($i = 0; $i < $k - 1 && $tail !== null; $i++) {
                $tail = $tail->next;
            }

            if ($tail === null) {
                break; // Not enough nodes for a group
            }

            $nextGroupHead = $tail->next;
            $this->reverseGroup($head, $tail); // In-place reversal

            $groupPrev->next = $tail;
            $head->next = $nextGroupHead;
            $groupPrev = $head;
            $head = $nextGroupHead;
        }

        return $dummy->next;
    }

    private function reverseGroup(&$head, &$tail) {
        $prev = null;
        $current = $head;
        while ($current !== $tail) {
            $next = $current->next;
            $current->next = $prev;
            $prev = $current;
            $current = $next;
        }
        $tail->next = $prev;
    }
}
