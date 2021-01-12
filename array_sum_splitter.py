'''
https://www.geeksforgeeks.org/split-array-two-equal-sum-subarrays/

Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays is the same. Print the two subarrays.

Examples :

Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
Output :  { 1 2 3 4 } 
          { 5 , 5 }

Input : Arr[] = { 4, 1, 2, 3 }
Output : {4 1}
         {2 3}

Input : Arr[] = { 4, 3, 2, 1}
Output : Not Possible
Asked In : Facebook interview

'''
import unittest

class TestArraySumSplitter(unittest.TestCase):
    
    def test_cannot_split_too_few_element(self):
        a = [1]
        result = array_sum_splitter(a)
        self.assertEqual(result, False)
    
    def test_cannot_split_sum_mod2_not_equal_0(self):
        a = [1, 2]
        result = array_sum_splitter(a)
        self.assertEqual(result, False)
    
    def test_cannot_split_due_to_impossible_to_sum(self):
        a = [7, 19, 1, 1, 2, 4, 1, 7]
        result = array_sum_splitter(a)
        self.assertEqual(result, False)
    
    def test_split_success(self):
        a = [1, 2, 3]
        result = array_sum_splitter(a)
        self.assertEqual(result, ([1, 2] , [3]))
    

def array_sum_splitter(a):
    return my_way(a)

def my_way(a):
    if a is None \
        or type(a) != list \
        or (type(a) == list and len(a) < 2) \
        or sum(a) % 2 != 0:
        return False

    half_sum = sum(a) / 2
    for i in range(0, len(a)):
        current_sum = sum(a[0:i])
        if current_sum >= half_sum:
            return (a[0:i], a[i:]) if current_sum == half_sum else False



if __name__ == '__main__':
    unittest.main()