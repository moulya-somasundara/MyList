#Write a function that takes a list of characters and reverses the letters in place. 

#Time Complexity : o(n)
#Space Complexity : o(1)

class Solution(object):
    def reverse(self,list_of_characters):
        left_index = 0
        right_index = len(list_of_characters)-1
        while (left_index < right_index):
            list_of_characters[left_index], list_of_characters[right_index] = list_of_characters[right_index], list_of_characters[left_index]
            left_index+= 1
            right_index-=1