import fcpgym as gym

env = gym.make('KickInMotion', host="localhost", agent_port=3100, monitor_port=3200)
for _ in range(10):
	obs = env.reset()
	done = False
	while not done:
		action = env.action_space.sample()
		obs, reward, done, info = env.step(action)
env.close()
