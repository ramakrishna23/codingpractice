class TwoSumClass(object):

    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    #======================Special Functions Used===========


    """
    enumerate() :

    Often, when dealing with iterators, we also get need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task. Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.

    Syntax: 

    enumerate(iterable, start=0)
    Parameters:

    Iterable: any object that supports iteration
    Start: the index value from which the counter is to be started, by default it is 0

    # changing index and printing separately

    l1 = ["eat", "sleep", "repeat"]
    for count, ele in enumerate(l1, 100):
        print (count, ele)
    
    output

    100 eat
    101 sleep
    102 repeat

    index()

    Python index() is an inbuilt function in Python, which searches for a given element from the start of the list and returns the lowest index where the element appears. 

    Syntax: list_name.index(element, start, end)

    Parameters:  

    element – The element whose lowest index will be returned.
    start (Optional) – The position from where the search begins.
    end (Optional) – The position from where the search ends.
    Returns: the lowest index where the element appears.

    Error: If any element which is not present is searched, it returns a ValueError

    list of items
    list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
    
    # Will print index of '4' in sublist
    # having index from 4 to 8.
    print(list1.index(4, 4, 8))

    """

    def twoSum(self, nums, target):
        
        seen = {}
        for i, firstNumber in enumerate(nums):

            secondNumber = target - firstNumber # firstNumber + secondNumber = target
            print(i, firstNumber, secondNumber)
            if secondNumber in seen:
                return [seen[secondNumber], i]
            else:
                seen[firstNumber] = i
    
    def twoSumSecound(self,nums, target):

        for i, firstNumber in enumerate(nums):
            secondNumber = target - firstNumber

            if secondNumber in nums:

                index = nums.index(secondNumber)

                return[i, index]

            
obj = TwoSumClass()
print(obj.twoSumSecound([1,3,2], 3))