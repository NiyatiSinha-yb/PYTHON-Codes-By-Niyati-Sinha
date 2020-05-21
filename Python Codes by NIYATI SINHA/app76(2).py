#now i want to import shipping.py but as it is present in package eccomerce we can't import it directly
#import eccomerce.shipping # importing the whole module shipping , we used eccomerce .shipping as shipping module is in eccomerce package

#eccomerce.shipping.calc_shipping() #calling a function from the module

#from eccomerce import shipping #now the shipping module is an object so we can use the dot operator directly to access its members
#shipping.calc_shipping()

from eccomerce.shipping import calc_shipping, calc_tax
calc_shipping()
calc_tax()