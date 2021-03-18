# FCP Gym

FC Portugal 3D gym environment to train a kick in motion for the RoboCup 3D Simulation League.

It uses OpenAI [Gym](https://gym.openai.com/docs/) under the hood, so the API is the same.

To run the environment with randomly sampled actions:

```python
import fcpgym as gym

env = gym.make('KickInMotion', host="localhost", agent_port=3100, monitor_port=3200)
for _ in range(10):
	obs = env.reset()
	done = False
	while not done:
		action = env.action_space.sample()
		obs, reward, done, info = env.step(action)
env.close()
```

# Operating System

[Ubuntu 18](http://releases.ubuntu.com/18.04/).

# Server

1. Install dependencies:

    ```bash
    sudo apt-get install g++ git cmake libfreetype6-dev libode-dev libsdl-dev ruby ruby-dev libdevil-dev libboost-dev libboost-thread-dev libboost-regex-dev libboost-system-dev qt4-default
    ```

2. Download the SimSpark repository:

    ```bash
    git clone https://gitlab.com/robocup-sim/SimSpark.git
    ```

3. Build and install:

    ```bash
    cd SimSpark
    sudo ./build.sh
    ```

4. Change the following settings:

    ```bash
    /usr/local/share/rcssserver3d/rcssserver3d.rb
        $enableRealTimeMode = false
    /usr/local/share/rcssserver3d/naosoccersim.rb
        addSoccerVar('BeamNoiseXY',0.0)
        addSoccerVar('BeamNoiseAngle',0.0)
        #gameControlServer.initControlAspect('SoccerRuleAspect')
    /usr/local/share/rcssserver3d/rsg/agent/nao/naoneckhead.rsg
        (setViewCones 120 120) ; 
        (setSenseMyPos true) ;
        (setSenseMyOrien true) 
        (setSenseBallPos true) ; 
        (addNoise true)
    ~/.simspark/spark.rb
        $agentSyncMode = true
    ```

# Viewer

1. Install dependencies:

    ```bash
    sudo apt install openjdk-8-jdk
    ```

2. Download the RoboViz repository:

    ```bash
    git clone https://github.com/magmaOffenburg/RoboViz.git
    ```

3. Build and install:

    ```bash
    cd RoboViz/scripts
    ./build.sh
    echo "alias roboviz='$PWD/../bin/roboviz.sh'" >> ~/.bash_aliases
    ```

4. Open the viewer:

    ```bash
    roboviz
    ```

# FCP Gym

1. Install dependencies:

    ```bash
    sudo apt install libboost-dev libboost-regex-dev libicu-dev libboost-system-dev libboost-program-options-dev libboost-thread-dev zlib1g-dev ruby ruby-dev libfreetype6-dev libode-dev g++ subversion cmake libsdl-dev libdevil-dev qt4-default libgtk2.0-dev libxml2-dev liblua5.1-0-dev libboost-filesystem-dev libgsl-dev python3-dev
    ```

2. Run the example:

    ```bash
    python3 example.py
    ```
