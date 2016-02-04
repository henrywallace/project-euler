<TeXmacs|1.99.2>

<style|article>

<\body>
  We seek integers <math|m,n> such that\ 

  <\eqnarray*>
    <tformat|<table|<row|<cell|log<rsub|10>m<rsup|n>>|<cell|\<in\>>|<cell|<around*|[|n-1,n|)>>>|<row|<cell|n>|<cell|\<in\>>|<cell|<around*|[|10<rsup|1-1/m>,10|)>>>>>
  </eqnarray*>

  And we restrict ourselves to <math|n\<gtr\>0> for obvious reasons. Note
  that <math|10<rsup|n>> is an <math|n+1> digit number, so that
  <math|m\<less\>9>. We get the first unachievable <math|n> digit number
  whenever

  <\eqnarray*>
    <tformat|<table|<row|<cell|log<rsub|10>9<rsup|n>>|<cell|\<less\>>|<cell|n-1>>>>
  </eqnarray*>

  by the first inequality. Or, simplified,

  <\eqnarray*>
    <tformat|<table|<row|<cell|m>|<cell|\<gtr\>>|<cell|<frac|1|1-log<rsub|10>9>>>|<row|<cell|>|<cell|\<approx\>>|<cell|21.8>>>>
  </eqnarray*>

  Thus to calculate the answer, we simply calculate the sum

  <\equation*>
    <big|sum><rsub|m=1><rsup|21>10-<around*|\<lceil\>|10<rsup|1-1/m>|\<rceil\>>
  </equation*>
</body>