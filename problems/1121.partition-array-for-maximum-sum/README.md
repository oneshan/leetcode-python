# 1121 - Partition Array for Maximum Sum

## Metadata

 - Difficulty: `Medium`
 - Link: https://www.leetcode.com/problems/partition-array-for-maximum-sum

## Content

<p>Given an integer array <code>arr</code>, partition the array into (contiguous) subarrays of length <strong>at most</strong> <code>k</code>. After partitioning, each subarray has their values changed to become the maximum value of that subarray.</p>

<p>Return <em>the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a <strong>32-bit</strong> integer.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,15,7,9,2,5,10], k = 3
<strong>Output:</strong> 84
<strong>Explanation:</strong> arr becomes [15,15,15,9,10,10,10]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
<strong>Output:</strong> 83
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [1], k = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 500</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= arr.length</code></li>
</ul>


## Hint

- Think dynamic programming:  dp[i] will be the answer for array A[0], ..., A[i-1].
- For j = 1 .. k that keeps everything in bounds, dp[i] is the maximum of dp[i-j] + max(A[i-1], ..., A[i-j]) * j .

