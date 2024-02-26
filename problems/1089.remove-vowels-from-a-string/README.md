# 1089 - Remove Vowels from a String

## Metadata

 - Difficulty: `Easy`
 - Link: https://www.leetcode.com/problems/remove-vowels-from-a-string

## Content

<p>Given a string <code>s</code>, remove the vowels <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code> from it, and return the new string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcodeisacommunityforcoders&quot;
<strong>Output:</strong> &quot;ltcdscmmntyfrcdrs&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aeiou&quot;
<strong>Output:</strong> &quot;&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>


## Hint

- How to erase vowels in a string?
- Loop over the string and check every character, if it is a vowel ignore it otherwise add it to the answer.

