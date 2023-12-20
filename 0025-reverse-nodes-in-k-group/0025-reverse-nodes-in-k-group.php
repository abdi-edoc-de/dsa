
class Solution {

  
    function reverseKGroup($head, $k) {
        if ($head === null || $k === 1) {
            return $head;
        }

        // Store nodes in an array
        $nodes = [];
        $current = $head;
        while ($current !== null) {
            $nodes[] = $current;
            $current = $current->next;
        }

        // Reverse groups of k nodes in the array
        for ($i = 0; $i < count($nodes); $i += $k) {
            if ($i + $k <= count($nodes)) {
                $this->reverseArray($nodes, $i, $i + $k - 1);
            }
        }

        // Reconstruct the linked list from the nodes array
        for ($i = 0; $i < count($nodes) - 1; $i++) {
            $nodes[$i]->next = $nodes[$i + 1];
        }
        $nodes[count($nodes) - 1]->next = null;

        return $nodes[0];
    }

    private function reverseArray(&$array, $start, $end) {
        while ($start < $end) {
            $temp = $array[$start];
            $array[$start] = $array[$end];
            $array[$end] = $temp;
            $start++;
            $end--;
        }
    }
}