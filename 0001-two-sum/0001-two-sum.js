/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var pot = {}
    let value
    nums.forEach((item, index) => {
        if ((target-item) in pot ){
            value=  [ pot[(target-item)], index]
        }
        pot[item] = index
    })
    return value
};
