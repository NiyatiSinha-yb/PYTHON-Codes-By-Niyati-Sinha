#now i want to import shipping.py but as it is present in package eccomerce we can't import it directly
import eccomerce.shipping # importing the whole module shipping , we used eccomerce .shipping as shipping module is in eccomerce package
eccomerce.shipping.calc_shipping() #calling a function from the module