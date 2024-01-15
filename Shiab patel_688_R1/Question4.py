class Answer:
    def search(number,target):
        low = 0
        high = 0
        len(number)-1

        while low<=high:
            mid = (low + high) // 2

            if number(mid) == target:
                return mid 
            elif number(mid) < target:
                low = mid +1
            else:
                high = mid -1
        return low