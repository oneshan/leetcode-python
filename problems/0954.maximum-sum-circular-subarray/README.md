# 0954 - Maximum Sum Circular Subarray

## Metadata

 - Difficulty: `Medium`
 - Link: https://www.leetcode.com/problems/maximum-sum-circular-subarray

## Content

<p>Given a <strong>circular integer array</strong> <code>nums</code> of length <code>n</code>, return <em>the maximum possible sum of a non-empty <strong>subarray</strong> of </em><code>nums</code>.</p>

<p>A <strong>circular array</strong> means the end of the array connects to the beginning of the array. Formally, the next element of <code>nums[i]</code> is <code>nums[(i + 1) % n]</code> and the previous element of <code>nums[i]</code> is <code>nums[(i - 1 + n) % n]</code>.</p>

<p>A <strong>subarray</strong> may only include each element of the fixed buffer <code>nums</code> at most once. Formally, for a subarray <code>nums[i], nums[i + 1], ..., nums[j]</code>, there does not exist <code>i &lt;= k1</code>, <code>k2 &lt;= j</code> with <code>k1 % n == k2 % n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,-2,3,-2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Subarray [3] has maximum sum 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,-3,5]
<strong>Output:</strong> 10
<strong>Explanation:</strong> Subarray [5,5] has maximum sum 5 + 5 = 10.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [-3,-2,-3]
<strong>Output:</strong> -2
<strong>Explanation:</strong> Subarray [-2] has maximum sum -2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code></li>
</ul>


## Hint

- For those of you who are familiar with the <b>Kadane's algorithm</b>, think in terms of that. For the newbies, Kadane's algorithm is used to finding the maximum sum subarray from a given array. This problem is a twist on that idea and it is advisable to read up on that algorithm first before starting this problem. Unless you already have a great algorithm brewing up in your mind in which case, go right ahead!
- What is an alternate way of representing a circular array so that it appears to be a straight array?
Essentially, there are two cases of this problem that we need to take care of. Let's look at the figure below to understand those two cases:

<br>
<img src="https://assets.leetcode.com/uploads/2019/10/20/circular_subarray_hint_1.png" width="700"/>
- The first case can be handled by the good old Kadane's algorithm. However, is there a smarter way of going about handling the second case as well?

