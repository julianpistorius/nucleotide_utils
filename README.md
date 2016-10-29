# Playing with Nucleotides
 
 Windowed calculations over streams of nucleotide groups.
 
 Testing a sequence 3,000,000 nucleotides with a window of size 300.
 
 - MacBook Pro (Retina, 15-inch, Mid 2015)
 - 2.8 GHz Intel Core i7
 - 16 GB 1600 MHz DDR3

 1. Python 2.7.12, using single core:
 
 ```bash
 time python2 main.py
 ```
 `real	0m25.259s`  
 `user	0m25.086s`  
 `sys	0m0.154s`  

 2. Python 3.5.2, using single core:
 
 ```bash
 time python3 main.py
 ```
 `real	0m33.899s`  
 `user	0m33.684s`  
 `sys	0m0.182s`  
 
 3. PyPy 2.7.10, using single core:
 
 ```bash
 time pypy main.py
 ```
 
 `real	0m7.076s`  
 `user	0m6.804s`  
 `sys	0m0.180s`  
 
 
 Moral of the story - Iterators are fun, and PyPy is fast.