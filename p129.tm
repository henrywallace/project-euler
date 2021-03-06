<TeXmacs|1.99.2>

<style|generic>

<\body>
  We can express a repunit number of length <math|k> as

  <\eqnarray*>
    <tformat|<table|<row|<cell|R<around*|(|k|)>>|<cell|=>|<cell|<big|sum><rsub|i=0><rsup|k-1>10<rsup|i>>>|<row|<cell|>|<cell|=>|<cell|<frac|1|9><around*|(|10<rsup|k>-1|)>>>>>
  </eqnarray*>

  And the function <math|A<around*|(|n|)>> is

  <\equation*>
    min<rsub|k> <around*|(|R<around*|(|k|)>\<equiv\>0 mod n|)>
  </equation*>

  The simplification of <math|R<around*|(|k|)>> with 9 in the denominator
  makes no sense for values <math|n>, <math|<around*|(|n,3|)>=3>, as this is
  equivalent to dividing by zero. As such, the inverse if it exists cannot be
  0.\ 
</body>