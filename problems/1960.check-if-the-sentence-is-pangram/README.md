# 1960 - Check if the Sentence Is Pangram

## Metadata

 - Difficulty: `Easy`
 - Link: https://www.leetcode.com/problems/check-if-the-sentence-is-pangram

## Content

<p>A <strong>pangram</strong> is a sentence where every letter of the English alphabet appears at least once.</p>

<p>Given a string <code>sentence</code> containing only lowercase English letters, return<em> </em><code>true</code><em> if </em><code>sentence</code><em> is a <strong>pangram</strong>, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;thequickbrownfoxjumpsoverthelazydog&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> sentence contains at least one of every letter of the English alphabet.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;leetcode&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 1000</code></li>
	<li><code>sentence</code> consists of lowercase English letters.</li>
</ul>


## Hint

- Iterate over the string and mark each character as found (using a boolean array, bitmask, or any other similar way).
- Check if the number of found characters equals the alphabet length.

