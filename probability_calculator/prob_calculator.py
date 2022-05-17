import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents

        balls = []
        for _ in range(num_balls):
            selected_ball = random.randrange(len(self.contents))
            balls.append(self.contents.pop(selected_ball))
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_number_balls = list(expected_balls.values())

    success = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)

        number_balls = []
        for key in expected_balls.keys():
            number_balls.append(balls.count(key))

        if number_balls >= expected_number_balls:
            success += 1

    return success / num_experiments