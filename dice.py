def calc_combinations(dice1, dice2):
    count = 0 #Initialize a counter variable to keep track of the total number of combinations
    for num1 in dice1: #This starts the first loop, iterating over each number in the dice1 list.
        for num2 in dice2:
            count += 1
    return count

def calc_distribution(dice1, dice2):
    sum_array = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    for i1 in range(0, 6):
        for i2 in range(0, 6):
            sum_array[i1][i2] = dice1[i1] + dice2[i2]
    return sum_array

def calc_probability(sum_array):
    prob_array = [0] * (13)
    for i1 in range(0, 6):
        for i2 in range(0, 6):
            prob_array[sum_array[i1][i2]] += 1

    return prob_array

def compare_probability(array1, array2):
    if len(array1) != len(array2):
        return False

    for i in range(0, len(array1)):
        if array1[i] != array2[i]:
            return False

    return True

def check_multiple(dice):
    for i1 in range(0, 5):
        for i2 in range(i1+1, 6):
            if dice[i1] == dice[i2]:
                return True
    return False

def update_dice(dice, minnum, maxnum):
    for i in range(5, -1, -1):
        dice[i] += 1
        if dice[i] < maxnum:
            break
        else:
            dice[i] = minnum

    return dice

def undom_dice(prob_array):
    new_die_a = [1, 1, 1, 1, 1, 1]
    new_die_b = [1, 2, 3, 4, 5, 6]

    while (True):
        # print("Trying " + str(new_die_a) + " " + str(new_die_b))
        new_sum_array = calc_distribution(new_die_a, new_die_b)
        new_prob_array = calc_probability(new_sum_array)
        if compare_probability(prob_array, new_prob_array):
            # print("****matches*****")
            # print(str(new_die_a))
            # print(str(new_die_b))
            # print(str(prob_array))
            # print(str(new_prob_array))
            # print(str(sum_array))
            # print(str(new_sum_array))
            break
        new_die_a = update_dice(new_die_a, 1, 5)
        while (True):
            new_die_b = update_dice(new_die_b, 1, 9)
            if not check_multiple(new_die_b):
                break
    return new_die_a, new_die_b

def main():
    dice1 = [1, 2, 3, 4, 5, 6]
    dice2 = [1, 2, 3, 4, 5, 6]

    count = calc_combinations(dice1, dice2)
    print("Number of possible combinations = " + str(count))

    sum_array = calc_distribution(dice1, dice2)
    print(str(sum_array))

    prob_array = calc_probability(sum_array)
    print(str(prob_array))
    # for i in range(0, len(prob_array)):
    #     if prob_array[i] == 0:
    #         continue
    #     print("P(" + str(i) + ") = " + str(prob_array[i]) + " / 36")

    new_die_a, new_die_b = undom_dice(prob_array)
    print("New_Die_A = " + str(new_die_a))
    print("New_Die_B = " + str(new_die_b))

if __name__ == "__main__":
    main()











