import utils
import csv

primeArr = utils.getPrimeArr(1000000000)

with open('all_prime_list.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(primeArr)


