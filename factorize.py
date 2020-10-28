import math as ma
import os
import sys
import copy


def factorize(numbers):
    """
        A Faire:
        - Ecrire une fonction qui prend en paramètre une liste de nombres et qui retourne leurs decompositions en facteurs premiers
        - cette fonction doit retourner un dictionnaire Python où :
            -- la clé est un nombre n parmi la liste de nombres en entrée
            -- la valeur est la liste des facteurs premiers de n (clé). Leur produit correpond à n (clé).

        - Attention :
            -- 1 n'est pas un nombre premier
            -- un facteur premier doit être répété autant de fois que nécessaire. Chaque nombre est égale au produit de ses facteurs premiers. 
            -- une solution partielle est rejetée lors de la soumission. Tous les nombres en entrée doivent être traités. 
            -- Ne changez pas le nom de cette fonction, vous pouvez ajouter d'autres fonctions appelées depuis celle-ci.
            -- Ne laissez pas trainer du code hors fonctions car ce module sera importé et du coup un tel code sera exécuté et cela vous pénalisera en temps.
    """
    # def _get_prime_numbers(n):
    #     """Return a list of all prime numbers <= n"""
    #     prime_numbers = [2]
    #     for number in range(3, n + 1):
    #         prime = True
    #         for p in range(2, int(ma.sqrt(number)) + 1):
    #             if number % p == 0:
    #                 prime = False
    #                 break
    #         if prime:
    #             prime_numbers.append(number)
    #     return prime_numbers

    def _get_next_prime(number):
        """Return the smallest prime number greater than number"""
        n = number + 1
        prime = False
        while not(prime):
            prime = True
            for p in range(2, int(ma.sqrt(n)) + 1):
                if n % p == 0:
                    prime = False
                    break
            if prime:
                return n
            prime = False
            n += 1

    def _factorize(number, factors):
        """Return the prime factorization of number as a list"""
        factors = copy.copy(factors)
        factors_number = []
        d = 2
        if len(factors) == 0:
            factors.append(d)
        idx_d = 0
        numb = number  # copy to keep number as it is
        while (numb != 1):
            while numb % d == 0:
                factors_number.append(d)
                numb = numb // d
            if len(factors_number) == 0 and d > ma.sqrt(number):
                return ([number], factors)
            if len(factors) > 0 and idx_d < len(factors) - 1:
                idx_d += 1
                d = factors[idx_d]
            else:
                d = _get_next_prime(d)
                factors.append(d)

        return (factors_number, factors)

    # max_number = max(numbers)
    # factors = _get_prime_numbers(int(ma.sqrt(max_number)) + 1)
    result = {}
    list_primes = [2]
    numbers = sorted(numbers)
    print(numbers)
    # print(numbers)
    for i, number in enumerate(numbers):
        # if i == 0 or i==1 or i==3:
        #     print(i)
        # print(number)
        # print('before', list_primes)
        res = _factorize(number, list_primes)
        list_primes = res[1]
        # print('after', list_primes)
        result[number] = res[0]
        # result[number] = _factorize(number, list_primes)

    return result

#########################################
#### Ne pas modifier le code suivant ####
#########################################
if __name__=="__main__":
    input_dir = os.path.abspath(sys.argv[1])
    output_dir = os.path.abspath(sys.argv[2])
    
    # un repertoire des fichiers en entree doit être passé en parametre 1
    if not os.path.isdir(input_dir):
	    print(input_dir, "doesn't exist")
	    exit()

    # un repertoire pour enregistrer les résultats doit être passé en parametre 2
    if not os.path.isdir(output_dir):
	    print(output_dir, "doesn't exist")
	    exit()       

     # Pour chacun des fichiers en entrée 
    for data_filename in sorted(os.listdir(input_dir)):
        # if data_filename == 'training_data01.txt':
        print(data_filename)
        # importer la liste des nombres
        data_file = open(os.path.join(input_dir, data_filename), "r")
        numbers = [int(line) for line in data_file.readlines()]        
        
        # decomposition en facteurs premiers
        D = factorize(numbers)

        # fichier des reponses depose dans le output_dir
        output_filename = 'answer_{}'.format(data_filename)             
        output_file = open(os.path.join(output_dir, output_filename), 'w')
        
        # ecriture des resultats
        for (n, primes) in D.items():
            output_file.write('{} {}\n'.format(n, primes))
        
        output_file.close()

    
