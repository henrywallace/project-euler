<TeXmacs|1.99.2>

<style|article>

<\body>
  First, as with our example, let our bound <math|m=30>. Each composite must
  have exactly two prime divisors: <math|n=p q>. Let <math|p\<less\>q>. To
  find the number of composites, we count the number <math|n> with
  <math|p=2,3,5,7\<ldots\>> Let <math|i> be the index of <math|p> in the list
  of primes, and <math|j> be the index of the largest prime <math|p> could
  product with, <math|Q=<around*|\<lfloor\>|m/p|\<rfloor\>>>. The number of
  composites is then <math|<big|sum><rsub|p<rsub|i><rsup|2>\<less\>m><around*|(|j-i+1|)>>.
  To find <math|j>, we use a simple binary search.

  Now, what is the runtime of this? We need to generate a list of primes
  bounded by <math|<around*|\<lfloor\>|m/2|\<rfloor\>>>, the largest
  <math|Q>. We'll use the Sieve of Eratosthenes for a runtime: <math|log
  log<around*|\<lfloor\>|m/2|\<rfloor\>>>. Then we do <math|<sqrt|m>> binary
  searches on a set with size <math|k>, where <math|k> is the number of
  primes less than <math|<around*|\<lfloor\>|m/2|\<rfloor\>>>. The prime
  number theorem gives this to be <math|k=<around*|\<lfloor\>|m/2|\<rfloor\>>/log<around*|\<lfloor\>|m/2|\<rfloor\>>>.
  With <math|b=<around*|\<lfloor\>|m/2|\<rfloor\>>>, the total runtime is

  <\eqnarray*>
    <tformat|<table|<row|<cell|log log b\<ast\><sqrt|m> <around*|(|log b-log
    log b|)>>|<cell|=>|<cell|O<around*|(|<sqrt|b> <around*|(|log
    b-log<rsup|2> log b|)>|)>>>>>
  </eqnarray*>
</body>