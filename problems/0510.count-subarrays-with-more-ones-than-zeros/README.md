# 0510 - Count Subarrays With More Ones Than Zeros

## Metadata

 - Difficulty: `Medium`
 - Link: https://www.leetcode.com/problems/count-subarrays-with-more-ones-than-zeros

## Content

<p>You are given a binary array <code>nums</code> containing only the integers <code>0</code> and <code>1</code>. Return<em> the number of <strong>subarrays</strong> in nums that have <strong>more</strong> </em><code>1</code>&#39;<em>s than </em><code>0</code><em>&#39;s. Since the answer may be very large, return it <strong>modulo</strong> </em><code>10<sup>9</sup> + 7</code>.</p>

<p>A <strong>subarray</strong> is a contiguous sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1,0,1]
<strong>Output:</strong> 9
<strong>Explanation:</strong>
The subarrays of size 1 that have more ones than zeros are: [1], [1], [1]
The subarrays of size 2 that have more ones than zeros are: [1,1]
The subarrays of size 3 that have more ones than zeros are: [0,1,1], [1,1,0], [1,0,1]
The subarrays of size 4 that have more ones than zeros are: [1,1,0,1]
The subarrays of size 5 that have more ones than zeros are: [0,1,1,0,1]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
No subarrays have more ones than zeros.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The subarrays of size 1 that have more ones than zeros are: [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1</code></li>
</ul>


## Hint

- Change the zeros in nums to -1 and create a prefix sum array prefixSum using the new nums.
- If prefixSum[i] for any index i in the range 0 <= i < prefixSum.length is positive, that means that there are more ones than zeros in the prefix ending at index i.
- If prefixSum[j] > prefixSum[i] for two indexes i and j such that 0 <= i < j < prefixSum.length, that means that there are more ones than zeros in nums in the range [i + 1 : j] (inclusive)

