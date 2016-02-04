<TeXmacs|1.99.2>

<style|article>

<\body>
  On iteration 0, we have 4 gaps. The successive placement of each cirlce
  within a gap replaces the gap with 3 gaps. Recursively, denote
  <math|G<rsub|n>> the number of gaps at iteration <math|n>:

  <\eqnarray*>
    <tformat|<table|<row|<cell|G<rsub|0>>|<cell|=>|<cell|4>>|<row|<cell|G<rsub|n>>|<cell|=>|<cell|3G<rsub|n-1>>>>>
  </eqnarray*>

  so that

  <\eqnarray*>
    <tformat|<table|<row|<cell|G<rsub|n>>|<cell|=>|<cell|4\<cdot\>3<rsup|n>>>>>
  </eqnarray*>

  \;
</body>