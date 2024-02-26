# 1221 - Element Appearing More Than 25% In Sorted Array

## Metadata

 - Difficulty: `Easy`
 - Link: https://www.leetcode.com/problems/element-appearing-more-than-25-in-sorted-array

## Content

<p>Given an integer array <strong>sorted</strong> in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,2,6,6,6,6,7,10]
<strong>Output:</strong> 6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hint

- Divide the array in four parts [1 - 25%] [25 - 50 %] [50 - 75 %] [75% - 100%]
- The answer should be in one of the ends of the intervals.
- In order to check which is element is the answer we can count the frequency with binarySearch.

