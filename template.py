'''      
# Example usage:
if __name__ == "__main__":
    hashing = Hashing("abc")
    print(hashing.substringHash(0, 2))  # Hash for "abc"
'''
class Hashing:
    def __init__(self, a):
        self.s = a
        self.n = len(a)
        self.hashPrimes = [1000000009, 100000007]
        self.base = 31
        self.primes = len(self.hashPrimes)
        
        # Precompute powers and inverse powers
        self.hashValues = []
        self.powersOfBase = []
        self.inversePowersOfBase = []
        
        for prime in self.hashPrimes:
            # Initialize power arrays
            power = [1] * (self.n + 1)
            inv_power = [1] * (self.n + 1)
            
            # Compute powers of base
            for j in range(1, self.n + 1):
                power[j] = (self.base * power[j-1]) % prime
            
            # Compute inverse powers using Fermat's little theorem
            inv_power[self.n] = pow(self.base, prime-2, prime)
            for j in range(self.n-1, -1, -1):
                inv_power[j] = (inv_power[j+1] * self.base) % prime
            
            self.powersOfBase.append(power)
            self.inversePowersOfBase.append(inv_power)
        
        # Compute hash values
        for i in range(self.primes):
            prime = self.hashPrimes[i]
            hash_val = [0] * self.n
            for j in range(self.n):
                current_char = ord(self.s[j]) - ord('a') + 1
                hash_val[j] = (current_char * self.powersOfBase[i][j]) % prime
                if j > 0:
                    hash_val[j] = (hash_val[j] + hash_val[j-1]) % prime
            self.hashValues.append(hash_val)
    
    def substringHash(self, l, r):
        """Returns hash values for substring s[l..r] (0-based)"""
        result = []
        for i in range(self.primes):
            prime = self.hashPrimes[i]
            val1 = self.hashValues[i][r]
            val2 = self.hashValues[i][l-1] if l > 0 else 0
            hash_val = (val1 - val2) % prime
            hash_val = (hash_val * self.inversePowersOfBase[i][l]) % prime
            result.append(hash_val)
        return result

    @staticmethod
    def mod_sub(a, b, mod):
        return (a - b) % mod

    @staticmethod
    def mod_mul(a, b, mod):
        return (a * b) % mod
