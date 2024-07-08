# 1166 - Toss Strange Coins

## Metadata

 - Difficulty: `Medium`
 - Link: https://www.leetcode.com/problems/toss-strange-coins

## Content

<p>You have some coins.&nbsp; The <code>i</code>-th&nbsp;coin has a probability&nbsp;<code>prob[i]</code> of facing heads when tossed.</p>

<p>Return the probability that the number of coins facing heads equals <code>target</code> if you toss every coin exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> prob = [0.4], target = 1
<strong>Output:</strong> 0.40000
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> prob = [0.5,0.5,0.5,0.5,0.5], target = 0
<strong>Output:</strong> 0.03125
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prob.length &lt;= 1000</code></li>
	<li><code>0 &lt;= prob[i] &lt;= 1</code></li>
	<li><code>0 &lt;= target&nbsp;</code><code>&lt;= prob.length</code></li>
	<li>Answers will be accepted as correct if they are within <code>10^-5</code> of the correct answer.</li>
</ul>


## Hint

- What about solving the problem with DP?
- Use DP with two states dp[pos][cnt], where pos represents the pos-th coin and cnt is the number of heads seen so far.
- You can do the transitions with a little bit math.
- For the base case, when pos == n return (cnt == target) to filter out the invalid scenarios.

