<TeXmacs|1.99.2>

<style|article>

<\body>
  Let <math|T> denote the whole triangle, with <math|n> rows. By brute force
  there are

  <\eqnarray*>
    <tformat|<table|<row|<cell|<big|sum><rsub|k=1><rsup|n><binom|k|2>+k>|<cell|=>|<cell|<binom|n+1|3>+<binom|n+1|2>>>|<row|<cell|>|<cell|=>|<cell|<binom|n+2|3>>>>>
  </eqnarray*>

  sub-triangles. For <math|n=1000>,

  <\eqnarray*>
    <tformat|<table|<row|<cell|<binom|1002|3>>|<cell|\<approx\>>|<cell|1.67\<times\>10<rsup|8>>>>>
  </eqnarray*>

  And each sub-triangle has to be summed over; so brute force is out of the
  question. We proceed to solve the minimum sub-triangle sum problem by
  induction. Let <math|t<rsub|k,i><around*|(|r|)>> be the sum of a
  sub-triangle whose bottom is on row <math|r> (wrt to <math|T>), whose
  bottom row contains <math|k> numbers, and whose bottom left entry is at
  index <math|i> on row <math|r>. We'll use zero-based indexing.

  In the base case we have a triangle with zero rows<emdash>whose minimum
  sub-triangle is the vacuous one of sum 0. Now, assume that for <math|n-1>
  rows we know the global minimum sub-triangle sum, and the ``suffix'
  sub-triangle sums <math|S<rsub|n-1>=<around*|{|t<rsub|k,i><around*|(|n-1|)>\<of\>1\<leq\>k\<leq\>n-1,0\<leq\>i\<leq\>n-1-k|}>>.
  Proceeding to the <math|n>th row,\ 

  <\render-code>
    for each <math|t<rsub|i,k>\<in\>S<rsub|n-1>>:

    \ \ \ \ if <math|T<around*|[|n|]><around*|[|i\<of\>i+k+1|]>+t<rsub|i,k>\<gtr\>global>:

    \ \ \ \ \ \ \ \ global = <math|T<around*|[|n|]><around*|[|i\<of\>i+k+1|]>+t<rsub|i,k>>

    \ \ \ \ \ \ \ \ <math|t<rsub|i,k> \<plusassign\>
    T<around*|[|n|]><around*|[|i\<of\>i+k+1|]>>

    \ \ \ \ else if <math|T<around*|[|n|]><around*|[|i\<of\>i+k+1|]>+t<rsub|i,k>\<less\>0>:

    \;
  </render-code>

  \;

  \;

  \;

  The number of suffix sub-triangles for row <math|n> is
</body>