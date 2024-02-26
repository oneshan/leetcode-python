# 1697 - Strings Differ by One Character

## Metadata

 - Difficulty: `Medium`
 - Link: https://www.leetcode.com/problems/strings-differ-by-one-character

## Content

<p>Given a list of strings <code>dict</code> where all the strings are of the same length.</p>

<p>Return <code>true</code> if there are 2 strings that only differ by 1 character in the same index, otherwise return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> dict = [&quot;abcd&quot;,&quot;acbd&quot;, &quot;aacd&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Strings &quot;a<strong>b</strong>cd&quot; and &quot;a<strong>a</strong>cd&quot; differ only by one character in the index 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> dict = [&quot;ab&quot;,&quot;cd&quot;,&quot;yz&quot;]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> dict = [&quot;abcd&quot;,&quot;cccc&quot;,&quot;abyd&quot;,&quot;abab&quot;]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of characters in <code>dict &lt;= 10<sup>5</sup></code></li>
	<li><code>dict[i].length == dict[j].length</code></li>
	<li><code>dict[i]</code> should be unique.</li>
	<li><code>dict[i]</code> contains only lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve this problem in <code>O(n * m)</code> where n is the length of <code>dict</code> and <code>m</code> is the length of each string.</p>


## Hint

- BruteForce, check all pairs and verify if they differ in one character. O(n^2 * m) where n is the number of words and m is the length of each string.
- O(m^2 * n), Use hashset, to insert all possible combinations adding a character "*". For example: If dict[i] = "abc", insert ("*bc", "a*c" and "ab*").

