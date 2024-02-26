# 0567 - Permutation in String

## Metadata

 - Difficulty: `Medium`
 - Link: https://www.leetcode.com/problems/permutation-in-string

## Content

<p>Given two strings <code>s1</code> and <code>s2</code>, return <code>true</code><em> if </em><code>s2</code><em> contains a permutation of </em><code>s1</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>In other words, return <code>true</code> if one of <code>s1</code>&#39;s permutations is the substring of <code>s2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidbaooo&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s2 contains one permutation of s1 (&quot;ba&quot;).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidboaoo&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>


## Hint

- Obviously, brute force will result in TLE. Think of something else.
- How will you check whether one string is a permutation of another string?
- One way is to sort the string and then compare. But, Is there a better way?
- If one string is a permutation of another string then they must one common metric. What is that?
- Both strings must have same character frequencies, if  one is permutation of another. Which data structure should be used to store frequencies?
- What about hash table?  An array of size 26?

