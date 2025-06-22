def solution(arrayA,arrayB):

    def gcd(a,b):
            while b:
                a,b = b,a%b
            return a

    def all_gcd(array):
        result = array[0]
        for i in range(1,len(array)):
            result = gcd(result,array[i])
        return result

    def is_valid(n,array):
        return all(i%n for i in array)

    gcd_a, gcd_b = all_gcd(arrayA), all_gcd(arrayB) 
    ans = 0
    if is_valid(gcd_a,arrayB):
        ans = max(ans,gcd_a)
    if is_valid(gcd_b,arrayA):
        ans = max(ans,gcd_b)
        
    return ans