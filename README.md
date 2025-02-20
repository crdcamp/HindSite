# The Preliminary Purpose of This README.md File

As of now, this README.md file is for personal notes I can refer to while discovering how a Monte Carlo simulation works. Big thanks to the book "Fooled by Randomness", by Nassim Nicholas Taleb, for inspiring this super interesting project.

# An Introduction To The Monte Carlo Simulation

We'll start with [this lecture](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/resources/lecture-6-monte-carlo-simulation/) from MIT Open Course Ware. Thank you Professor Guttag for the free lesson!

## Inferential Statistics

> A Monte Carlo simulation is "a method of estimating the value of an unknown quantity using the principles of inferential statistics".
>
> - **Population**: A set of examples
> - **Sample**: A proper subset of a population
> - A random sample tends to exhibit the same properties as the population from which it is drawn.

These are things we already know, but they are important to keep in mind.

Guttag then references the classic example of a coin flip to illustrate the idea. Ironically, this is something that Taleb thinks is a poor approach to understanding the true notions behind the simulation.

It's as simple as it gets: the more you flip the coin, the more the sample population tends to show that the coin flip has 50/50 odds.

> **Confidence in our estimate depends on two things:**
>
> - Size of the sample
> - Variable of the sample
> - As the variance grows, we need larger samples to have the same degree of confidence

Again, all very simple and familiar concepts.
