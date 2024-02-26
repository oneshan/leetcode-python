# 1131 - Count Substrings with Only One Distinct Letter

## Metadata

 - Difficulty: `Easy`
 - Link: https://www.leetcode.com/problems/count-substrings-with-only-one-distinct-letter

## Content

<p>Given a string <code>s</code>, return <em>the number of substrings that have only <strong>one distinct</strong> letter</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaaba&quot;
<strong>Output:</strong> 8
<strong>Explanation: </strong>The substrings with one distinct letter are &quot;aaa&quot;, &quot;aa&quot;, &quot;a&quot;, &quot;b&quot;.
&quot;aaa&quot; occurs 1 time.
&quot;aa&quot; occurs 2 times.
&quot;a&quot; occurs 4 times.
&quot;b&quot; occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaaaaaaaaa&quot;
<strong>Output:</strong> 55
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> consists of only lowercase English letters.</li>
</ul>


## Hint

- What if we divide the string into substrings containing only one distinct character with maximal lengths?
- Now that you have sub-strings with only one distinct character, Try to come up with a formula that counts the number of its sub-strings.
- Alternatively, Observe that the constraints are small so you can use brute force.

