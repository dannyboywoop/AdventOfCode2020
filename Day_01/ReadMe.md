# Day 1: [Report Repair](https://adventofcode.com/2020/day/1)

## Problem Definition

### Part One

After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

```
1721
979
366
299
675
1456
```

In this list, the two entries that sum to `2020` are `1721` and `299`. Multiplying them together produces `1721 * 299 = 514579`, so the correct answer is `514579`.

Of course, your expense report is much larger. Find the two entries that sum to `2020`; what do you get if you multiply them together?

### Part Two

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to `2020` are `979`, `366`, and `675`. Multiplying them together produces the answer, `241861950`.

In your expense report, what is the product of the three entries that sum to `2020`?

## Notes on my solution

The "brute force" solution to part 1 would be as follows:

```pseudocode
for i in range(dataset_size):
	for j in range(i+1, dataset_size):
		if (dataset[i]+dataset[j] == 2020):
			return dataset[i]*dataset[j]
```

This has a time complexity of O(n^2), where n is the size of the dataset. Note for part 2, this would become O(n^3) as you would need to loop over i, j and k.

To improve on this I stored the data in a hash set, this allows you to check for the existence of a number in the set in time O(1). I could then improve the time complexity of the solution to O(n) for part 1:

```pseudocode
while dataset is not empty:
	value = dataset.pop()
	complement = 2020-value
	if complement is in dataset:
		return value*complement
```

For part two I extended my solution to part 1, via recursion, to allow you to check for a set of m numbers that sum 2020. The time complexity for this is O(n<sup>m-1</sup>).