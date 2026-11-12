# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last `n` items of `items` appended to a fresh list (or a caller-supplied list) without mutating state across separate function calls.
- **Current Issue**: Two defects exist: (1) an off-by-one indexing error (`len(items) - n + 1`) skips the first of the `n` requested elements, and (2) using a mutable default list `target_list=[]` causes results from previous calls to persist into subsequent calls.

## bug2.js
- **Intended Behavior**: Asynchronously fetch the tax rate for each cart item, compute the accurate taxed subtotal, apply a flat $10 discount when `"SAVE10"` is passed, and return the final total rounded to 2 decimal places.
- **Current Issue**: `Array.prototype.forEach` does not await `async` callbacks, so `calculateCartTotal` applies the discount and returns `subtotal` before any tax rates resolve (resulting in `-10` instead of `45`).

## bug3.java
- **Intended Behavior**: Safely check whether a user's list of roles contains the target `requiredRole` string, returning `false` if `roles` is null/empty or no match is found.
- **Current Issue**: Two defects exist: (1) calling `roles.isEmpty()` before checking `roles == null` throws a `NullPointerException` on null input, and (2) comparing strings with `==` instead of `.equals()` checks object reference identity rather than string value equality.

## bug4.py
- **Intended Behavior**: Perform a binary search on a sorted list of integers to return the earliest (leftmost) index of `target`, or `-1` if `target` does not exist.
- **Current Issue**: When `sorted_nums[mid] == target`, setting `right = mid` without recording the found index or breaking when `left == right` triggers an infinite loop and never returns the matched index.

## bug5.sql
- **Intended Behavior**: Query all active (`deleted_at IS NULL`) customers who have strictly more than 2 completed orders in 2026, returning their ID, full name, email, order count, and total spend.
- **Current Issue**: Three defects exist: (1) `c.deleted_at = NULL` always evaluates to `UNKNOWN` instead of using `IS NULL`, (2) `c.full_name` and `c.email` are unaggregated columns missing from the `GROUP BY` clause, and (3) `HAVING COUNT(o.order_id) >= 2` includes customers with exactly 2 orders instead of strictly more than 2 (`> 2`).
