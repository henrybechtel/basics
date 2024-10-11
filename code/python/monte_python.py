import random as random
import sys

# name = sys.argv[1]
# print(f"Hello, {name}!")

'''
# Hypothiesis testing with an assumed model (DGP)
Let's suppose you come across a coin that has been flipped x times and has landed on heads y of those times. 
Is it a fair coin?
First, we need to state the null hypothesis: 
"The coin is fair and the y heads are the result of random chance"
Our test statistic will be the sum (count) of all the heads flipped.
Here we have a DGP model to simulate the conditionsa of the null hypothesis: a binary random variable with equal probability of landing heads or tails.
'''


# Defining our null hypothesis as a function
def coin_flip(null_hyp_prob = 0.5):
    ''' Function returns 1 for heads and 0 for tails. '''
    result = 1 if random.random() >= null_hyp_prob else 0
    return result


def main():
    # number_of_flips = 30
    # observed_heads = 21

    number_of_flips = int(input("How many flips of the coin did you observe?  "))
    observed_heads = int(input("How many heads did you observe?  "))

    trials = 1000000
    print(f"Running {trials} trials to simulate how often we'd expect to see a result at least this big...")

    count = 0
    for i in range(trials):
        trial_heads = 0
        for flip in range(number_of_flips):
            trial_heads += coin_flip()

        # how many times would we have seen something like what we observed (or even more extreme)    
        if trial_heads >= observed_heads:
            count += 1

    p = count/trials
    print(f"p-value: {p}")

    # Arbitrary p-value threshold interpretation:
    if p < 0.05:
        print("The coin is likely biased. We should reject the null hypothesis.")
    else:
        print("The null hypothesis couldn't be rejected.")


if __name__ == "__main__":
    main()