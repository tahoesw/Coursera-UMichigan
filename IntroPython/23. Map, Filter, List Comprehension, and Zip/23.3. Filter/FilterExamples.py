def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

nums = [3, 4, 6, 7, 0, 1]
print("Original list:", nums)
print("Even numbers in list", keep_evens(nums))

def keep_evenz(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print("Same using filter()", keep_evenz([3, 4, 6, 7, 0, 1]))

print("---------")

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

print(lst_check)
filter_testing = filter(lambda item: 'w' in item, lst_check)
print(list(filter_testing), "have a 'w' in them")

print("---------")

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

print(lst)
lst2 = filter(lambda item: 'o' in item, lst)
print(list(lst2), "have an 'o' in them")
