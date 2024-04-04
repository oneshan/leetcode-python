# 2738 - Count the Number of K-Free Subsets

## Metadata

 - Difficulty: `Medium`
 - Link: https://www.leetcode.com/problems/count-the-number-of-k-free-subsets

## Content

<p>You are given an integer array <code>nums</code>,&nbsp;which contains <strong>distinct</strong> elements and an integer <code>k</code>.</p>

<p>A subset is called a <strong>k-Free</strong> subset if it contains <strong>no</strong> two elements with an absolute difference equal to <code>k</code>. Notice that the empty set is a <strong>k-Free</strong> subset.</p>

<p>Return <em>the number of <strong>k-Free</strong> subsets of </em><code>nums</code>.</p>

<p>A <b>subset</b> of an array is a selection of elements (possibly none) of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,6], k = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> There are 5 valid subsets: {}, {5}, {4}, {6} and {4, 6}.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,5,8], k = 5
<strong>Output:</strong> 12
<strong>Explanation:</strong> There are 12 valid subsets: {}, {2}, {3}, {5}, {8}, {2, 3}, {2, 3, 5}, {2, 5}, {2, 5, 8}, {2, 8}, {3, 5} and {5, 8}.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,5,9,11], k = 20
<strong>Output:</strong> 16
<strong>Explanation:</strong> All subsets are valid. Since the total count of subsets is 2<sup>4 </sup>= 16, so the answer is 16. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
</ul>


## Hint

- Split all numbers into several groups, with each group being an arithmetic sequence with a common difference of k.
- How many K-free subsets are there for each group? This can be solved by dp: dp[i] = dp[i-1] + dp[i-2], meaning if we choose ith element, we cannot choose (i-1)th; otherwise we can choose (i-1)th element.
- After solving the problem for every group, the final result is just the product of the sub-problems.
- Split all numbers into several groups, with each group being an arithmetic sequence with a common difference of k.

