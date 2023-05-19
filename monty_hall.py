from numpy import random as rand
import numpy as np

if __name__ == "__main__":
    answer = input("Should the player change their second pick? yes(Y)/no(N)");

    if answer == "Y" or answer == "yes":
        change_second_time = True;
    elif answer == "N"  or answer == "no":
        change_second_time = False;
    else:
        raise ValueError("You should provide a yes(Y)/no(N) answer!")

    num_of_tests = 500000;
    num_of_success = 0;

    for i in range(num_of_tests):
        goat_index = rand.randint(0,3);
        doors = np.array([i==goat_index for i in range(3)]);
        player_pick = rand.randint(0,3);
        elimination_index = (player_pick + 1) % 3;
        if elimination_index == goat_index:
            elimination_index = (elimination_index + 1) % 3;
        player_pick = (player_pick + 1) % 3;
        if change_second_time:
            if player_pick == elimination_index:
                player_pick = (player_pick + 1) % 3;
        if player_pick == goat_index:
            num_of_success += 1;
    phrase = "with" if change_second_time else "without";
    print(f"The rate of success is {(num_of_success/num_of_tests):0.4f} {phrase} the player changing their pick for the second time.")