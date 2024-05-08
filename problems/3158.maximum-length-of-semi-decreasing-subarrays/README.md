# 3158 - Maximum Length of Semi-Decreasing Subarrays

## Metadata

 - Difficulty: `Medium`
 - Link: https://www.leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays

## Content

<p>You are given an integer array <code>nums</code>.</p>

<p>Return <em>the length of the <strong>longest semi-decreasing</strong> subarray of </em><code>nums</code><em>, and </em><code>0</code><em> if there are no such subarrays.</em></p>

<ul>
	<li>A <b>subarray</b> is a contiguous non-empty sequence of elements within an array.</li>
	<li>A non-empty array is <strong>semi-decreasing</strong> if its first element is <strong>strictly greater</strong> than its last element.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,6,5,4,3,2,1,6,10,11]
<strong>Output:</strong> 8
<strong>Explanation:</strong> Take the subarray [7,6,5,4,3,2,1,6].
The first element is 7 and the last one is 6 so the condition is met.
Hence, the answer would be the length of the subarray or 8.
It can be shown that there aren&#39;t any subarrays with the given condition with a length greater than 8.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [57,55,50,60,61,58,63,59,64,60,63]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Take the subarray [61,58,63,59,64,60].
The first element is 61 and the last one is 60 so the condition is met.
Hence, the answer would be the length of the subarray or 6.
It can be shown that there aren&#39;t any subarrays with the given condition with a length greater than 6.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since there are no semi-decreasing subarrays in the given array, the answer is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hint

- First, solve the problem assuming <code>nums</code> contains distinct values.
- Make a new array with each element being the pair <code>(nums[i], i)</code> for every <code>i</code> and call it <code>num_ind</code>.
- Sort <code>num_ind</code> in decreasing order.
- Iterate over <code>num_ind</code> and store a variable that represents the minimum index (i.e. min of <code>num_ind[i].second</code>) that has been iterated until now. Call it <code>min_index</code>
- Now if you are currently on pair <code>(nums[x], x)</code>, then <code>ans = max(ans, min_index - x)</code>.
- Now try to remove the first assumption.

