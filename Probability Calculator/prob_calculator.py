import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **args):
    self.contents = []
    for key, value in args.items():
      if value == 1:
        self.contents.append(key)
      else:
        for i in range(value):
          self.contents.append(key)
  
  def draw(self, num_balls_drawn):
    balls_drawn = []
    if num_balls_drawn >= len(self.contents):
      balls_drawn = copy.deepcopy(self.contents)
      self.contents.clear()
    else:
      for i in range(num_balls_drawn):
        ball_chosen = random.choice(self.contents)
        balls_drawn.append(ball_chosen)
        self.contents.remove(ball_chosen)
    return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_count = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)
    success = False
    for key, value in expected_balls.items():
      if balls_drawn.count(key) >= value:
        success = True
      else:
        success = False
        break
    if success:
      success_count += 1
  probability = success_count / num_experiments
  return probability
