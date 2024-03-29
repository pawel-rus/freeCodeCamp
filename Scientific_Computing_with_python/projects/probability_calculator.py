import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents =[]
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, number):
        if number > len(self.contents):
            balls_drawn = self.contents
            self.contents = []
            return balls_drawn
        else:
            balls_drawn = random.sample(self.contents, number)
            for ball in balls_drawn:
                self.contents.remove(ball)
            return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    copied_hat = copy.deepcopy(hat)
    for _ in range(num_experiments):
        copied_hat = copy.deepcopy(hat)
        success = True
        balls_drawn = copied_hat.draw(num_balls_drawn)
        for color, amount in expected_balls.items():
            if balls_drawn.count(color) < amount:
                success = False
        if success:
            count += 1
    return count / num_experiments