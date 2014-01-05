Fort Calhoun Status Getter
===========

A python script that:
<ol>
<li>Uses Beautiful Soup and Mechanize to target the <a href="http://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/ps.html" target="_blank">current power capacity</a> of the Fort Calhoun Nuclear Station.</li>
<li>Evaluates whether the number is below 100; if so, it sends an email.</li>
<li>Sends out a status tweet via <a href="https://twitter.com/FortCalhounBot" target="_blank">this twitterbot.</a></li>
</ol>