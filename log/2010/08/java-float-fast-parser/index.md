# 🐌 Float.parseFloat is slow

While profiling some loader code and expecting to see performance issues with
my regular expressions, I found that ~60% of my time was actually spent
converting String variables to floats. It turns out that the slow bit lives
inside [Float.parseFloat](https://web.archive.org/web/20150503161221/http://www.java2s.com/Open-Source/Java-Document/Apache-Harmony-Java-SE/org-package/org/apache/harmony/luni/util/FloatingPointParser.java.htm)
where it calls String.toLowerCase every single time just in case this string
is a hex float, a very rare type of float which I had never seen before. I
[logged this with Apache](https://web.archive.org/web/20150503161221/https://issues.apache.org/jira/browse/HARMONY-6635)
but as I can't ship a custom ROM with my SVG parser I decided to replace it.
Here's the results from some tests of 3896 calls to parseFloat on my Nexus One:

* a Using Float.parseFloat(String): 1516.449ms
* b My own parseFloat(String): 654.882ms
* c ...and my own isDigit(char): 449.622
* d ...and isDigit written inline: 295.865ms
* e ...copying the string into a char buffer and avoiding all string access and
  method calls: 254.527ms (112ms spent copying the characters!)

So in theory, if the method took a character buffer and length it could be as
short as 135ms, over ten times faster than Float.parseFloat. I'm currently using
option d as gives a nice performance gain without breaking my design, but when
performance tuning the entire API later this may see some huge changes. Here's
the function I cooked up:

```java
public static float parseFloat(String f) {
	final int len   = f.length();
	float     ret   = 0f;         // return value
	int       pos   = 0;          // read pointer position
	int       part  = 0;          // the current part (int, float and sci parts of the number)
	boolean   neg   = false;      // true if part is a negative number

	// find start
	while (pos < len && (f.charAt(pos) < '0' || f.charAt(pos) > '9') && f.charAt(pos) != '-' && f.charAt(pos) != '.')
		pos++;

	// sign
	if (f.charAt(pos) == '-') {
		neg = true;
		pos++;
	}

	// integer part
	while (pos < len && !(f.charAt(pos) > '9' || f.charAt(pos) < '0'))
		part = part*10 + (f.charAt(pos++) - '0');
	ret = neg ? (float)(part*-1) : (float)part;

	// float part
	if (pos < len && f.charAt(pos) == '.') {
		pos++;
		int mul = 1;
		part = 0;
		while (pos < len && !(f.charAt(pos) > '9' || f.charAt(pos) < '0')) {
			part = part*10 + (f.charAt(pos) - '0');
			mul*=10; pos++;
		}
		ret = neg ? ret - (float)part / (float)mul : ret + (float)part / (float)mul;
	}

	// scientific part
	if (pos < len && (f.charAt(pos) == 'e' || f.charAt(pos) == 'E')) {
		pos++;
		neg = (f.charAt(pos) == '-'); pos++;
		part = 0;
		while (pos < len && !(f.charAt(pos) > '9' || f.charAt(pos) < '0')) {
			part = part*10 + (f.charAt(pos++) - '0');
		}
		if (neg)
			ret = ret / (float)Math.pow(10, part);
		else
			ret = ret * (float)Math.pow(10, part);
	}
	return ret;
```

This is of course a very crude method, it requires a well-formed number and
will return 0 or partial numbers instead of raising exceptions, it doesn't work
with hex floats or parse NaNs or Infinity and it doesn't use doubles internally
so the accuracy is not perfect. It does however work for my purposes, so I
thought I'd share it with the Internet.

